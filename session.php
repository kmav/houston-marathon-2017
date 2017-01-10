<?php
// Establishing Connection with Server by passing server_name, user_id and password as a parameter
//$connection = mysql_connect("localhost", "root", "");
// Selecting Database
// = mysql_select_db("company", $connection);
include ('db/connect.php');

$path = $_SERVER['REQUEST_URI'];


session_start();// Starting Session

// Storing Session
//Session variable is a dictionary that you can add any values that you want 
$user_check=$_SESSION['login_user'];

// SQL Query To Fetch Complete Information Of User
$ses_sql="select username,level from login where username='$user_check'";
$result = $db->query($ses_sql);
if ($result->num_rows==1){
    $row = $result -> fetch_assoc();
    $login_session =$row['username'];
    $level_session = $row['level'];
    
    $sql = "INSERT INTO userBehavior (tstamp,user,page) VALUES (NOW(),'$user_check','$path');";
    //echo $sql;
    $result = $db->query($sql);
    
}
else {
    if (strcmp($path,"/getMobile.php")==0){
        $user_check = "no_user";
        $sql = "INSERT INTO userBehavior (tstamp,user,page) VALUES (NOW(),'$user_check','$path');";
        if ($db->query($sql) === TRUE) {
            //echo "New record created successfully";
        } else {
            //echo "Error: " . $sql . "<br>" . $conn->error;
        }        // header("Location: index.php");
    }
    else{
        header("Location: index.php");

    }
}



?>
