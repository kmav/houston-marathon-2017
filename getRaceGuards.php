<!DOCTYPE html>
<html>
    <head>
        <title>Race Guards Tracker Data </title>
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
        $scraped_page = curl("https://race-guards.firebaseio.com/houston.json?auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE0ODMwNDYzMjUsImQiOnsidWlkIjoiODY3NTMwOSJ9LCJleHAiOjE0ODU5MDcyMDAsInYiOjB9.rWQBSntm9a5uNxT77no8p31gGaHSUfJYAWdQMyoiqCo");    // Downloading IMDB home page to variable $scraped_page
        echo 'scraped page:';
        echo $scraped_page;
        echo 'stop';
        
        //console.log($scraped_page);
        
        echo 'start';

        $jsonData = json_decode($scraped_page,true);
        
        echo $jsonData;
        
        echo $jsonData["Andy"]["location"];
        
        
        
        $myfile = fopen("data/raceGuards.csv","w") or die("Error opening file");
        
        $fields = array("name", "lat", "long");
        
        fputcsv($myfile, $fields);
        
        foreach ($jsonData as $value){
            $name = $value["name"];
            $location = $value["location"];
            $location = explode(",",$location);
            $lat = $location[0];
            $long = $location[1];
            
            $newField = array($name,$lat,$long);
            
            fputcsv($myfile,$newField);
            
            
            echo "<p>$name | $newField</p>";
        }

        fclose($myfile);
 
        ?>

    </body>
</html>
