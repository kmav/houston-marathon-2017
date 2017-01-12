<!DOCTYPE html>
<html>
    <head>
        <title>General Info </title>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js" charset="utf-8"></script>
        <link rel='stylesheet' type='text/css' href='css/styling.css'>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
        <link rel='stylesheet' type='text/css' href='css/menu.css'>
        <script src="js/googleAnalytics.js"></script>

    </head>
    <body>
        <?php include('php/header.php'); ?>
        <?php include 'db/connect.php'; ?>
        
        <?php
        $AidStations = array();
        
        
        foreach($_POST as $var){
            echo $var;
            echo "<br><br> - ";
        }
        
        
        //get previous data to see if we should put it
        $sql = "SELECT *
                    FROM GeneralInformation
                    WHERE GeneralInformation.id = (
                    SELECT MAX( id )
                    FROM GeneralInformation ) ;";
        $result = $db->query($sql);
        
        if ($result->num_rows>0){
            //output data of each row as a variable in php
            while ($row = $result -> fetch_assoc()){
                
                if (((int)$_POST['AlertStatus'])==55){
                    $alertStatus=$row['AlertStatus'];
                }
                else{
                    $alertStatus = (int)$_POST['AlertStatus']; 
                }
                
                if (((int)$_POST['runnersOC'])==0){
                        $runnersOc = $row['RunnersOnCourse'];
                    }
                    else{
                        $runnersOc = (int)$_POST['runnersOC']; 
                }
                
                
                if (((int)$_POST['finished'])==0){
                        $finished = $row['FinishedRunners'];
                    }
                    else{
                        $finished = (int)$_POST['finished']; 
                }
                
                 if (((int)$_POST['transports'])==0)
                 {
                        $transports = $row['HospitalTransports'];
                    }
                    else{
                        $transports= (int)$_POST['transports']; 
                }
                
                
                if (((int)$_POST['pSeen'])==0){
                        $pSeen = $row['PatientsSeen'];
                    }
                    else{
                        $pSeen = (int)$_POST['pSeen']; 
                }
                
                

                //echo $_POST['alert'];
                 if (($_POST['alert'])=="0"){
                    $alert = $row['Alert'];
                }
                else{
                    $alert = $_POST['alert']; 
                }

               ////////////////////////////////////// weather
               echo "<br>";
                echo $_POST['temperature'];
                echo "<br>";
                 if (($_POST['temperature'])=="0"){
                    $temperature = $row['temperature'];
                }
                else{
                    $temperature = $_POST['temperature']; 
                }
                
                
                //echo $_POST['alert'];
                 if (($_POST['windSpeed'])=="0"){
                    $windSpeed = $row['windSpeed'];
                }
                else{
                    $windSpeed = $_POST['windSpeed']; 
                }
                
                
                //echo $_POST['alert'];
                 if (($_POST['windDirection'])=="0"){
                    $windDirection = $row['windDirection'];
                }
                else{
                    $windDirection = $_POST['windDirection']; 
                }
                
                
                //echo $_POST['alert'];
                 if (($_POST['humidity'])=="0"){
                    $humidity = $row['humidity'];
                }
                else{
                    $humidity = $_POST['humidity']; 
                }
                
                //echo $_POST['alert'];
                 if (($_POST['emergencyCheck'])){
                    $emergencyCheck = 1;
                }
                else{
                    $emergencyCheck = 0; 
                }
                
                if (($_POST['shelterDisplay'])){
                    $shelterDisplay = 1;
                }
                else{
                    $shelterDisplay = 0;
                }
                
                if (floatval($_POST['latAl'])==0){
                    $latAl = $row['AlertLat'];
                }
                else{
                    $latAl = floatval($_POST['latAl']); 
                }
                
                if (floatval($_POST['longAl'])==0){
                    $longAl = $row['AlertLong'];
                }
                else{
                    $longAl = floatval($_POST['longAl']); 
                }
                
                
            }
        }
        else {
            echo "0 results!!!";
        }
        
        //obtain sum of treatments from AidStations table
        $sql = "SELECT sum(CumulativePatients) PatientsSeen from AidStations;";
        $result = $db->query($sql);
        if ($result->num_rows>0){
            while ($row = $result -> fetch_assoc()){
                $pSeen = $row['PatientsSeen'];
            }
        }
            
        
        
        $sql = "INSERT INTO GeneralInformation (time, AlertStatus, temperature, windSpeed, windDirection, 
            humidity,RunnersOnCourse, FinishedRunners, HospitalTransports,
            PatientsSeen, Alert,emergencyCheck, AlertLat, AlertLong, shelterDisplay)
            VALUES (
                NOW(),
                ".$alertStatus.",
                ".$temperature.",
                ".$windSpeed.",
                \"".$windDirection."\",
                ".$humidity.",
                ".$runnersOc.",
                ".$finished.",
                ".$transports.",
                ".$pSeen.",
                \"".$alert."\" ,
                ".$emergencyCheck.",
                ".$latAl.",
                ".$longAl.",
                ".$shelterDisplay.");";
                
                    
        if ($db->query($sql) === TRUE) {
            echo "New record created successfully" . $sql;
        } else {
            echo "Error: why error" . $sql . "<br>" . $conn->error;
        }
        
        $db->close();
        
        $myfile = fopen("data/genInfo.csv","w") or die("Error opening file");
        
        $txt = "AlertStatus,temperature,windSpeed,windDirection,humidity,";
        $txt = $txt."runnersOnCourse,runnersFinished,hospitalTransports,patientsSeen,";
        $txt = $txt."Alert,pace350Lat,pace350Long,pace400Lat,pace400Long,pace415Lat,pace415Long,pace500Lat,pace500Long,pace530Lat,pace530Long,pace600Lat,pace600Long,emergencyCheck,AlertLat,AlertLong,shelterDisplay\n";
        
        $txt = $txt.$alertStatus.",";
        $txt = $txt.$temperature.",";
        $txt = $txt.$windSpeed.",";
        $txt = $txt."\"".$windDirection."\",";
        $txt = $txt.$humidity.",";
        $txt = $txt.$runnersOc.",";
        $txt = $txt.$finished.",";
        $txt = $txt.$transports.",";
        $txt = $txt.$pSeen.",";
        
        $txt = $txt."\"".$alert."\",";
        // $txt = $txt.$latLM.",";
        // $txt = $txt.$longLM.",";
        // $txt = $txt.$latLF.",";
        // $txt = $txt.$longLF.",";
        
        // $txt = $txt.$latLMH.",";
        // $txt = $txt.$longLMH.",";
        // $txt = $txt.$latLFH.",";
        // $txt = $txt.$longLFH.",";

        // $txt = $txt.$latLWM.",";
        // $txt = $txt.$longLWM.",";
        // $txt = $txt.$latLWF.",";
        // $txt = $txt.$longLWF.",";

        $txt = $txt.$lat350.",";
        $txt = $txt.$long350.",";
        $txt = $txt.$lat400.",";
        $txt = $txt.$long400.",";
        $txt = $txt.$lat415.",";
        $txt = $txt.$long415.",";
        $txt = $txt.$lat500.",";
        $txt = $txt.$long500.",";
        $txt = $txt.$lat530.",";
        $txt = $txt.$long530.",";
        $txt = $txt.$lat600.",";
        $txt = $txt.$long600.",";
        
        
        $txt = $txt.$emergencyCheck.",";
        $txt = $txt.$latAl.",";
        $txt = $txt.$longAl.",";
        $txt = $txt.$shelterDisplay;
        
        echo $txt;
        
        fwrite($myfile,$txt);
        fclose($myfile);

        
        ?> 
        
    <br><br><br><br>
    <a href='input_geninfo.php' >Go back to form</a>
    </body>
</html>