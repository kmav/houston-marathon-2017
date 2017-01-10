<?php

//connect to server
include('db/connect.php');
include('php/isMobile.php');

session_start(); // Starting Session
$error=''; // Variable To Store Error Message

if (isset($_POST['submit'])) {
    if (empty($_POST['username']) || empty($_POST['password'])) {
        //one of the two is empty
        $error = "Username or Password is invalid";
    }
    else
    {
        // Define $username and $password variables (get from the submission)
        $username=$_POST['username'];
        $password=$_POST['password'];
       
    
        // To protect MySQL injection for Security purpose
        $username = stripslashes($username);
        $password = stripslashes($password);
        //$username = mysql_real_escape_string($username);
        //$password = mysql_real_escape_string($password);
        
        // SQL query to fetch information of registerd users and finds user match.
        $sql = "select username,level from login where password='$password' and username='$username'";
        $result = $db->query($sql);
        //$query = mysql_query("select * from login where password='$password' AND username='$username'");
        if ($result->num_rows==1){
            $row = $result -> fetch_assoc();
            $level = $row['level'];
            //how to keep track of who logged in
            $_SESSION['login_user'] = $username; // Initializing Session
            $_SESSION['start'] = time();
            header("location: profile.php");
            
            //now record that login attempt
            $sql = "insert into loginHistory (username,loginTime) VALUES ('$username',NOW());";
            $reslt = $db->query($sql);
        }
        else{
            $error = "Username or password is invalid";
        }
       
        //mysql_close($connection); // Closing Connection
    }
}
?><?php

//connect to server
include('db/connect.php');
include('php/isMobile.php');


session_start(); // Starting Session
$error=''; // Variable To Store Error Message

if (isset($_POST['submit'])) {
    if (empty($_POST['username']) || empty($_POST['password'])) {
        //one of the two is empty
        $error = "Username or Password is invalid";
    }
    else
    {
        // Define $username and $password variables (get from the submission)
        $username=$_POST['username'];
        $password=$_POST['password'];
       
    
        // To protect MySQL injection for Security purpose
        $username = stripslashes($username);
        $password = stripslashes($password);
        //$username = mysql_real_escape_string($username);
        //$password = mysql_real_escape_string($password);
        
        // SQL query to fetch information of registerd users and finds user match.
        $sql = "select username,level from login where password='$password' and username='$username'";
        $result = $db->query($sql);
        //$query = mysql_query("select * from login where password='$password' AND username='$username'");
        if ($result->num_rows==1){
            $row = $result -> fetch_assoc();
            $level = $row['level'];
            $_SESSION['login_user'] = $username; // Initializing Session
            $_SESSION['start'] = time();
            header("location: profile.php");
            
            //now record that login attempt
            $sql = "insert into loginHistory (username,loginTime) VALUES ('$username',NOW());";
            $reslt = $db->query($sql);
        }
        else{
            $error = "Username or password is invalid";
        }
       
        //mysql_close($connection); // Closing Connection
    }
}
?>