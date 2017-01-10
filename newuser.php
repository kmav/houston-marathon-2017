

<?php
//base of code from http://www.formget.com/login-form-in-php/
//modified for purposes of this project

include('register.php'); // Includes Login Script

if(isset($_SESSION['login_user']))
{
    //login was successful, redirect page to profile.php
    header("location: profile.php");
}

?>
<!DOCTYPE html>
<html>
<head>
<title>2017 Houston Marathon </title>
<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Ubuntu">

<link href="css/styled_login.css" rel="stylesheet" type="text/css">
</head>
<body>
<div id="main">
<h1>2017 Houston Marathon </h1>
<h2 style="font-weight:normal;">Data Visualization System</h2>
<div id="login">
<h2>Registration Form for New Users</h2>
<h3>If you forget the password, send an email to marathondvs@gmail.com with your username. </h3>
<h3>There are currently no restrictions on the password (length, caps, special characters, numbers, etc)</h3>
<form action="" method="post">
<label>First Name :</label>
<input id="fname" name="name" placeholder="First Name" type="text">
<br><br>
<label>Last Name :</label>
<input id="lname" name="lastname" placeholder="Last Name" type="text">
<br><br>
<label>Email :</label>
<input id="email" name="email" placeholder="email@email.com" type="email">
<br><br>
<label>Username :</label>
<input id="name" name="username" placeholder="username" type="text">
<br><br>
<label>Password :</label>
<input id="password" name="password" placeholder="password" type="password">
<br><br>
<label>Repeat Password:</label>
<input id="password2" name="password2" placeholder="password" type="password">
<br><br>
<label>Finally, tell us a little bit about where you will be during the Houston Marathon</label>
<br><br>
I will be stationed at  : <select  name="station">
  <option value="AS">Aid Stations</option>
  <option value="Finish">Finish Line</option>
  <option value='FC'>Unified Command</option>
  <option value='MT'>Medical Tents</option>
  <option value='Remote'>Remotely</option>
  <option value="Start">Start Line</option>
   <option value='other'>other</option>
</select>



<input name="submit" type="submit" value=" Register ">
<br>
<span style="font-weight:normal;"><?php echo $error; ?></span>
</form>
</div>
</div>
</body>
</html>