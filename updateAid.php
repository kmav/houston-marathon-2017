<?php 
//include('php/isMobile.php');

?>
<!DOCTYPE html>
<html>
    <head>
        <title>Input Medical </title>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js" charset="utf-8"></script>
        <script src="js/googleAnalytics.js"></script>

        <link rel='stylesheet' type='text/css' href='css/styling.css'>
             <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
        <link rel='stylesheet' type='text/css' href='css/menu.css'>
    </head>
    <body>
        <?php include('php/header.php'); ?>
            <a href='input_medical.php' >Go back to form</a>
<br><br>
        <?php include 'db/connect.php'; ?>
        
        <?php
        
        // printing the input names and values (from input_medical.php)
        foreach ($_POST as $key => $value)
            echo "Field ".htmlspecialchars($key)." is ".htmlspecialchars($value)."<br>";
        
        //initialize an array 
        $AidStations = array();

        // get the previous values and make an array of arrays of the previous values (same as dictionary in python so you can use key or index)
        $sql = "SELECT * FROM AidStations";
        $result = $db->query($sql);
        
        if ($result->num_rows>0){
            //output data of each row as a variable in php
            while ($row = $result -> fetch_assoc()){
                
                $tempArray = array(
                    "Key"=>$row['id'],
                    "Type"=>$row['StationType'],
                    "TimeUpdate"=>((string)$row['timeUpdate']),
                    "Location"=>$row['Location'],
                    "Comments"=>$row['Comments'],
                    "CurrentPatients"=>$row['CurrentPatients'],
                    "CumulativePatients"=>$row['CumulativePatients'],
                    "Beds"=>$row['Beds'],
                    "Lat"=>$row['Latitude'],
                    "Long"=>$row['Longitude'],
                    "Km"=>$row['Km'],
                    "Status"=>$row['Status'],
                    "Display"=>$row['Display']
                    );
                //echo $tempArray["Location"];
                //echo "<br>";
                // append the arary to array of arrays
                array_push($AidStations,$tempArray);
            }
        }
        else {
            echo "0 results";
        }


        //get the values passed to me from the form input_medical.php
        $counter = 1;
        foreach($AidStations as &$station){
            //now check and/or change as needed
            if ($station["Type"]=="AS"){
                $station["CurrentPatients"] = (int)$_POST["AS_Current".$station["Location"]];
                
                $station["CumulativePatients"] = (int)$_POST["AS_Cumulative".$station["Location"]];
                //add status updates!!! (from buttons or something like that)
                $str = "AS_status".$station["Location"];
                $station["Status"] = (int)$_POST[$str];
                $str = "AS_Display".$station["Location"];      
                //echo "<br>";
                //echo $str;
                $station["Display"] = $_POST[$str];
                if ($station["Display"]==true){
                    $station["Display"]=1;
                }
                else{
                    $station["Display"]=0;
                }
                //shows keys and values
                echo $station;
                //echo $station["Display"];
                //echo "<br>";
            }
            else{
                //do the same for medical tents
                $str = "MT_Current".$station["Location"];
                $station["CurrentPatients"] = (int)$_POST[$str];
                $str = "MT_Cumulative".$station["Location"];
                $station["CumulativePatients"] =  (int)$_POST[$str];
            
                //add status updates!!! (from buttons or something like that)
                $str = "MT_status".$Location;
                $station["Status"] = (int)$_POST[$str];
                $str = "MT_Display".$Location;
                $station["Status"] = (int)$_POST[$str];
            }
            
            //and update in the database
            //UPDATE table_name
            //SET column1=value, column2=value2,...
            //  WHERE some_column=some_value 
            // $sql = "INSERT INTO AidStations 
                // (timeUpdate,CurrentPatients,CumulativePatients,Status,Display,
                // StationType,Location,Comments,Beds,Latitude,
                // Longitude,Km) SELECT NOW(),".$station['CurrentPatients'].",".$station['CumulativePatients'].",".$station['Status'].",".$station['Display']."
                // ,StationType,Location,Comments,Beds,Latitude,Longitude,Km from AidStations where Location='".$station['Location']."' order by timeUpdate LIMIT 1;";
            $sql = "UPDATE AidStations
                SET CurrentPatients=" . $station["CurrentPatients"] .", CumulativePatients=". $station["CumulativePatients"] .", Status=".$station["Status"].",Display=".$station["Display"]."
                WHERE Location='". $station["Location"] ."';";
            echo $sql;
            echo $station["Location"];
            echo "<br>";
            //how to execute the query, true means no errors (form will say "New recorded created" if successful)
            if ($db->query($sql) === TRUE) {
                echo "Record ".$station["id"] ."updated successfully";
            } else {
                echo "Error updating record: ".$station["id"]." -- ERROR: ". $db->error;
            }


            $sql = "INSERT into AidStationHistory (AS_id,timeupdate,currentPatients,cumulativePatients,beds,status,display) 
            VALUES ('".$station["Location"]."',NOW(),".$station["CurrentPatients"].",".$station["CumulativePatients"].",".$station["Beds"].",".$station["Status"].",".$station["Display"].")";
            echo "<br><br>".$sql;
            if ($db->query($sql) === TRUE) {
                echo "Record ".$station["id"] ."saved successfully";
            } else {
                echo "Error saving record: ".$station["Location"]." -- ERROR: ". $db->error;
            }
            echo "<br>!!//////<br>";
            
            $counter++;
        }

        //now write to file
        
        
        /* format: 
        $myfile = fopen("newfile.txt", "w") or die("Unable to open file!");
        $txt = "John Doe\n";
        fwrite($myfile, $txt);
        $txt = "Jane Doe\n";
        fwrite($myfile, $txt);
        fclose($myfile);
        */
        $myfile = fopen("data/AidStations.csv","w") or die("unable to open file!");
        $txt = "Type,Location,Comments,CurrentPatients,CumulativePatients,Beds,Latitude,Longitude,Km,Status,Display\n";
        fwrite($myfile,$txt);
        $counter=1;
        foreach($AidStations as $station){
            //ERROR -> for some reason, the last key and location gets changed back to 19 instead of 20
            //fixed it with a counter, but should check on this!
            //echo $station["Key"];
            //echo $counter;
            //write a new line
            if ($counter<21){
                 $txt = $station["Type"].",";
                if ($counter==19){
                   $txt = $txt ."Minor,";
                }
                else {
                    $txt = $txt .$station["Location"].",";
                }
                //appending to the file (each loop iteration is one row in the file)
                $txt = $txt .$station["Comments"].",";
                $txt = $txt .$station["CurrentPatients"].",";
                $txt = $txt .$station["CumulativePatients"].",";
                $txt = $txt .$station["Beds"].",";
                $txt = $txt .$station["Lat"].",";
                $txt = $txt .$station["Long"].",";
                $txt = $txt .$station["Km"].",";
                $txt = $txt .$station["Status"].",";
                $txt = $txt .$station["Display"];
                $txt = $txt ."\n";
                echo $txt."<br>";
                fwrite($myfile,$txt);
                $counter++;   
            }
        }
        fclose($myfile);
        
   
       ?>
        
        
    <br><br><br><br>
    </body>
</html>


<!--to avoid writing a csv file every time  you update-->
<!--d3.csv(getAidStations.php, function)).....-->
<!--getAidStations.php:  -->
<!--    SELECT * from AidStations -->
        
<!--        goes through all the rows -->
<!--        prints it with commas -->
        
    