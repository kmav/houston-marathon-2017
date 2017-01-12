var timeMultiplier=2;
var mapRefresh = 0;
var graphRefresh = 0;
var trackersRefresh = 0;
var pageUpdate = 0;
var densityUpdate = 0;

var startHour = 20;
var startMinute = 10;

var yScaleBoth = 0;

function filterMedicalTents(obj){
	return ((obj.Type=="MT")&&obj.Location!="DUMMY");
};

function filterAidStations(obj){
	//return false;
	return ((obj.Type=="AS")&&(+obj.Display==1));
};

function easyFilter(obj){
	return ((obj.Type=="AS"))&&(+obj.Status<=2);
}

function colorBars(current,beds,status){
	
	//initial check for closed!
	if (+status==2){
		return "rgb(112,112,112)";
		//////("BLACK!!!");
	}
	var percent = 100*(+current)/(+beds);
    if (percent >= 100) {
        percent = 99
    }
    var r, g, b;

    if (percent < 50) {
        // green to yellow
        r = 11;
        g = 181;
        b = 11;
		
    } else if (percent < 90) {
        // yellow to red
        r = 255;
        g = 220;
        b = 0;
    }
    
    else {
    	r = 255;
    	g = 0;
    	b = 0;
    }

    return "rgb(" + r + "," + g + "," + b + ")";
};

var key = function(d){
	return +d.Location;
}

var sortOrder = false;
var sortItems = function(a,b){
	if (sortOrder){
		return +a.Location - +b.Location;
	}
	return +b.Location - +a.Location;
}


function filterByMinute(obj){
  var minute = getMinute();
  minute = minute - minute%minuteInterval;
  // //////(obj);
  // //////(+obj.Minute+" = "+minute);
  return (+obj.Minute==minute);
}

function refreshPage() {
	window.location.reload(1);
}

function getMinute() {
    
  var currentTime = new Date();
  var nowTime = currentTime.getTime();

	var startedTime = new Date();
	
	var multiplier = 1;
	
	startedTime.setHours(startHour);
	startedTime.setMinutes(startMinute);
	startedTime.setSeconds(0);
	startedTime.setMilliseconds(0);

	var startedMs = startedTime.getTime();

	//now calculate the millisecond difference from one to other
	var elapsedTime = nowTime - startedMs;
	if (elapsedTime<0) {
		return 0;
	  elapsedTime = 0 - elapsedTime;
	}
	//1000 ms in a second, 60 seconds in a minute
	var elapsedMinutes = parseInt(elapsedTime*timeMultiplier / 60000);
	var elapsedMinutes = elapsedMinutes + elapsedMinutes%2;
    
  //////("Minute: "+elapsedMinutes);
  
  return (elapsedMinutes);

}

function updateClock()
{
	var currentTime = new Date();

	//make sure we're on the right timezone
	var offset = currentTime.getTimezoneOffset();
	////////(offset);
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
	startTime.setHours(startHour);
	startTime.setMinutes(startMinute);
	startTime.setSeconds(0);
	startTime.setMilliseconds(0);

	var startMs = startTime.getTime();

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
	////////(elapsedTimeString)
}

function updateMaps()
{
	generateLines();
	plotAS(1);
}

function updateTrackers()
{
	runnerTracking();
}


function updateASGraph(data)
{
	

	//////(window.location.pathname);
	//////("redrawing aid stations");
	//.table(data);

	var AidStations = [];
	var AidStationDataset =  data.filter(filterAidStations);
	
	if (AidStationDataset.length<3){
		AidStationDataset = data.filter(easyFilter);
	}
	
	AidStationDataset.reverse();
	//AidStationDataset = AidStationDataset.slice(0,AidStationDataset.length)
	
	var w = document.getElementById('aidStation').offsetWidth *0.8 ;
	var h = document.getElementById('aidStation').offsetHeight*0.77;
	
	var p = 10;
	
	var svg = d3.selectAll("#aid_station_graph");
	
	var xScale = d3.scale.linear()
    	.domain([0,4+d3.max(AidStationDataset,function(d){
						return +d.Beds;
					})])
    	.range([p,w-p]);
    	
   	var yScale = d3.scale.ordinal()
		.domain(d3.range(AidStationDataset.length))
		.rangeRoundBands([h-p,2*p],0.15);
					
	var xAxis = d3.svg.axis()
		.scale(xScale)
		.orient("bottom")
		.ticks(4);
					
	//write y axis
	var yAxis = d3.svg.axis()
		.scale(yScale)
		.orient("left");

	//make a function that returns axis to use later in the gridlines
	function make_xAxis(){
		return xAxis;
	}

	function make_yAxis(){
		return yAxis;
	}
	
	var ySpacing = (yScale(2)-yScale(1))/2;
	////.table(AidStationDataset);
	
	var bars = svg.selectAll(".bedstaken")
		.data(AidStationDataset,key);
	
	var totalbeds = svg.selectAll(".totalbeds")
		.data(AidStationDataset,key);
	
	var text = svg.selectAll(".text_bar")
		.data(AidStationDataset,key);
	
	
	bars.exit()
		.remove();
		
	totalbeds.exit()
		.remove();
	
	text.exit()
		.remove();
	
	
	totalbeds.enter()
		.append("rect")
		.attr("class","totalbeds");
		
	bars.enter()
		.append("rect")
		.attr("class","bedstaken");
	
	text.enter()
		.append("text")
		.attr("class","text_bar");
	
	totalbeds = svg.selectAll(".totalbeds")
		.sort(sortItems)
		.transition()
		.attr("x",function(d,i){
			return p;
		})
		.attr("y",function(d,i){
			////////(h));
			////////(yScale(i)+"yscale in AS");
			return (yScale(i));
			//return h-p-yScale(+d.CurrentPatients);
		})
		.attr("width",function(d){
			////////(h-yScale())
			//return yScale(+d.CurrentPatients);
			return (xScale(+d.Beds)-xScale(0));
		})
		
		.attr("height",yScale.rangeBand())
		.attr("fill","rgba(0,0,0,0.2)")

	bars = svg.selectAll(".bedstaken")
		.sort(sortItems)
		.transition()
		.attr("x",function(d,i){
					return p;
				})
		.attr("y",function(d,i){
			////////(h));
			//horizontal bars:
			return (yScale(i));
			//vertical bars
			//return h-p-yScale(+d.CurrentPatients);
		})
		.attr("width",function(d){
			////////(h-yScale())
			//used before for vertical
			//return yScale(+d.CurrentPatients);
			//horizontal: 
			if (+d.Status==2){
				return (xScale(+d.Beds)-p);
			}
			else{
				return (xScale(+d.CurrentPatients)-p);
			}
		})
		.attr("height",yScale.rangeBand())
		.attr("fill",function(d){
			//////(+d.CurrentPatients + " Current Patients");
			return colorBars(+d.CurrentPatients,+d.Beds,+d.Status);
		});
		
	text = svg.selectAll(".text_bar")
		.sort(sortItems)
		.transition()
		.text(function(d){
				if (+d.Location==10){
					return "A"+d.Location+" (Half)";
				}
				return "A"+d.Location;
			})
		.attr("y",function(d,i){
			return yScale(i)-ySpacing;
		})
		.attr("x",function(d){
			return d3.max([xScale(+d.Beds)+1.5*p,xScale(+d.CurrentPatients)+1.5*p]);
		})
		.attr("text-anchor","right")
		.style("font-weight",400)
		.style("font-size", function(d){
			if((window.location.pathname=="/command.php"))
			return ((yScale.rangeBand()*0.8))+'px';
			
			else
			return ((yScale.rangeBand()*0.75))+'px';
		});

}

function updateMTGraph(data){
	//This one does not require all the complication of AS since
	//you don't have things going in/out of the chart
	//so just update the bedsTaken field
	//and the tooltip (probably?)
	
	//////("UPDATING MT");
	//filter out to MT
	var AidStations = [];
	var MedicalTentsDataset =  data.filter(filterMedicalTents);
	
	if (MedicalTentsDataset.length<3){
		MedicalTentsDataset = data.filter(easyFilter);
	}
	
	var svg = d3.select("#MT_graph")
	var p = 10;
	var w = $('#MT_graph').width()*0.75;
	var h = $("#MT_graph").height()*0.75;
	
	var xScale = d3.scale.linear()
				.domain([0,1.2*d3.max(MedicalTentsDataset,function(d) { return +d.Beds;})])
				.range([p,w-p]);
				
	//now update the bedsTaken
	svg.selectAll(".bedstaken")
		.data(MedicalTentsDataset)
		.transition()
		//.transition()
		.attr("width",function(d) {
			//////(d.Location+" : "+d.CurrentPatients);
			return xScale(+d.CurrentPatients)-p;
		});
	//////(svg.selectAll(".bedstaken"));
		
	//////("Finished updating MT");
	
}



function updateGraphs()
{
	
	//since things change, we need to essentially write a full function to redo (with transition) the graphs
	d3.csv('data/AidStations.csv',updateASGraph);
	
	//update medical tent
	d3.csv('data/AidStations.csv',updateMTGraph);

	return;
}

function updateDensity()
{
	
	//use d3.csv to re-bind the full marathon data
	d3.csv("data/RunnerData.csv",function(data){
		
		var minute = getMinute();
  
		minute = minute - minute%minuteInterval;
		//////(minute);
		var margin = 15;
		var margins = {top: 20, right: 30, bottom: 30, left: 40};
		    
		var height= $("#sidebarGraphs").height()-margin;
		  
		var y = d3.scale.linear()
          	.range([height-margins.bottom,2*margin]);
		
		var RaceData = data.filter(filterByMinute);
		//.table(RaceData);
		
		  y.domain([0,d3.max(RaceData,function(d) {
    		return (parseInt((+d.Runners)/1000)+1)*1000;
    	})]);
		
		yScaleBoth = d3.max(RaceData,function(d) {return (parseInt((+d.Runners)/1000)+1)*1000;});
		
		// debugger;
		d3.selectAll(".fullBars")
			.data(RaceData)
			.attr("y",function(d) {return y(+d.Runners); })
			.attr("height",function(d) { return height - margins.bottom - y(+d.Runners); })
		
		d3.selectAll(".stackedBars")
			.data(RaceData)
			.attr("y",function(d) { return y(+d.Half); })
          	.attr("height", function(d) { return height-margins.bottom-y(+d.Half); })
	});
	

//now update the half marathon data
	d3.csv("data/RunnerDataHalf.csv",function(data){
		
		var minute = getMinute();
  
		minute = minute - minute%minuteInterval;
		//////(minute);
		var margin = 15;
		var margins = {top: 20, right: 30, bottom: 30, left: 40};
		    
		var height= $("#sidebarGraphs").height()-margin;
		  
		var y = d3.scale.linear()
          	.range([height-margins.bottom,2*margin]);
		
		var RaceData = data.filter(filterByMinute);
		//.table(RaceData);
		
		y.domain([0,yScaleBoth]);
		// yScaleBoth = d3.max(RaceData,function(d) {return +d.Runners; });
		// debugger;
		d3.selectAll(".halfBars")
			.data(RaceData)
			.attr("y",function(d) {return y(+d.Runners); })
			.attr("height",function(d) { return height - margins.bottom - y(+d.Runners); })
	});
	
	
	
	
	
	
	
	// d3.csv("data/RunnerDataHalf.csv",drawHalf);
	//then select with data and update tables
	
	//do this for both graphs
	
	
	
	return;
}

function updateGeneral(){
	d3.csv("data/genInfo.csv",displayInfo);
	d3.csv("simulation/DensitiesFull.csv",displayDrops);
	d3.csv("data/Densities.csv",displayRunnerData);
	//d3.csv("data/gen_info.csv",displayAlert);

}

// Docs at http://simpleweatherjs.com
// function displayWeather(data) {
//   var temp = data[0].temperature;
//   var windDirec = data[0].windDirection;
//   var windSpeed = data[0].windSpeed;
//   var humid = data[0].humidity;
//   var status = data[0].AlertStatus;

//   $(document).ready(function() {
//     $.simpleWeather({
//       location: 'Houston, TX',
//       woeid: '',
//       unit: 'f',
//       success: function(weather) {
//         if (status==1)//alert level yellow 
//         {
//           html = '<h2 style="color:black"><i class="icon-' + weather.code + '" style="color:black"></i> ' + temp + '&deg;' + ' WBGT' + '</h2>';
//         }
        
//         else
//         {
//           html = '<h2 style="color:black"><i class="icon-' + weather.code + '" style="color:black"></i> ' + temp + '&deg;' + ' WBGT' + '</h2>';
//         }

//         html += '<ul><li>' +'Memorial Park</li>';
//         html += '<li class="currently">' + weather.humidity + '% RH</li>';
        
//         if(windDirec=='N')
//         html += '<li class="wind" style="text-transform: uppercase;"> '+ weather.wind.speed + ' MPH &#8595</li></ul>';
        
//         else if(windDirec=='E')
//         html += '<li class="wind" style="text-transform: uppercase;"> '+ weather.wind.speed + ' MPH &#8592</li></ul>';
        
//         else if(windDirec='S')
//         html += '<li class="wind" style="text-transform: uppercase;"> '+ weather.wind.speed + ' MPH &#8593</li></ul>';
        
//         else if(windDirec=='W')
//         html += '<li class="wind" style="text-transform: uppercase;"> '+ weather.wind.speed + ' MPH &#8594</li></ul>';
        
//         else if(windDirec=='NE')
//         html += '<li class="wind" style="text-transform: uppercase;"> '+ weather.wind.speed + ' MPH &#8601</li></ul>';
        
//         else if(windDirec=='NW')
//         html += '<li class="wind" style="text-transform: uppercase;"> '+ weather.wind.speed + ' MPH &#8600</li></ul>';
        
//         else if(windDirec=='SE')
//         html += '<li class="wind" style="text-transform: uppercase;"> '+ weather.wind.speed + ' MPH &#8598</li></ul>';
        
//         else if(windDirec=='SW')
//         html += '<li class="wind" style="text-transform: uppercase;"> '+ weather.wind.speed + ' MPH &#8599</li></ul>';
        

//         $("#weather").html(html);
//       },
//       error: function(error) {
//         $("#weather").html('<p>' + error + '</p>');
//       }
//     });
//   });

// }



////////////////////////////MAIN UPDATE OF THE PAGE
function updatePage(){
	
	updateClock();
	mapRefresh++;
	graphRefresh++;
	pageUpdate++;
	trackersRefresh++;
	densityUpdate++;
	
	if (trackersRefresh==10)
	{
		updateTrackers();
		updateGeneral();
		d3.csv("data/genInfo.csv", displayWeather)

		trackersRefresh = 0;
	}
	
	if (mapRefresh==10)
	{
		updateMaps();
		mapRefresh = 0;
	}
	if (graphRefresh==10)
	{
		updateGraphs();
		graphRefresh = 0;
	}
	
	if (pageUpdate==120)
	{
		refreshPage();
		//////("refresh!!!");

	}
	
	if (densityUpdate==1)
	{
		 updateDensity();
	}
	densityUpdate = densityUpdate%10;
	
	
	
}
