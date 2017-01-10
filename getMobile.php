
<!DOCTYPE html>
<html>
<head>
<title></title>
<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Ubuntu">
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
<link href="css/styled_mobile.css" rel="stylesheet" type="text/css">
<script src="js/googleAnalytics.js"></script>

</head>

<body onload="updatePage(); setInterval('updatePage()',1000)">
<?php
    include('db/connect.php');
    include('session.php');
?>

 <ul class='menuHolder nav nav-pills'>
     <li class='actives'><a class='link' href='profile.php'>Home</a></li>
 </ul>


<h1>Bank of America Chicago Marathon 2015</h1>
<h2>Data Visualization System - Mobile Version</h2>

    <div id='timingDiv'>
        <div id='timeTitle'>Clock Time</div>
        <div id='clock'>&nbsp</div>        
        <div id='timeTitle'>Race Time</div>
        <div id='elapsedTime'>&nbsp</div>
        <?php $sql = "select Alert,emergencyCheck from GeneralInformation WHERE GeneralInformation.id = (SELECT MAX( id ) FROM GeneralInformation ) ;";
           $result = $db->query($sql);
            if ($result->num_rows>=1){
                $row = $result -> fetch_assoc();
                $alert =$row['Alert'];
                $emergencyCheck = $row['emergencyCheck'];
                if ($emergencyCheck==1){
                    $color='red';
                }
                else{
                    $color='black';
                }
            }
            echo "<div id='alertMessage' style='color:$color;'> Alerts and Messages: $alert </div>"; ?>
    </div>

<h1 style='font-weight: bold;'>What Aid Station are you in? </h1>
<form action="" method="post">
<select class='inAS' type='number' name="AS" id="AS">
    <option value=0>All</option>
    <option value=1>1</option>
    <option value=2>2</option>
    <option value=3>3</option>
    <option value=4>4</option>
    <option value=5>5</option>
    <option value=6>6</option>
    <option value=7>7</option>
    <option value=8>8</option>
    <option value=9>9</option>
    <option value=10>10</option>
    <option value=11>11</option>
    <option value=12>12</option>
    <option value=13>13</option>
    <option value=14>14</option>
    <option value=15>15</option>
    <option value=16>16</option>
    <option value=17>17</option>
    <option value=18>18</option>
    <option value=19>19</option>
    <option value=20>20</option>
</select>
<input class='submitButton' type='submit' name='submit' value='submit'>
</form>


<div class='tstamp'>
    <h2 style='font-weight: bold;'>Data updated as of: <div style='display: inline;' id='tnow'>&nbsp</div></h2>
</div>

<script>
var timeMultiplier=2;
    //get time now
    function checkTime(i) {
        if (i < 10) {
            i = "0" + i;
        }
        return i;
    }
    function startTime() {

    	currentTime = new Date();// - difference*60000);
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
    	document.getElementById('tnow').firstChild.nodeValue = currentTimeString;
    }
    startTime();
</script>

<div class="container-fluid">
    <table class="table table-striped">
        <thead>
            <tr>
                <!--   table titles -->
                <th>Aid Station</th>
                <th>Runners behind </th>
                <th>Runners ahead</th>
            </tr>
        </thead>
        <tbody>
            

<?php
//connect to server
if (isset($_POST['submit'])) {
    
    include('db/connect.php');

    //echo $_POST['AS'];
    //get minute of the race right now
    $now = time();
    $minute = round(abs($now-$raceStart)/60,0);
    $minute = $minute + ($minute%2);
    //to make sure always correct, get modulus
    $minute = $minute%500;

    
    
    $error=''; // Variable To Store Error Message

    $ASKm = array();
    $ASStatus = array();

    if($_POST['AS']==0) //display all info
    {
       $sql = "select Km, Status, Location from AidStations where StationType='AS'";
    }
    
    else //display 3 stations before and 1 after
    {
    $sql = "select Km, Status, Location from AidStations where StationType='AS' and id<=".(1+$_POST['AS'])." order by Km DESC limit 5";
    }
    
    $result = $db->query($sql);
    if ($result->num_rows>0){
        $i=0;
        while ($row = $result -> fetch_assoc()){
                    $ASKm[$row['Location']] = $row['Km'];
                    $ASStatus[$i] = $row['Status'];
                    $i++;
                }
    }

    //now, we need to get the actual data for how many have passed and how many have yet to pass
    $i=0;
    $before = array();
    $after = array();

    foreach($ASKm as $key => $value){
        //get people before and after
        if ($key==$_POST['AS']){
            echo "<tr class='yours'>";
        }
        else {
            echo "<tr>";
        }
        $sql = "select count(*)*40 ct, (position<$value) behind from MarathonRunners where minute=$minute group by behind order by behind desc;";
        // echo $sql.'<br>';
        echo "<td>".($key)."</td>";
        $result = $db->query($sql);
        if ($result->num_rows>1){
            while($row = $result->fetch_assoc()){
                if ($row['ct']<120){
                    echo "<td>0</td>";
                }
                else {
                    echo "<td>".$row['ct']."</td>";
                }
            }
        }
        else{
            //one or more of the aid stations have a number 0 in the return
            if ($result->num_rows==1){
                //only one aid station has positive numbers, other does not appear
                $row = $result->fetch_assoc();
                //check if it's behind or after
                if ($row['behind']==1){
                    //behind, so print first what we have, then 0
                    echo "<td>".$row['ct']."</td><td>0</td>";
                }
            else{
                //print 0 first then what we have
                echo "<td>0</td><td>".$row['ct']."</td>";
                
            }
        }
    }
    //any other commands to put stuff on the table can go here
    
    
    
    
    
    //end table row
    echo "</tr>";
    //get after
     //$sql = "select count(*)*40 ct from MarathonRunners where (position>=$value) AND minute=$minute;";
     //echo $sql.'<br>';
    // $result = $db->query($sql);
    // if ($result->num_rows>0){
    //     $row = $result->fetch_assoc();
    //     $after[$key] = $row['ct'];
    //     echo "<td>".$row['ct']."</td>";
    // }

}



// mysql_close($db); // Closing Connection
}
?>

        </tbody>
    </table>
</div>


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

	//now calculate the millisecond difference from one to other
	var elapsedMs = ( nowMs - startMs)*timeMultiplier;
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

</body>
</html>