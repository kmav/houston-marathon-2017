minuteInterval= 2;

d3.selection.prototype.moveToFront = function() {  
      return this.each(function(){
        this.parentNode.appendChild(this);
      });
    };
    
d3.selection.prototype.moveToBack = function() {  
    return this.each(function() { 
        var firstChild = this.parentNode.firstChild; 
        if (firstChild) { 
            this.parentNode.insertBefore(this, firstChild); 
        } 
    });
};

MileMarkers = [];
function plotFullMile(update){
    
    var MileMarkers = [];
    var fullMileLoc = [];
    d3.csv("data/milemarkers/milefull.csv", function(d) {
        //////(d);
        fullMileLoc = d;
        return {
            MileNumber: d.MileNumber,
            Latitude: +d.Latitude,
            Longitude: +d.Longitude
        };
    },
    function(error,rows) {
        
        ////(rows);
        
        for (var i = 0; i < 25; i++) {
            geojson[16+i]["geometry"]["coordinates"] = [rows[i].Longitude,rows[i].Latitude]
            geojson[16+i]["properties"]["icon"]["html"] = (i+1);
            
            geojson[16+i]["properties"]["icon"]["className"] = "my-icon icon-hm";
            geojson[16+i]["properties"]["icon"]["iconSize"] = null;
            //////(MileMarkers);
        }
        
        // Miles.setGeoJSON(MileMarkers);
    }
    );

}

// function plotHalfMile(update){
    
//     MileMarkers = [];
//     var halfMileLoc = [];
//     d3.csv("data/milemarkers/milehalf.csv", function(d) {
//         //////(d);
//         halfMileLoc = d;
//         return {
//             MileNumber: d.MileNumber,
//             Latitude: +d.Latitude,
//             Longitude: +d.Longitude
//         };
//     },
//     function(error,rows) {
        
//         ////(rows);
        
//         for (var i = 0; i < 5; i++) {
//             MileMarkers.push({
//                 type: 'Feature',
//                 geometry: {
//                     type: 'Point',
//                     coordinates: [
//                         rows[i].Longitude, rows[i].Latitude
//                     ]
//                 },
//                 properties: {
//                     'title': 'Mile Marker ' + (i+8),
//                     'marker-size': 'small',
//                     'marker-color': '#00C5FE',
//                     'marker-symbol': (i+8)
//                 }
//             });
//             //////(MileMarkers);
//         }
        



        
//         Miles.setGeoJSON(MileMarkers);
//     }
//     );

// }

function plotAS(update){
  
  
  size = 'small';
  // //Plot markers for the aid stations
  var aidLoc = [];
  var aidColor = [];
  // load the AidStation file 
  
  // d3.csv("filename",function(d), function(error,rows))
  
  d3.csv("data/AidStations.csv", function(d) {
        // Add a LatLng object to each item in the dataset
        aidLoc = d;
        return {
            //use function(d)  to give all the columns names 
            //+ ones are numeric
            Type: d.Type,
            Latitude: +d.Latitude,
            Longitude: +d.Longitude,
            Location: d.Location,
            RaceKM: +d.RaceKM,
            Status: d.Status,
            CurrentPatients: +d.CurrentPatients,
            Beds: +d.Beds
        };
    },
    //rows takes in all the rows
    function(error, rows) {
        ////(rows);
    
        AidStationsGEOJSON = []
        
        //15 aid stations
        for (var i = 0; i < 15; i++) { //try forEach
            //debugger;
            //gets percentage of patients (beds = capacity of aid stations)
            var percent = 100 * (+rows[i].CurrentPatients / +rows[i].Beds);
            ////(+rows[i].Beds);
            
            //if that aid station is closed (=2)
            if ((+rows[i].Status) == 2) {
                //create an aid station marker
                AidStationsGEOJSON.push(
                  {
                    type: 'Feature',
                    geometry: {
                        type: 'Point',
                        // coordinates here are in longitude, latitude order because
                        // x, y is the standard for GeoJSON and many formats
                        coordinates: [
                            rows[i].Longitude, rows[i].Latitude
                        ]
                    },
                    properties: {
                        'title': 'Closed',
                        'marker-size': size,
                        'marker-color': '#878787',
                        //either a number or one letter on the marker
                        'marker-symbol': rows[i].Location
                    }
                });
                //closed marker

            }
            //if percent of occupancy is less than 50
            else if (percent < 50) {
                AidStationsGEOJSON.push({
                    // this feature is in the GeoJSON format: see geojson.org
                    // for the full specification
                    type: 'Feature',
                    geometry: {
                        type: 'Point',
                        // coordinates here are in longitude, latitude order because
                        // x, y is the standard for GeoJSON and many formats
                        coordinates: [
                            rows[i].Longitude, rows[i].Latitude
                        ]
                    },
                    properties: {
                        'title': 'Aid Station ' + rows[i].Location +'<br>Current Patients: ' + rows[i].CurrentPatients + '/' + rows[i].Beds,
                        'marker-size': size,
                        'marker-color': '#009933',
                        'marker-symbol': rows[i].Location
                    }
                });
                //create green marker

            }
            //debugger;
            else if (percent < 90) {
                AidStationsGEOJSON.push({
                    type: 'Feature',
                    geometry: {
                        type: 'Point',
                        // coordinates here are in longitude, latitude order because
                        // x, y is the standard for GeoJSON and many formats
                        coordinates: [
                            rows[i].Longitude, rows[i].Latitude
                        ]
                    },
                    properties: {
                        'title': 'Aid Station ' + rows[i].Location +'<br>Current Patients: ' + rows[i].CurrentPatients + '/' + rows[i].Beds,
                        'marker-size': size,
                        'marker-color': '#FFDC00',
                        'marker-symbol': rows[i].Location
                    }
                });
                //create yellow marker

            }
            else {
                AidStationsGEOJSON.push({
                    type: 'Feature',
                    geometry: {
                        type: 'Point',
                        // coordinates here are in longitude, latitude order because
                        // x, y is the standard for GeoJSON and many formats
                        coordinates: [
                            rows[i].Longitude, rows[i].Latitude
                        ]
                    },
                    properties: {
                        'title': 'Aid Station ' + rows[i].Location +'<br>Current Patients: ' + rows[i].CurrentPatients + '/' + rows[i].Beds,
                        'marker-size': 'large',
                        'marker-color': '#ff0000',
                        'marker-symbol': rows[i].Location
                    }
                });
                //create red marker
            }
            
            //at the end so you don't keep overlaying images (Aid Station Feature Layer)
            ASFL.clearLayers();
            //set new geojson data, takes array you have and puts it on the map
            ASFL.setGeoJSON(AidStationsGEOJSON);
        };

        //if (update==0){
          //only add medical tent if it's the first time
          //add medical tent markers (only show Balbo, not both Balbo/Pod) 
          for(var i=16; i<17; i++){ 
              //////(rows[i].Longitude);
              if (size=="medium"){
                var class_size = "fa-2x";
              }
              else{
                var class_size = "fa-3x";
              }
              L.marker([rows[i].Latitude, rows[i].Longitude], {
                icon: L.divIcon({
                  // specify a class name that we can refer to in styles, as we
                  // do above.
                  className: 'fa-icon',
                  // html here defines what goes in the div created for each marker
                  html: '<i class="fa fa-plus-square '+class_size+'" style = "color:red"></i>',
  
                  // and the marker width and height
                  iconSize: [60, 60]
                })
              }).addTo(ASFL);
          };
    });
}


function generateLines() {
    
    pathsLayer.clearLayers();
    returnArray = [];
    
    //takes runner data (load csv) then run the following function
    //densities.csv is from simulation
    var runnerData = d3.csv('data/Densities.csv', function(error, data) {

        // getMinute() is in updateAll
        var minute = getMinute();
        // debugger;
        ////(minute);
        ////(data);
        
        //divide by two because data array is every two minutes
        //35th minute will be 17th element 
        var data = data[parseInt(minute/2)];
        //.table(data);

        //map looks at every element in the array.
        var data = $.map(data, function(value, index) {
            //+ makes value from a string into an int or vice versa
            return [+value];
        });


        if (error) return //.warn(error);
        // //.table(data);

        //26 miles + last segment (26.2) + 3 mile markers for where the half marathon splits 
        for (var i = 0; i < 30; i++) {
            
            //number of runners at mile i (because miles begin at index 2)
            var runners = +data[i+2];
            ////("Mile "+i+" - runners: "+runners);
            // debugger;
            //set properties of that segment i
            //default is green
            var segmentStyle = {
                number: i + 1,
                color: 'green',
                weight: '5',
                opacity: 1
            }
            //change colors based on runners density
            switch (Math.floor(runners / 1000)) {
                case 0:
                    break;
                case 1:
                    segmentStyle.color = 'yellow';
                    break;
                case 2:
                    segmentStyle.color = 'orange';
                    segmentStyle.weight = '7';
                    break;
                case 3:
                    segmentStyle.color = 'red';
                    segmentStyle.weight = '8';
                default:
                    segmentStyle.color = 'red';
                    segmentStyle.weight = '10';
            }
            if (runners<500)
            {
                segmentStyle.color = '#a6a6a6';
            }
            
            ////(segmentStyle);
            
            //remove the old map if you have done the first one already
            if (started==1){
                //layerGroup.removeLayer(map);
                map.removeLayer(polylineArr[i]);
                started=1;
            }
            started=1;
            //now add a new one and store it
            polylineArr[i]=plotSegment(i, segmentStyle, runners);
        }
        

    });
    // debugger;
    //return returnArray;
}

//PolylineStyling is segment style which is defined above (has the color, etc.)
function plotSegment(segmentNumber, PolylineStyling, runners) {
  
    //draws a single mile on the map 
    
    ////("Inside plotSegment!");
    //each mile on the map is a bunch of connected dots and polyline draws it
    var polyline = d3.csv('data/milemarkers/mile' + (segmentNumber + 1) + '.csv', function(error, data) {
        ////('interval: '+segmentNumber)
        var i = 0
        if (error) return //.warn(error);
        //now try to create a mapping of it
        coords = data.map(function(d, i) {
            return [parseFloat(d.Latitude), parseFloat(d.Longitude)];
        });
        // debugger;
        //create a polyline with certain coordinates and styling
        polyline = L.polyline(coords, PolylineStyling)
            .bindPopup('Runners:' + runners)
            .addTo(pathsLayer);
            
        return polyline;
    });

    return polyline;
}

//GPS
function runnerTracking(){
      //plot runner tracking on map
      
      var runLoc = [];
      d3.csv("data/gen_info.csv", function(d) {
          // Add a LatLng object to each item in the dataset
          //.table(d);
          //("Here is the tracking data:");
          //(d);
          runLoc = d;
          return {
              latLWM: +d.LeadWheelchairMaleLat,
              longLWM: +d.LeadWheelchairMaleLong,
              latLWF: +d.LeadWheelchairFemaleLat,
              longLWF: +d.LeadWheelchairFemaleLong,
              LMRLat: +d.LeadMaleRunnerLat,
              LMRLong: +d.LeadMaleRunnerLong,
              LFRLat: +d.LeadFemaleRunnerLat,
              LFRLong: +d.LeadFemaleRunnerLong,
              LMRLatH: +d.LeadMaleRunnerLatHalf,
              LMRLongH: +d.LeadMaleRunnerLongHalf,
              LFRLatH: +d.LeadFemaleRunnerLatHalf,
              LFRLongH: +d.LeadFemaleRunnerLongHalf,
              pace350Lat: +d.pace350Lat,
              pace350Long: +d.pace350Long,
              pace400Lat: +d.pace400Lat,
              pace400Long: +d.pace400Long,
              pace415Lat: +d.pace415Lat,
              pace415Long: +d.pace415Long,
              pace500Lat: +d.pace500Lat,
              pace500Long: +d.pace500Long,
              pace530Lat: +d.pace530Lat,
              pace530Long: +d.pace530Long,
              pace600Lat: +d.pace600Lat,
              pace600Long: +d.pace600Long
          };
      
      }, function(error, rows) {
      
        ////(rows);
        //.table(rows);
        // debugger;
        //debugger;
        geojson[0]["geometry"]["coordinates"] = [rows[0].longLWM,rows[0].latLWM]
        geojson[1]["geometry"]["coordinates"]  = [rows[0].longLWF,rows[0].latLWF]
        geojson[2]["geometry"]["coordinates"]  = [rows[0].LMRLong,rows[0].LMRLat]
        geojson[3]["geometry"]["coordinates"]  = [rows[0].LFRLong,rows[0].LFRLat]
        geojson[4]["geometry"]["coordinates"]  = [rows[0].LMRLongH,rows[0].LMRLatH]
        geojson[5]["geometry"]["coordinates"]  = [rows[0].LFRLongH,rows[0].LFRLatH]
        geojson[6]["geometry"]["coordinates"]  = [rows[0].pace350Long,rows[0].pace350Lat]
        geojson[7]["geometry"]["coordinates"]  = [rows[0].pace400Long,rows[0].pace400Lat]
        geojson[8]["geometry"]["coordinates"]  = [rows[0].pace415Long,rows[0].pace415Lat]
        geojson[9]["geometry"]["coordinates"]  = [rows[0].pace500Long,rows[0].pace500Lat]
        geojson[10]["geometry"]["coordinates"]  = [rows[0].pace530Long,rows[0].pace530Lat]
        geojson[11]["geometry"]["coordinates"]  = [rows[0].pace600Long,rows[0].pace600Lat]

      
      
        geojson[0]["properties"]["icon"]["html"] = "Spare";
        geojson[1]["properties"]["icon"]["html"] = "T";
        geojson[2]["properties"]["icon"]["html"] = "LeadM";
        geojson[3]["properties"]["icon"]["html"] = "LeadF";
        geojson[4]["properties"]["icon"]["html"] = "HalfM";
        geojson[5]["properties"]["icon"]["html"] = "HalfW";
        geojson[6]["properties"]["icon"]["html"] = "3:50";
        geojson[7]["properties"]["icon"]["html"] = "4:00";
        geojson[8]["properties"]["icon"]["html"] = "4:15";
        geojson[9]["properties"]["icon"]["html"] = "5:00";
        geojson[10]["properties"]["icon"]["html"] = "5:30";
        geojson[11]["properties"]["icon"]["html"] = "6:00";

        for (var p=0;p<12;p++)
        {
            geojson[p]["properties"]["icon"]["className"] = "my-icon icon-sf";
            geojson[p]["properties"]["icon"]["iconSize"] = null;
        }
        
        trackingLayer.clearLayers();
        trackingLayer.setGeoJSON([]);
        //("Putting them on the map");
        //(geojson);
        trackingLayer.setGeoJSON(geojson);
        
      });
      
    ////('here is the geojson');
    ////(geojson);
    trackingLayer.on('layeradd', function(e) {
      var marker = e.layer,
          feature = marker.feature;
      marker.setIcon(L.divIcon(feature.properties.icon));
    });
};



//GPS
function raceGuardTracking(){

      
      d3.csv("data/raceGuards.csv", function(d) {
        
        var numberOfRows = d.length; // we can easily get the number of rows (excluding the title row)
        
        //("Number of trackers: " + numberOfRows);
        
        var geojson = [];
        

        for(var i=0; i<numberOfRows; i++){
          
          // //("long:" + d[i].long);
          // //("lat:" + d[i].lat);
          
          // newjson["geometry"]["coordinates"] = [d[i].long,d[i].lat];
          // //(newjson["geometry"]["coordinates"]);
          geojson.push(          
            {
              "type": "Feature",
              "geometry": {
                "type": "Point",
                "coordinates": [d[i].long,d[i].lat]
              },
              "properties": {
                "name": "",
                "icon": {"className":"my-icon icon-sf"}
              }
            }
           );
        
        }
          
            raceGuardsLayer.clearLayers();
            raceGuardsLayer.setGeoJSON([]);
            //("geojson");
            //(geojson);
            raceGuardsLayer.setGeoJSON(geojson);
      });

    ////('here is the geojson');
    ////(geojson);
    raceGuardsLayer.on('layeradd', function(e) {
      var marker = e.layer,
          feature = marker.feature;
      marker.setIcon(L.divIcon(feature.properties.icon));
    });
};




L.mapbox.accessToken = 'pk.eyJ1IjoiYnBleW5ldHRpIiwiYSI6IjNjMjQ0NTM4MTE0MmM0ODkwYTA0Mjg0NGYyZGM4MzM5In0.K96jFRdiKaEPadA1IxKoQw';
//map refers to id in desktopHouston.php
var map = L.mapbox.map('map', 'bpeynetti.ed1c07fe')
    .setView([29.753192, -95.422], 13);
    

// map.touchZoom.disable();
// map.doubleClickZoom.disable();
// map.scrollWheelZoom.disable();

//create 3 layers minumum
//gps and milemarkers
var trackingLayer = L.mapbox.featureLayer().addTo(map);
//raceGuards
var raceGuardsLayer = L.mapbox.featureLayer().addTo(map);
//runner density
var pathsLayer = L.mapbox.featureLayer().addTo(map);

started = 0;
var polylineArr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
var coordsArr = [];
//now try to create slices of 2 by 2

////("Putting the mile lines on the map ");
var PolylineStyling = generateLines();
    
//for gps trackers and runners (blue dots that are linked to GPS trackers)    
var geojson = [
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      //all get generated to this new location
      "coordinates": [-75.031952,30.913184]
    },
    "properties": {
      "icon": {
        "className": "my-icon icon-dc", // class name to style
        "html": "&#9733;", // add content inside the marker
        "iconSize": null // size of icon, use null to set the size in CSS
      }
    }
  },
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-77.031952,38.913184]
    },
    "properties": {
      "icon": {
        "className": "my-icon icon-dc", // class name to style
        "html": "&#9733;", // add content inside the marker
        "iconSize": null // size of icon, use null to set the size in CSS
      }
    }
  },
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-77.031952,38.913184]
    },
    "properties": {
      "icon": {
        "className": "my-icon icon-dc", // class name to style
        "html": "&#9733;", // add content inside the marker
        "iconSize": null // size of icon, use null to set the size in CSS
      }
    }
  },
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-77.031952,38.913184]
    },
    "properties": {
      "icon": {
        "className": "my-icon icon-dc", // class name to style
        "html": "&#9733;", // add content inside the marker
        "iconSize": null // size of icon, use null to set the size in CSS
      }
    }
  },
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-77.031952,38.913184]
    },
    "properties": {
      "icon": {
        "className": "my-icon icon-dc", // class name to style
        "html": "&#9733;", // add content inside the marker
        "iconSize": null // size of icon, use null to set the size in CSS
      }
    }
  },
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-77.031952,38.913184]
    },
    "properties": {
      "icon": {
        "className": "my-icon icon-dc", // class name to style
        "html": "&#9733;", // add content inside the marker
        "iconSize": null // size of icon, use null to set the size in CSS
      }
    }
  },
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-77.031952,38.913184]
    },
    "properties": {
      "icon": {
        "className": "my-icon icon-dc", // class name to style
        "html": "&#9733;", // add content inside the marker
        "iconSize": null // size of icon, use null to set the size in CSS
      }
    }
  },
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-77.031952,38.913184]
    },
    "properties": {
      "icon": {
        "className": "my-icon icon-dc", // class name to style
        "html": "&#9733;", // add content inside the marker
        "iconSize": null // size of icon, use null to set the size in CSS
      }
    }
  },
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-77.031952,38.913184]
    },
    "properties": {
      "icon": {
        "className": "my-icon icon-dc", // class name to style
        "html": "&#9733;", // add content inside the marker
        "iconSize": null // size of icon, use null to set the size in CSS
      }
    }
  },
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-77.031952,38.913184]
    },
    "properties": {
      "icon": {
        "className": "my-icon icon-dc", // class name to style
        "html": "&#9733;", // add content inside the marker
        "iconSize": null // size of icon, use null to set the size in CSS
      }
    }
  },
    {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-77.031952,38.913184]
    },
    "properties": {
      "icon": {
        "className": "my-icon icon-dc", // class name to style
        "html": "&#9733;", // add content inside the marker
        "iconSize": null // size of icon, use null to set the size in CSS
      }
    }
  },
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-77.031952,38.913184]
    },
    "properties": {
      "icon": {
        "className": "my-icon icon-dc", // class name to style
        "html": "&#9733;", // add content inside the marker
        "iconSize": null // size of icon, use null to set the size in CSS
      }
    }
  },
  {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-77.031952,38.913184]
    },
    "properties": {
      "icon": {
        "className": "my-icon icon-dc", // class name to style
        "html": "&#9733;", // add content inside the marker
        "iconSize": null // size of icon, use null to set the size in CSS
      }
    }
  },
  {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-95.395097,29.725794]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm1", // class name to style
          "html": "8H", // add content inside the marker
          "iconSize": null, // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-95.391111,29.73275]
      },
      "properties": {
        "icon": {
          "title": "9Half",
          "className": "my-icon icon-hm1", // class name to style
          "html": "9H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-95.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm1", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    
    //full miles
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [0,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    },
{
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-90.391066,29.746207]
      },
      "properties": {
        "icon": {
          "className": "my-icon icon-hm", // class name to style
          "html": "10H", // add content inside the marker
          "iconSize": null // size of icon, use null to set the size in CSS
        }
      }
    }
];


// var MileMarkers = [
//     {
//       "type": "Feature",
//       "geometry": {
//         "type": "Point",
//         "coordinates": [-95.395097,29.725794]
//       },
//       "properties": {
//         "icon": {
//           "className": "my-icon icon-sf", // class name to style
//           "html": "&#9733;", // add content inside the marker
//           "iconSize": null // size of icon, use null to set the size in CSS
//         }
//       }
//     },
//     {
//       "type": "Feature",
//       "geometry": {
//         "type": "Point",
//         "coordinates": [-95.391111,29.73275]
//       },
//       "properties": {
//         "icon": {
//           "className": "my-icon icon-sf", // class name to style
//           "html": "9H", // add content inside the marker
//           "iconSize": null // size of icon, use null to set the size in CSS
//         }
//       }
//     },
//     {
//       "type": "Feature",
//       "geometry": {
//         "type": "Point",
//         "coordinates": [-95.391066,29.746207]
//       },
//       "properties": {
//         "icon": {
//           "className": "my-icon icon-sf", // class name to style
//           "html": "10H;", // add content inside the marker
//           "iconSize": null // size of icon, use null to set the size in CSS
//         }
//       }
//     }
    
// ];


    
    
Miles = L.mapbox.featureLayer().addTo(map);
ASFL = L.mapbox.featureLayer().addTo(map);

// Miles.setGeoJSON(halfMile);

trackingLayer.setGeoJSON(geojson);

//raceGuardsLayer.setGeoJSON(geojson);


////("Printing the miles!");
plotFullMile(1);
// plotHalfMile(1);
////("Putting aid stations on the map");
//plot Aid Stations
plotAS(1);
//plotHalfMile(1);
runnerTracking();
raceGuardTracking();

