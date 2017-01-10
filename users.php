<?php
    include('session.php');
?>
<!DOCTYPE html>
<html>
<head>
<title>User list</title>
<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Ubuntu">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
<script src="js/googleAnalytics.js"></script>

<link href="css/styled_login.css" rel="stylesheet" type="text/css">
</head>
<body>
<h1>Houston Marathon 2017</h1>
<h2>Data Visualization System</h2>

<div id="main">
    <div id='login'>
        <h2 id="welcome">Welcome : <?php echo $login_session; ?></h2>
        <h1></h1>
        
        
        <form action='index.php' method='post'>
            <input name='submit' type='submit' value="HOME">
        </form>
    </div>
</div>
<div class="container">
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>Username</th>
                        <th>Level</th>
                        <th>Last Login</th>
                    </tr>
                </thead>
                <tbody>
        <?php
            $admin = "bpeynetti";
            if (strcmp($admin,$login_session)==0){
                //admin (bpeynetti) 
                //we list out the stuff
                $sql = "select loginHistory.username user, login.level clearance, max(loginTime) lt from (loginHistory join login on login.username=loginHistory.username) group by login.username order by lt desc;";
                $result = $db->query($sql);
                if ($result->num_rows>0){
                    $users = array();
                    while ($row = $result -> fetch_assoc()){
                        echo "<tr><td>";
                        array_push($users,$row['user']);
                        echo $row['user']."</td><td>".$row['clearance']."</td><td>".$row['lt'];
                        echo "</tr>";
                    }
                }
            }
            else {
                header("location: index.php");
            }
        ?>
        
            </tbody>
        </table>
        </div>
</body>
</html>
