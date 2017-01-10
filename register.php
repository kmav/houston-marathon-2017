<?php

//connect to server
include('db/connect.php');

$error=''; // Variable To Store Error Message
if (isset($_POST['submit'])) {
    if (empty($_POST['name']) || empty($_POST['lastname'] || empty($_POST['email']))) {
        //one of the two is empty
        $error = "Please input a first and last name, and an email";
    }
    else {
        if (empty($_POST['username']) || empty($_POST['password'])) {
        //one of the two is empty
        $error = "Username or Password is invalid";
        }
        else
        {
            // Define $username and $password variables (get from the submission)
            $username=$_POST['username'];
            $password=$_POST['password'];
            $name = $_POST['name'];
            $lastname = $_POST['lastname'];
            $password1 = $_POST['password2'];
            $email = $_POST['email'];
            $station = $_POST['station'];
            if (strcmp ( $password , $password1 ) ==0)
            {
           
        
                // To protect MySQL injection for Security purpose
                $username = stripslashes($username);
                $password = stripslashes($password);
                $name = stripslashes($name);
                $lastname = stripslashes($lastname);
                $email = stripslashes($email);
                $station = stripslashes($station);
                //$username = mysql_real_escape_string($username);
                //$password = mysql_real_escape_string($password);
                
                // SQL query to fetch information of registerd users and finds user match.
                $sql = "select username from login where username='$username'";
                $result = $db->query($sql);
                //$query = mysql_query("select * from login where password='$password' AND username='$username'");
                if ($result->num_rows==0){
                    $sql = "insert into login (username,password,createUser,level,name,lastname,email,station) VALUES ('$username','$password',NOW(),1,'$name','$lastname','$email','$station');";
                    $result = $db->query($sql);
                    
                    header('Location: login.php');
                    
                    session_start();// Starting Session
                    $_SESSION['login_user']=$username;
                    $_SESSION['firstTime'] = true;
                    
                    $sql = "select username from login where username='$username'";
                    $result = $db->query($sql);
                    if ($result->num_rows==1){
                        $error = "</span><h2 style='color:#009933; font-weight:bold;'>User $username created.</h4>
                                        <br> 
                                        <a href='users.php'><div class='pagelink'> Back to login page </div></a>
                                        <span> ";
                    }
                }
                else{
                    $error = "User already exists";
                }
            }
            else {
                $error = "Error, please try again";
            }
       
        }
    }
    
}
// mysql_close($db); // Closing Connection

?>