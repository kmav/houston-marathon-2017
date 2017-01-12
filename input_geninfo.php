<?php
//Checks if you're logged in, if not sends you to index.php
session_start(); // Starting Session
//if(!isset($_SESSION['login_user'])){
//    header("location: index.php");
?>

<!DOCTYPE html>
<html>
<meta charset="utf-8"/>
<head>
    <title>Input General Info </title>
    <style>
        .inputBox {
            text-align: center;
            width: 100%;
            height: 30px;
            margin: auto;
            border-radius: 10px;
            background: linear-gradient(rgb(135,206,235),rgb(173,216,230), white);
            
        }
        .wrapper {
            position: relative;
            width: 100%;
            height: 100%;
            margin: auto;
            float: left;
        }
        
        .genInfoBox {
            border: 2px; 
            text-align: center;
            width: 200px;
            height: 50px;
            padding: 10px;
            background: linear-gradient(rgb(135,206,235),rgb(173,216,230), white);
            border-radius: 10px;
            float: left;
            margin: 10px;
        }
        
        .trackingBox {
            border: 2px ;
            text-align: center;
            width: 200px;
            height: 130px;
            padding: 10px;
            background: linear-gradient(rgb(135,206,235),rgb(173,216,230), white);
            border-radius: 10px;
            float: left;
            margin: 10px;
        }
        
        .AlertBox {
            border: 2px;
            text-align: center;
            width: 600px;
            height: 50px;
            padding: 10px;
            background: linear-gradient(rgb(135,206,235),rgb(173,216,230), white);
            border-radius: 10px;
            float: left;
            margin: 10px;
        }
        
        .emergBox {
            border: 2px;
            text-align: center;
            width: 200px;
            height: 150px;
            padding: 10px;
            background: linear-gradient(rgb(249,100,100),rgb(249,100,100), white);
            border-radius: 10px;
            float: left;
            margin: 10px;
        }
        
        .Titles {
            font-size: 120%;
  	        font-family: "Helvetica Neue", Geneva, sans-serif;
        }
        
        .Labels {
            font-size: 100%;
  	        font-family: "Helvetica Neue", Geneva, sans-serif;
        }
        .submitButton{
            width: 300px;
            height: 60px;
            font-size: 1.5em;
        }
        
        
    </style>
    <script src="js/googleAnalytics.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js" charset="utf-8"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
        <link rel='stylesheet' type='text/css' href='css/menu.css'>

</head>

<body>
    <?php include('php/header.php'); ?>
    
    <form action="updateGenInfo.php" method="POST" id='inputForm'>
        
        
        <div class="wrapper">
            
            
        <div class='genInfoBox' id='AlertBox'>
            <div class="Titles" >Alert Status</div>
            <select id="AlertStatus" name='AlertStatus' onchange="myFunction()" form='inputForm'>
              <option name='AlertStatus' value=55>No Change
              <option name='AlertStatus' value=0>Green
              <option name='AlertStatus' value=1>Yellow
              <option name='AlertStatus' value=2>Red
              <option name='AlertStatus' value=3>BLACK (be careful)
            </select>
        </div>    
    
        <script type='text/javascript'>
            
            function myFunction(){
                alert("Are you sure?");
            }
            
            
        </script>
        
        <div class="genInfoBox">
        <div class="Titles">Temperature</div>
        <input type="number" name="temperature" value=0> &deg F
        </div>
        
        <div class="genInfoBox">
        <div class="Titles">Wind Speed</div>
        <input type="number" name="windSpeed" value=0> mph
        </div>
        
        <div class="genInfoBox">
        <div class="Titles">Wind Direction</div>
        <select name="windDirection">
        <option value="0">0</option>
        <option value="N">N</option>
        <option value="E">E</option>
        <option value="S">S</option>
        <option value="W">W</option>
        <option value="SW">SW</option>
        <option value="SE">SE</option>
        <option value="NW">NW</option>
        <option value="NE">NE</option>
        </select>
       
        </div>
        
        <div class="genInfoBox">
        <div class="Titles">Humidity</div>
        <input type="number" name="humidity" value=0>
        </div>
        
        </div>
        
        <div class="wrapper">
            
            <div class="genInfoBox">
            <div class="Titles"># Runners On Course</div>
            <input type="number" name="runnersOC" value=0>
            </div>
            
    
            
            <div class="genInfoBox">
            <div class="Titles"># Finished Runners</div>
            <input type="number" name="finished" value=0>
            </div>
            
    
            
            <div class="genInfoBox">
            <div class="Titles"># Hospital Transports</div>
            <input type="number" name="transports" value=0>
            </div>
            
    
            
            <div class="genInfoBox">
            <div class="Titles"># Patients Seen</div>
            <input type="number" name="pSeen" value=0>
            </div>
            
    
        
        </div>
        
      
        
        <div class="wrapper">
            
            <div class="AlertBox">
            <div class="Titles">Alerts</div>
            <input id='alert_saved' type="text" name="alert" size=70 value=0>
            </div>
            
            <div class="emergBox">
            <div class="Titles"> Emergency Alerts</div>
            <input type="checkbox" id="emerg" name="emergencyCheck">Check if an emergency.
            <div class="Labels">Lat:</div>
            <input type="text" name="latAl" id="latAl" value=0>
            <div class="Labels">Long:</div>
            <input type="text" name="longAl" id="lonAl" value=0>
            </div>
        </div>
        
        <div class='wrapper'>
            
            <div class='emergBox' style='height:auto;'>
                <div class='Titles'>Shelter Display</div>
                    <input type='checkbox' id='shelterDisplay' name='shelterDisplay'>Display ALL shelters.
                    <br>
                    <input type='checkbox' id='shelters0' name='shelters0'>Display Section 0
                    <br>
                    <input type='checkbox' id='shelters1' name='shelters1'>Display Section 1
                    <br>
                    <input type='checkbox' id='shelters2' name='shelters2'>Display Section 2
                    <br>
                    <input type='checkbox' id='shelters3' name='shelters3'>Display Section 3
                    <br>
                    <input type='checkbox' id='shelters4' name='shelters4'>Display Section 4
                    <br>
                    <input type='checkbox' id='shelters4h' name='shelters4h'>Display Section 4H
                    <br>
                    <input type='checkbox' id='shelters5' name='shelters5'>Display Section 5
                    <br>
                    <input type='checkbox' id='shelters6' name='shelters6'>Display Section 6
            </div>
        </div>
   
        <input type="submit" class='submitButton' value="Submit Data">
        
    </form>
    
    <script type="text/javascript">//getting default alert values
    function getAlerts(data)
    {
         var check = +data[0].emergencyCheck; 
         var AlertLat = data[0].AlertLat; 
         var AlertLong = data[0].AlertLong;
         var shelterDisplay = data[0].shelterDisplay;
        var message=data[0].Alert;
        //(message+"alert");
        document.getElementById('alert_saved').value=message;
        //get the true/false of the check for the emergency
        if (check==1){
            $("#emerg").prop('checked',true);
        }
        else{
            //set checked=false
            $("#emerg").prop('checked',false); 
        }
        if (shelterDisplay==1)
        {
            $("#shelterDisplay").prop('checked',true);
        }
        else{
            $("#shelterDisplay").prop('checked',false);
        }
        
        //now put lat/long values in the fields
        document.getElementById("latAl").value = AlertLat;
        document.getElementById("lonAl").value = AlertLong;
        

        
    }
    d3.csv('data/genInfo.csv',getAlerts);    
    </script>
    
</body>

</html>