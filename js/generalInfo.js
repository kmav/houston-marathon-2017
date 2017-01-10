var alertMarker=0;
var currentDrops=0;
var currentStarted=0;
var currentFinished=0;

function displayDrops(data){
    var currentMin = getMinute();
    currentDrops = data[parseInt(currentMin/2)].drops;
        
    d3.select("#RunnersDropped")
    .text("\u2212 Drops: " + Math.round(currentDrops));
    console.log(currentDrops+"current");
}

function displayRunnerData(data){
    
    var currentMin = getMinute();
    var index = parseInt(currentMin/2);
    currentStarted = data[index].started;
    currentFinished = data[index].finished;
    
    d3.select("#RunnersStarted")
    .text("Started: " + currentStarted);
    
    d3.select("#RunnersFinished")
    .text("\u2212 Finished: " + currentFinished);
    
    console.log(currentMin + "minute")
}
    
function displayInfo(data){
    console.table(data);
    
	var run = data[0].runnersOnCourse;
    var runnersFinished = data[0].runnersFinished;
    var hospitalTransports = data[0].hospitalTransports;
    //var totalTreatments = data[0].patientsSeen;
    var Status = data[0].AlertStatus;
    var emergencyCheck = data[0].emergencyCheck;
    var AlertLat = data[0].AlertLat; 
    var AlertLong = data[0].AlertLong; 
    var message = data[0].Alert;
    var shelterDisplay = data[0].shelterDisplay;
    console.log("SHELTER DISPLAY::::: "+shelterDisplay);
    
    //display runners finished
    /*d3.select("#RunnersOnCourse")
    .text("On Course: " + run);
    
    d3.select("#RunnersFinished")
    .text("Finished: " + runnersFinished);
    */
    /*d3.select("#RunnersOnCourse")
    .text(run);
    
    d3.select("#RunnersFinished")
    .text(runnersFinished);
    
    
    d3.select("#HospitalTransports")
    .text("Hospital Transports: " + hospitalTransports);
    
    d3.select("#PatientsSeen")
    .text("Treatments: " + totalTreatments);
    */
    console.log(hospitalTransports+" transports");
    
    d3.select("#HospitalTransports")
    .text("Hospital Transports: " + hospitalTransports);
    
    d3.select("#PatientsSeen")
    .text("Total Treatments: " + totalTreatments);
    
    d3.select("#InMedical")
    .text("In-Treatment: " + inMedical);
    
    //d3.select("#RunnersStarted")
    //.text("Started: " + 3*test);
    
    /* 
    Get drop value from density file given current minute - 
    getMinute() returns race minute, get floor matching minutes
    */
    /*d3.select("#RunnersDropped")
    .text("\u2212 Drops: " + test);
    console.log('testing drops')
    */
    //d3.select("#RunnersFinished")
    //.text("\u2212 Finishers: " + test);

    var currentOnCourse = currentStarted - currentDrops - currentFinished;
    d3.select("#RunnersOnCourse")
    .text("On Course: " + currentOnCourse);
    
    d3.select("#alertBar")
        .attr("class",function(){
            switch (+emergencyCheck){
                case 0:
                    console.log("alert bar white");
                    return 'white';
                    break;
                case 1:
                    console.log("alert bar red");
                    return 'red';
                    break;
            }
        });
      

    d3.select("#alertText")
    .text(message);
    
    console.log(message);
    
    d3.select("#mediumRow")
        .attr("class",function(){
            console.log(Status);
            switch (+Status){
                case 0:
                    return 'green';
                    break;
                case 1:
                    return 'yellow';
                    break;
                case 2:
                    return 'red';
                    break;
                case 3:
                    return 'black';
                    break;
            }
        });
        
    d3.select("#marathonLogo")
        .attr("class",function(){
            if ((+Status)==1){
                return 'black';
            }
            else{
                return 'white';
            }
        });
    
    d3.select("#aramcoLogo")
        .attr("class",function(){
            if ((+Status)==1){
                return 'black';
            }
            else{
                return 'white';
            }
        });
    
    d3.select("#NUlogo")
        .attr("class",function(){
            if ((+Status)==1){
                return 'purple';
            }
            else{
                return 'white';
            }
        });
        
         
    var temp = data[0].temperature;
    var windspeed = data[0].windSpeed;
    var winddirec = data[0].windDirection;
    var humidity = data[0].humidity;

    
    //display runners finished
    // console.log(temp);
    // console.log(windspeed);
    
    d3.select("#Temp")
    .text(temp + " °F");
    
    console.log("TEMPERATURE: "+temp)
    
    d3.select("#WindHumid")
    .text(windspeed + " mph " + winddirec + ", RH: " + humidity + "%");
    
    // console.log(run);
    // console.log(runnersFinished);
    
    //adding popup emergency marker on map 
                // console.log(AlertLat);
                // console.log(AlertLong);
    /*           L.mapbox.featureLayer({
                    type: 'Feature',
                    geometry: {
                        type: 'Point',
                        // coordinates here are in longitude, latitude order because
                        // x, y is the standard for GeoJSON and many formats
                        coordinates: [
                            AlertLong, AlertLat
                        ]
                    },
                    properties: {
                        'marker-color': '#FF0000',
                        'marker-symbol': 'cross',
                        "icon": {
                            'iconSize': [50,50],
                            'iconAnchor': [25,25]
                        }
                        
                    }
                }).addTo(map); */
if (alertMarker!=0){
map.removeLayer(alertMarker);
}
if(emergencyCheck==1){    
    
alertMarker = L.marker([AlertLat, AlertLong], {
    icon: L.divIcon({
        // specify a class name that we can refer to in styles, as we
        // do above.
        className: 'fa-icon',
        // html here defines what goes in the div created for each marker
        html: '<i class="fa fa-exclamation-triangle fa-5x"  style = "color:red"></i>',
        // and the marker width and height
        iconSize: [60, 60]
    })
});
alertMarker.addTo(map);

}

if (shelterDisplay==1){
    console.log("now I'll put the dots onthe map");


//// shelters
    // Setup our svg layer that we can manipulate with d3
    var svg = d3.select(map.getPanes().overlayPane)
      .append("svg");
    var g = svg.append("g").attr("class", "leaflet-zoom-hide");
    
    function project(ll) {
        //console.log('projecting:');
      // our data came from csv, make it Leaflet friendly
      var a = [+ll.lat, +ll.lon]; 
      // convert it to pixel coordinates
      var point = map.latLngToLayerPoint(L.latLng(ll))
      return point;
    }
    
    d3.csv("data/shelters.csv", function(err, data) {
      var dots = g.selectAll("circle.dot")
        .data(data)
      console.log("data on shelters:")
      console.table(data);
      dots.enter().append("circle").classed("dot", true)
      .attr("r", 1)
      .style({
        fill: "#FFFFFF",
        "fill-opacity": 0.9,
        stroke: "#004d60",
        "stroke-width": 1
      })
      .transition().duration(1000)
      .attr("r", 6)
      
      
      function render() {
        // We need to reposition our SVG and our containing group when the map
        // repositions via zoom or pan
        // https://github.com/zetter/voronoi-maps/blob/master/lib/voronoi_map.js
        var bounds = map.getBounds();
        var topLeft = map.latLngToLayerPoint(bounds.getNorthWest())
        var bottomRight = map.latLngToLayerPoint(bounds.getSouthEast())
        svg.style("width", map.getSize().x + "px")
          .style("height", map.getSize().y + "px")
          .style("left", topLeft.x + "px")
          .style("top", topLeft.y + "px");
        g.attr("transform", "translate(" + -topLeft.x + "," + -topLeft.y + ")")
        g.attr("z-index",10);

        // We reproject our data with the updated projection from leaflet
        g.selectAll("circle.dot")
        .attr({
          cx: function(d) { return project(d).x},
          cy: function(d) { return project(d).y},
        })
        // .call(function(d){
        //     d3.select(this).moveToFront();
        // })

      };

      // re-render our visualization whenever the view changes
      map.on("viewreset", function() {
        render();
      })
      map.on("move", function() {
        render();
      })

      // render our initial visualization
      render();
    });
}
    
}

d3.csv("simulation/DensitiesFull.csv",displayDrops);
d3.csv("data/Densities.csv",displayRunnerData);
d3.csv("data/genInfo.csv",displayInfo);



//may make new general info file with runners on course, runners finished, hospital transports, and patients seen
