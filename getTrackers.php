<!DOCTYPE html>
<html>
    <head>
        <title>Obtaining Tracker Data </title>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js" charset="utf-8"></script>
        <script src="js/googleAnalytics.js"></script>

        <link rel='stylesheet' type='text/css' href='css/styling.css'>
    </head>
    <script>
    var PageRefresh = 0;
    function updatePage(){
    	PageRefresh++;
        if (PageRefresh==10){
	        window.location.reload(1);
    	    PageRefresh=0;
        }
    };
    
    </script>
    <body onload="updatePage(); setInterval('updatePage()',1000)">        <?php include 'db/connect.php'; ?>
        
        <?php
        
        //define basic scraping function -- from http://www.jacobward.co.uk/working-with-the-scraped-data-part-2/
        function scrape_between($data, $start, $end){
            echo "scraping <br>";
            $data = stristr($data, $start); // Stripping all data from before $start
            $data = substr($data, strlen($start));  // Stripping $start
            $stop = stripos($data, $end);   // Getting the position of the $end of the data to scrape
            $data = substr($data, 0, $stop);    // Stripping all data from after and including the $end of the data to scrape
            return $data;   // Returning the scraped data from the function
        
        }
        // Defining the basic cURL function
        function curl($url) {
            echo "curl <br>";
            // Assigning cURL options to an array
            $options = Array(
                CURLOPT_RETURNTRANSFER => TRUE,  // Setting cURL's option to return the webpage data
                CURLOPT_FOLLOWLOCATION => TRUE,  // Setting cURL to follow 'location' HTTP headers
                CURLOPT_AUTOREFERER => TRUE, // Automatically set the referer where following 'location' HTTP headers
                CURLOPT_CONNECTTIMEOUT => 120,   // Setting the amount of time (in seconds) before the request times out
                CURLOPT_TIMEOUT => 120,  // Setting the maximum amount of time for cURL to execute queries
                CURLOPT_MAXREDIRS => 10, // Setting the maximum number of redirections to follow
                CURLOPT_USERAGENT => "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1a2pre) Gecko/2008073000 Shredder/3.0a2pre ThunderBrowse/3.2.1.8",  // Setting the useragent
                CURLOPT_URL => $url, // Setting cURL's URL option with the $url variable passed into the function
            );
             
            $ch = curl_init();  // Initialising cURL 
            curl_setopt_array($ch, $options);   // Setting cURL's options using the previously assigned array data in $options
            $data = curl_exec($ch); // Executing the cURL request and assigning the returned data to the $data variable
            curl_close($ch);    // Closing cURL 
            return $data;   // Returning the data from the function 
        }
        
        // ---------
        $scraped_page = curl("https://gateway.landairsea.com/tmmgw/tmmgw.asmx/Poll?cmd={%22usr%22:%22cemevent%22,%22pwd%22:%22raceday%22}");    // Downloading IMDB home page to variable $scraped_page
        echo $scraped_page;
        $start = '<string xmlns="http://www.landairsea.com/webservices/">';
        $end = '</string>';
        $scraped_data = scrape_between($scraped_page, $start,$end);   // Scraping downloaded dara in $scraped_page for content between <title> and </title> tags
    

        $jsonData = json_decode($scraped_data,true);
        
        $devices = $jsonData["devices"];
        
        foreach ($devices as $key => $value){
            $id = $value["id"];
            $name = $value["name"];
            $tsamp = $value["tstamp"];
            $lat = $value["lat"];
            $lon = $value["lon"];
            
            echo "<p>$key | $id | $name | $tsamp | $lat | $lon</p>";
        }
        
        
        /* information on trackers 
                0 | 8880320504 | AID-BR | 8/30/2015 12:39:31 AM | 41.870663 | -87.620172
                1 | 8880320506 | SPARE 1 | 8/30/2015 6:03:30 PM | 41.873138 | -87.619432
    leadMale        2 | 8880320508 | z508 | 8/30/2015 4:48:37 PM | 41.868593 | -87.620655
    leadFemale      3 | 8880320519 | z519 | 8/30/2015 5:07:18 PM | 41.864902 | -87.618926
    leadWheelMale   4 | 8880320522 | z522 | 9/3/2015 8:19:07 PM | 41.892037 | -87.621194
    leadWheelFemale 5 | 8880320528 | z528 | 9/1/2015 7:28:21 PM | 41.604179 | -87.609562
    FinalWheelchair 6 | 8880320535 | z535 | 5/3/2015 6:28:28 PM | 40.457876 | -79.971891
    Turle           7 | 8880320537 | z537 | 5/3/2015 6:10:20 PM | 40.457773 | -79.972241
        
    PacerWave1_3h   8 | 8880320538 | z538 | 5/3/2015 6:09:55 PM | 40.458117 | -79.971961
    PacerWave1_4h   9 | 8880320542 | z542 | 5/3/2015 6:41:28 PM | 40.457843 | -79.971957
    PacerWave1_5h   10 | 8880320544 | z544 | 5/3/2015 7:12:14 PM | 40.457901 | -79.971945
    PacerWave2_3h   11 | 8880320548 | z548 | 5/3/2015 6:36:34 PM | 40.43909 | -80.005181
    PacerWave2_4h   12 | 8880320549 | z549 | 5/4/2015 8:04:43 PM | 41.755963 | -85.167812
    PacerWave2_5h   13 | 8880320552 | z552 | 5/4/2015 6:58:06 PM | 41.592458 | -84.028299
    PacerWave2_6h   14 | 8880320571 | z571 | 5/4/2015 7:28:39 PM | 41.617728 | -84.664083
        15 | 8880320573 | z573 | 5/4/2015 7:10:06 PM | 41.590655 | -84.282947
        16 | 8880320574 | z574 | 5/3/2015 12:18:07 PM | 40.439017 | -79.998829
        17 | 8880320575 | z575 | 5/3/2015 1:09:44 PM | 40.461161 | -79.948258
        18 | 8880320580 | z580 | 5/4/2015 9:25:46 PM | 41.608745 | -86.851618
        19 | 8880320581 | z581 | 5/2/2015 12:57:30 PM | 40.439209 | -80.005757
        20 | 8880321015 | z015 | 8/30/2015 6:38:16 PM | 41.870638 | -87.620223
                21 | 8880321016 | EMS 1 | 8/30/2015 6:36:36 PM | 41.869698 | -87.620562
                22 | 8880321017 | EMS 2 | 8/30/2015 6:38:18 PM | 41.870646 | -87.620211
                23 | 8880321018 | BM-RXS | 9/2/2015 12:16:37 PM | 41.626705 | -87.682367
                24 | 8880321019 | BM-AK | 9/2/2015 12:21:26 PM | 41.626622 | -87.682213
                25 | 8880321218 | LB-AC | 6/15/2015 5:07:56 PM | 41.852518 | -87.653749
                26 | 8880321219 | LB-AK | 8/30/2015 5:08:22 PM | 41.873154 | -87.619301
                27 | 8880321220 | LB-LS | 8/30/2015 6:38:21 PM | 41.870662 | -87.620251
                28 | 8880321221 | LB-DC | 8/30/2015 6:38:20 PM | 41.870634 | -87.620239
                29 | 8880323596 | z596 | 5/3/2015 3:43:30 PM | 40.436398 | -80.000195
                30 | 8880420994 | z994 | 5/5/2015 7:16:28 PM | 41.852547 | -87.653859
                31 | 8880420995 | z995 | 5/3/2015 10:31:10 PM | 40.439936 | -80.008004
                32 | 8880420996 | z996 | 5/5/2015 3:20:42 PM | 41.860418 | -87.667539
                33 | 8880420997 | z997 | 5/5/2015 4:25:54 PM | 41.86712 | -87.64964
                34 | 8880420998 | z998 | 5/12/2015 9:36:01 PM | 41.860343 | -87.667658
        */
        
        //ID FOR TRACKERS
        $leadF = 8880320574;
        $leadM = 8880320575;
        $turtle = 8880323596;
        $leadFH = 8880320580;
        $leadMH = 8880320581;
        $leadWM = 8880420993;
        $pace350 = 8880120781;
        $pace400 = 8880120782;
        $pace415 = 8880120783;
        $pace430 = 8880120784
        $pace500 = 8880120785;
        $pace515 = 8880120786;
        $pace530 = 8880420998;
        $pace600 = 8880420999;
        
        //turtle
        $leadWF = 8880328566;

        // now we need to get the last from general information database
        // and get the stuff that we need
        // and just fill in the extra stuff that we don't need
        
        $sql = "SELECT *
            FROM GeneralInformation
            WHERE GeneralInformation.id = (
            SELECT MAX( id )
            FROM GeneralInformation ) ;";
            
        $result = $db->query($sql);
        if ($result->num_rows>0){
            //output data of each row as a variable in php
            while ($row = $result -> fetch_assoc()){
                var_dump($row);
                
                $alertStatus=$row['AlertStatus'];
                $runnersOc = $row['RunnersOnCourse'];
                $finished = $row['FinishedRunners'];
                $transports = $row['HospitalTransports'];
                $pSeen = $row['PatientsSeen'];
                
                $temperature = $row["temperature"];
                $windDirection = $row["windDirection"];
                $humidity = $row["humidity"];
                $windSpeed = $row["windSpeed"];
                
                $alert = $row["Alert"];
                $emergencyCheck = $row['emergencyCheck'];
            
                $latAl = $row['AlertLat'];
                $longAl = $row['AlertLong'];
                
                $shelter = $row['shelterDisplay'];
                
                echo "<br> Pace 6 hours: $pace600 <br> ";
                foreach ($devices as $key => $value){
                    $id = $value["id"];
                    $name = $value["name"];
                    $tsamp = $value["tstamp"];
                    $lat = $value["lat"];
                    $lon = $value["lon"];
                    echo "<br> Putting id: $id ";
                    switch ($id) {
                        case $leadF:
                            $latLF = $lat;
                            $longLF = $lon;
                            break;
                        case $leadM:
                            $latLM = $lat;
                            $longLM = $lon;
                            break;
                        case $turtle:
                            $latTurtle = $lat;
                            $longTurtle = $lon;
                            break;
                        case $leadWM:
                            $latLWM = $lat;
                            $longLWM = $lon;
                            break;
                        case $leadWF:
                            echo " - Wheelchair woman ";
                            $latLWF = $lat;
                            $longLWF = $lon;
                            break;
                        case $leadFH:
                            echo "$leadFH - Female half: $lat , $lon";
                            $latLFH = $lat;
                            $longLFH = $lon;
                            break;
                        case $leadMH:
                            $latLMH = $lat;
                            $longLMH = $lon;
                            break;
                        case $pace350:
                            $lat350 = $lat;
                            $long350 = $lon;
                            break;
                        case $pace400:
                            $lat400= $lat;
                            $long400 = $lon;
                            break;
                        case $pace415:
                            $lat415= $lat;
                            $long415 = $lon;
                            echo " - Pace 415 hours $lat415 $long415";
                            break;
                        case $pace430:
                            $lat430= $lat;
                            $long430 = $lon;
                            break;
                        case $pace500:
                            echo " - Pace 5 hours $lat $lon";
                            $lat500= $lat;
                            $long500 = $lon;
                            break;
                        case $pace515:
                            $lat515= $lat;
                            $long515 = $lon;
                            break;
                        case $pace530:
                            echo " - Pace 530 hours $lat $lon";
                            $lat530= $lat;
                            $long530 = $lon;
                            break;
                        case $pace600:
                            echo " - Pace 6 hours $lat, $lon";
                            $lat600= $lat;
                            $long600 = $lon;
                            break;
                        default:
                            
                    }
                           
                }
                
            }
        }
        else {
            echo "0 results";
        }
                
                
        // now we insert a new element into the database that has the updated lat and lon coordinates
        //and we also put the updated for the d3 lecture of information so it all works fine
                
        $sql = "INSERT INTO GeneralInformation (time, AlertStatus, temperature, windSpeed, windDirection, 
            humidity,RunnersOnCourse, FinishedRunners, HospitalTransports,
            PatientsSeen, 
            LeadMaleLat, LeadMaleLong, LeadFemaleLat, LeadFemaleLong, 
            LeadMaleLatHalf, LeadMaleLongHalf, LeadFemaleLatHalf, LeadFemaleLongHalf,
            LeadWheelchairMaleLat,LeadWheelchairMaleLong, LeadWheelchairFemaleLat, LeadWheelchairFemaleLong,
            pace350Lat, pace350Long, pace400Lat, pace400Long,
            pace415Lat, pace415Long, pace430Lat, pace430Long, pace500Lat, pace500Long, pace515Lat, pace515Long,
            pace530Lat, pace530Long, pace600Lat, pace600Long,
            Alert,emergencyCheck, AlertLat, AlertLong,shelterDisplay)
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
                
                ".$latLM.",
                ".$longLM.",
                ".$latLF.",
                ".$longLF.",
                
                ".$latLMH.",
                ".$longLMH.",
                ".$latLFH.",
                ".$longLFH.",
                
                ".$latLWM.",
                ".$longLWM.",
                ".$latLWF.",
                ".$longLWF.",
                
                ".$lat350.",
                ".$long350.",
                ".$lat400.",
                ".$long400.",
                ".$lat415.",
                ".$long415.",
                ".$lat430.",
                ".$long430.",
                ".$lat500.",
                ".$long500.",
                ".$lat515.",
                ".$long515.",
                
                ".$lat530.",
                ".$long530.",
                ".$lat600.",
                ".$long600.",
                
                \"".$alert."\" ,
                ".$emergencyCheck.",
                ".$latAl.",
                ".$longAl.",
                ".$shelter."
                );";
                
                    
        if ($db->query($sql) === TRUE) {
            echo "New record created successfully!!!!!!";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
        
        $db->close();
        
        $myfile = fopen("data/gen_info.csv","w") or die("Error opening file");
        
        $txt = "AlertStatus,temperature,windSpeed,windDirection,humidity,";
        $txt = $txt."runnersOnCourse,runnersFinished,hospitalTransports,patientsSeen,";
        $txt = $txt."LeadMaleRunnerLat,LeadMaleRunnerLong,LeadFemaleRunnerLat,LeadFemaleRunnerLong,TurtleLat,TurtleLong,";
        $txt = $txt."LeadMaleRunnerLatHalf,LeadMaleRunnerLongHalf,LeadFemaleRunnerLatHalf,LeadFemaleRunnerLongHalf,";
        $txt = $txt."LeadWheelchairMaleLat,LeadWheelchairMaleLong,LeadWheelchairFemaleLat,LeadWheelchairFemaleLong,";
        $txt = $txt."pace350Lat,pace350Long,pace400Lat,pace400Long,pace415Lat,pace415Long,pace430Lat,pace430Long,pace500Lat,pace500Long,pace515Lat,pace515Long,pace530Lat,pace530Long,pace600Lat,pace600Long,Alert,emergencyCheck,AlertLat,AlertLong,shelterDisplay\n";
        
        $txt = $txt.$alertStatus.",";
        $txt = $txt.$temperature.",";
        $txt = $txt.$windSpeed.",";
        $txt = $txt."\"".$windDirection."\",";
        $txt = $txt.$humidity.",";
        $txt = $txt.$runnersOc.",";
        $txt = $txt.$finished.",";
        $txt = $txt.$transports.",";
        $txt = $txt.$pSeen.",";
        
        $txt = $txt.$latLM.",";
        $txt = $txt.$longLM.",";
        $txt = $txt.$latLF.",";
        $txt = $txt.$longLF.",";
        $txt = $txt.$latTurtle.",";
        $txt = $txt.$longTurtle.",";
        
        $txt = $txt.$latLMH.",";
        $txt = $txt.$longLMH.",";
        $txt = $txt.$latLFH.",";
        $txt = $txt.$longLFH.",";

        $txt = $txt.$latLWM.",";
        $txt = $txt.$longLWM.",";
        $txt = $txt.$latLWF.",";
        $txt = $txt.$longLWF.",";

        $txt = $txt.$lat350.",";
        $txt = $txt.$long350.",";
        $txt = $txt.$lat400.",";
        $txt = $txt.$long400.",";
        $txt = $txt.$lat415.",";
        $txt = $txt.$long415.",";
        $txt = $txt.$lat430.",";
        $txt = $txt.$long430.",";
        $txt = $txt.$lat500.",";
        $txt = $txt.$long500.",";
        $txt = $txt.$lat515.",";
        $txt = $txt.$long515.",";
        $txt = $txt.$lat530.",";
        $txt = $txt.$long530.",";
        $txt = $txt.$lat600.",";
        $txt = $txt.$long600.",";
        
        $txt = $txt."\"".$alert."\",";
        $txt = $txt.$emergencyCheck.",";
        $txt = $txt.$latAl.",";
        $txt = $txt.$longAl.",";
        $txt = $txt.$shelter;
        
        echo $txt;
        
        fwrite($myfile,$txt);
        fclose($myfile);
 
        ?>

    </body>
</html>
