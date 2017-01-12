


function drawFullStack(data){
  
  "use strict";
  
  var minute = getMinute();
  
  minute = minute - minute%minuteInterval;
  //(minute);
 var margin = 15;
 var margins = {top: 20, right: 30, bottom: 30, left: 40};
    
  var width = $("#sidebarGraphs").width()*2/3-margin;
  var height= $("#sidebarGraphs").height()-margin;
  
  var y = d3.scale.linear()
          .range([height-margins.bottom,2*margin]);
          
          

  var chart = d3.select(".fullChart")
          .attr("width",width)
          .attr("height",height);
          

  //filter data to the one from this minute

  var RaceData =  data.filter(filterByMinute);
  // //.table(RaceData);
  
    //xscale
  var x = d3.scale.linear()
    .domain([0,27])
    .range([margins.left,width]);
    //.rangeRoundBands([margins.left,width], 0.2);
    
  var barWidth = (x(3)-x(2));
  
  //("Width is "+barWidth);
  barWidth = (x(3)-x(2))*.6;

  y.domain([0,yScaleBoth]);

		// yScaleBoth = d3.max(RaceData,function(d) {return (parseInt((+d.Runners)/1000)+1)*1000; });
  
  
  
  //var barWidth = width/RaceData.length;
  
  var bar = chart.selectAll("rect")
          .data(RaceData)
          .enter()
          .append("rect")
          .attr("class","stackedBars")
          .attr("x",function(d,i) {
            return +x(+d.Mile)-barWidth/2;
          })
          .attr("y",function(d) { return y(+d.Runners); })
      .attr("height", function(d) { return height-margins.bottom-y(+d.Runners); })
      .attr("width", barWidth);
  
    
};

var minuteInterval = 2;
d3.csv("data/RunnerDataStack.csv",drawFullStack);





