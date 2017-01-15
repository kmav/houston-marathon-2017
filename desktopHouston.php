<?php 
session_start(); // Starting Session
include('session.php');
include('getTreatments.php');
if ($mobile==true)
{
    //header("location: getMobile.php");
}
if ($level_session>1){
    header("location: index.php");
}
if(!isset($_SESSION['login_user'])){
    header("location: index.php");
}
//check if it's been active for 1 hour, otherwise close it
if ($_SESSION['start'] + (7*60*60) < time()) {
     header("location: php/logout.php");
  }
?>

<!DOCTYPE html>
<html>

<head>
    <script>
        // window.location = "http://marathon.iems.northwestern.edu";
    </script>
    <meta charset=utf-8 />
    <title>Chevron Houston Marathon</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js" charset="utf-8"></script>
    
    <script src='https://api.tiles.mapbox.com/mapbox.js/v2.2.1/mapbox.js'></script>
    <link href='https://api.tiles.mapbox.com/mapbox.js/v2.2.1/mapbox.css' rel='stylesheet' />
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

    <link rel="stylesheet" href="css/leaflet.awesome-markers.css">
    <script src="js/leaflet.awesome-markers.js"></script>

    <!--<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.simpleWeather/3.0.2/jquery.simpleWeather.min.js"></script> -->

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Lato">

    <link rel='stylesheet' type='text/css' href='css/desktop_style.css'>

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <script src='js/generalInfo.js' type='text/javascript'></script>
    
    <style>

    </style>

    <!--Including own scripts -->
    <script src='js/updateAll.js'></script>
</head>

<body onload="updatePage(); setInterval('updatePage()',1000)">

    <body>
        <div class="container-fluid">

            <div class="row" id='mediumRow'>
                <div class="col-sm-12 full" id='topBar'>
                    
                    <a href="profile.php">
                    <div class="col-sm-1 full">
                        <div id="marathonLogo"></div>
                    </div> </a>
                    
                    <div class="col-sm-1 full">
                        <div id="aramcoLogo"></div>
                    </div>
                    <a href="http://www.mccormick.northwestern.edu/industrial" target="_blank">
                    <div class="col-sm-2 full">
                        <div id="NUlogo"></div>
                    </div> </a>


                    <div class="col-sm-2 full"><!--Runners on course stat-->
                    </div>
                    <div class="col-sm-3 full" class='times'>
                        <div class='row'>Clock Time</div>
                        <div class='row'>
                            <span id='clock'>&nsbp</span>
                        </div>
                    </div>
                    <div class="col-sm-2 full" class='times'>
                        <div class='row'>Race Time</div>
                        <div class='row'>
                            <span id='elapsedTime'>&nsbp</span>
                        </div> 
                    </div>
                    <div class='col-sm-1 full' class='refresh'>
                        <!--<div class='row refreshButton' >-->
                        <!--    <button class='refreshButton' onclick="refreshPage()">REFRESH</button>-->
                        <!--</div>-->
                    </div>

                </div>
            </div>

            <div class="row" id='smallRow'>
                <div class="col-sm-12  full" id='alertBar'>
                    <div class='col-sm-12 full' id='alertText'></div>
                    
                </div>
            </div>

            <div class="row" id="xLargeRow">
                <div class="col-sm-7 full" id='map'>
                    <script src='js/generateMaps.js'></script>
                    <div class="row">
                        <div class='col-sm-5 full' id='infoBox'>
                            <p id='HospitalTransports'>&nbsp</p>
			                <p id='PatientsSeen'>&nbsp</p>
					        <p id='InMedical'>&nbsp</p>
                        </div>
                        <!--<div class='col-sm-2 full blank'></div>-->
                        <div class='col-sm-5 full'>
                            <div id="runners_box">
						    <p id='RunnersStarted'>&nbsp</p>
						    <p id='RunnersDropped'>&nbsp</p>
			        	    <p id='RunnersFinished'>&nbsp</p>
			        	    <p id='RunnersOnCourse'>&nbsp</p>
					        </div>
                        </div>
                    </div>
                    
                <div id="map_legend">
					<p> Runners: </p>
				<p>Opened Road <span class="boxes gray"></span></p>
			        <p>250-1000 <span class="boxes green"></span></p>
			        <p>1000-2000 <span class="boxes yellow"> </p>
			        <p>2000-3000 <span class="boxes orange"> </p>
			        <p>3000+ <span class="boxes red"> </p>
				<p> Miles <span class="circles purple"></span></p>
				<p> Aid Stations <span class="circles green"></span></p>			
				<p> AS (Closed) <span class="circles gray"></span></p>
				<p> Race Guards <span class="circles raceGuardsRed"></span></p>
				<p> GPS Pacers <span class="circles pacersBlue"></span></p>
	           </div>
	
                </div>
                <div class='col-sm-5 full' id='sidebar'>
                    <div class='col-sm-12 full'>
                    <div class="row" id="sidebarTopRow">
                        
                        <!--<div class='col-sm-1 full blank'></div>-->
                        <div class='col-sm-5 full module' id="legendBox">
                            <h5>Legend (Bed Occupancy)</h5>
			                <span class="boxes green"></span><p>&lt50%</p>
			                <span class="boxes yellow"></span><p>50-90% </p>
			                <span class="boxes red"></span><p>90% </p>
                        </div>
                        
                        <div class='col-sm-6 full module' id='weather'>
                            <script src='js/weather.js' type='text/javascript'></script>
                        </div>
                        

                        <!--end weather div-->
                    </div>
                    <!--end sidebarTopRow-->


                    <div class="row" id="sidebarGraphs">


                        
                        <div class='col-sm-5 full module' id='aidStation'>
                            <!--Here is Aid station-->
                            <script src='js/graphAidStations_Houston.js' type='text/javascript'></script>
                        </div>

                        <div class='col-sm-1'></div>
                        
                        <div class='col-sm-6 full module' id='medicalTent'>
                            <!--Here goes medical tent-->
                            <script src='js/medicalTents_Houston.js' type='text/javascript'></script>
                        </div>

                    </div>
                    
                    <div class="row module" id="densityGraphs">
                        
                            
                          <div class='col-sm-7 full' id='densityPlot'>
                             <svg id='fullChart'></svg>
                            </div>
                            
                            <div class='col-sm-5 full' id='densityPlotH'>
                                 <svg id='halfChart'></svg>
                                 
                            </div>      
                            
                            <div id="densityLegend">
        
                                <div class='col-sm-4 full'>
                                               <span class="boxes halfMarathonPurple"></span><p>Half marathon</p>
                                </div>
                                <div class='col-sm-4 full'>
                                               <span class="boxes marathonPurple"></span><p>Full marathon</p>
                                </div>
                            </div>
                            
                    </div>
                    
                    
                    </div>


                    
                    

                    
                    
                    <script src='js/densityPlot.js' type='text/javascript'></script>

                </div>
                <!--end 7 col div for sidebar-->
                </div>
            </div>
            <!--end xlarge row-->



<!-- here is the tooltip that goes on the info bars -->
<div id="tooltip" class="hidden">
    <p><span id="tooltipHeader">Aid Station</span></p>
    <p><span id="value">100</span></p>
</div>

        </div>

    </body>

</html>
