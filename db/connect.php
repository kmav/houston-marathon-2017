
<?php
    // A simple PHP script demonstrating how to connect to MySQL.
    // Press the 'Run' button on the top to start the web server,

    date_default_timezone_set("America/Chicago");
    $today = date("Y-m-d",time());
    $raceStart = strtotime("$today 07:30:01");
    
    $servername = getenv('IP');
    $username = getenv('C9_USER');
    $password = "";
    $database = "houston2016";
    $dbport = 3306;

    $serverName = $_SERVER['SERVER_NAME'];
    if (strcmp($serverName,'marathon.iems.northwestern.edu')==0){
        include('/home/numarathon/marathon2015/Chicago2015/connectHere.php');
    }
    
    else {
          // Create connection
        $db = new mysqli($servername, $username, $password, $database, $dbport);
    
        // Check connection
        if ($db->connect_error) {
            die("Connection failed: " . $db->connect_error);
        } 
        //echo "Connected successfully (".$db->host_info.")";  
    }

    ?>
