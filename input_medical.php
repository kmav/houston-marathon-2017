<?php 
session_start(); // Starting Session
if(!isset($_SESSION['login_user'])){
    header("location: index.php");
}

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
    <body onload="updatePage(); setInterval('updatePage()',1000)">
            <?php include('php/header.php'); ?>

 <div id='timingDiv'>
        <div id='timeTitle' style="width: 50%">Clock Time</div>
        <div id='clock' style="width: 50%", style="float: right">&nbsp</div>      
        <div id='timeTitle'>Race Time</div>
        <div id='elapsedTime'>&nbsp</div>
        </div>


        <form action='updateAid.php' class="inputform" method="post" id="inputform">
        <script type='text/javascript'>
        
        
            <?php include('db/connect.php'); 
            
            
            
            echo "var Stations = [";
            
            $sql = "SELECT * FROM AidStations;";
            $result = $db->query($sql);
            
            if ($result->num_rows>0){
                //output data of each row as a variable in php
                while ($row = $result -> fetch_assoc()){
                    echo "{ Type: '".$row['StationType']."' , 
                            TimeUpdate: '".(string)$row['timeUpdate']."',
                            Location: '".$row['Location']."',
                            Comments: '".$row['Comments']."',
                            CurrentPatients: ".$row['CurrentPatients'].",
                            CumulativePatients: ".$row['CumulativePatients'].",
                            Beds: ".$row['Beds'].",
                            Km: ".$row['Km'].",
                            Display: ".$row['Display'].",
                            Status: ".$row['Status']." }, \n";
                }
            }
            else {
                echo "0 results";
            }

            $db->close();

            echo "];"
            ?>
        </script>
        <script type='text/javascript' src='js/addAidStationButtons.js'></script>
      


<script type="text/javascript">
    
function updateClock()
{
	var currentTime = new Date();

	//make sure we're on the right timezone
	var offset = currentTime.getTimezoneOffset();
	//console.log(offset);
	var difference = offset ;

	currentTime = new Date(currentTime.getTime());// - difference*60000);

	//now get the actual time at Chicago
	var currentHours = currentTime.getHours();
	var currentMinutes = currentTime.getMinutes();
	var currentSeconds = currentTime.getSeconds();

	//pad the minutes and seconds with leading zeros if needed
	currentMinutes = (currentMinutes < 10 ? "0" : "")+currentMinutes;
	currentSeconds = (currentSeconds < 10 ? "0" : "")+currentSeconds;

	//choose AM or PM
	var timeOfDay = (currentHours < 12) ? "AM" : "PM";

	//convert hours to 12 hour format
	var currentHours = (currentHours > 12) ? currentHours - 12 : currentHours;

	//convert hours of 0 to 12
	if (currentHours ==0){
		currentHours = 12;
	}

	//get the string
	var currentTimeString = currentHours + ":" + currentMinutes + " "+ timeOfDay;
	//display the string
	document.getElementById('clock').firstChild.nodeValue = currentTimeString;


	//now get the elapsed time since event started

	var nowMs = currentTime.getTime();

	var startTime = new Date();
	startTime.setHours(7);
	startTime.setMinutes(30);
	startTime.setSeconds(0);
	startTime.setMilliseconds(0);

	var startMs = startTime.getTime();
    var timeMultiplier = 1;
	//now calculate the millisecond difference from one to other
	var elapsedMs = (nowMs - startMs)*timeMultiplier;
	//3600 seconds in an hour
	var elapsedHours = parseInt(elapsedMs / (3600*1000));
	elapsedHours = (elapsedHours < 10? "0":"")+elapsedHours;
	var elapsedMinutes = parseInt((elapsedMs % (3600*1000))/60000);
	elapsedMinutes = (elapsedMinutes < 10 ? "0": "")+elapsedMinutes;
	var elapsedSeconds = parseInt((elapsedMs % 60000)/1000);
	elapsedSeconds = (elapsedSeconds < 10 ? "0":"")+elapsedSeconds;

	var elapsedTimeString = elapsedHours + ":"+ elapsedMinutes+":"+elapsedSeconds;
	document.getElementById('elapsedTime').firstChild.nodeValue = elapsedTimeString;
	console.log(elapsedTimeString)
}

////////////////////////////MAIN UPDATE OF THE PAGE
function updatePage(){
	updateClock();
}
</script>

    </form>
    </body>
</html>