<?php
//base of code from http://www.formget.com/login-form-in-php/
//modified for purposes of this project

include('login.php'); // Includes Login Script
include('php/isMobile.php');

if(isset($_SESSION['login_user']))
{
    //login was successful, redirect page to profile.php
    header("location: profile.php");
}

?>

<!DOCTYPE html>
<html>

<head>
    <script>
        // window.location = "http://marathon.iems.northwestern.edu/";
    </script>
<title>Chevron Houston Marathon 2017</title>
<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Ubuntu">

<?php 
    if ($mobile==true){
        echo "<link href='css/styled_login_mobile.css' rel='stylesheet' type='text/css'>";
    }
    else{
        echo "<link href='css/styled_login.css' rel='stylesheet' type='text/css'>";
    }
?>
<script src="js/googleAnalytics.js"></script>

</head>
<body>
<div id="main">
<h1>Houston Marathon 2017 </h1>
<h2 style="font-weight: normal;">Data Visualization System</h2>
<div id="login">
<h2>Login Form</h2>
<form action="" method="post">
<label>Username :</label>
<input id="name" name="username" placeholder="username" type="text">
<label>Password :</label>
<input id="password" name="password" placeholder="password" type="password">
<h4>Login will last: 2 hours</h4>
<h4>Not registered? Click <a style="color:blue;" href='newuser.php'>here</a> to make an account. Email marathondvs@gmail.com with any questions or concerns. </h4>
<input name="submit" type="submit" value=" Login ">
<!--<a href='getMobile.php'><div class='pagelink'>Mobile Version <span class='small'>(no login required)</span></div></a>-->
<br>
<span style="font-weight:normal;"><?php echo $error; ?></span></form>
</div>
</div>
</body>
</html>