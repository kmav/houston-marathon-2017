
function draw(data){
  
  "use strict";
  
   var minute = getMinute();
  
  minute = minute - minute%minuteInterval;
  console.log(minute);
  
  var margin = 15;
  var width = $("#densityPlot").width()-margin;
  var height= $("#densityPlot").height()-margin;

  var svg = d3.select("#densityPlot")
    .append("svg")
      .attr("width",width+margin)
      .attr("height",height+1*margin)
    .append("g")
      .attr("class","densityChart");
      
    // dimple.js chart code
    
       
    var now = String(minute);
    var later = String(minute+30);
    console.log(now);
    console.log(later);
    var datum = dimple.filterData(data,"Minute",[now,later])
    var myChart = new dimple.chart(svg,datum);
    var x = myChart.addCategoryAxis("x","Mile");
    x.addOrderRule("Mile");
    var y = myChart.addMeasureAxis("y","Runners");
   // var bubble = myChart.addSeries(null,dimple.plot.bubble);
    var line = myChart.addSeries("Minute",dimple.plot.line);
    //line.interpolation = "cardinal";

    //myChart.addLegend('10%', '10%', 510, 20, "right");
        myChart.draw();
    
 
    
    // svg.append("text")
    //   .attr("x",width-180-margin)
    //   .attr("y",margin)
    //   .attr("text-anchor","left")
    //   .attr("font-size",'12px')
    //   .text("Now");
    
    // svg.append("text")
    //   .attr("x",width-100-margin)
    //   .attr("y",margin)
    //   .attr("text-anchor","left")
    //   .attr("font-size",'12px')
    //   .text("In 30 minutes");
    
    // svg.append("rect")
    //   .attr("x",width-180-margin-25)
    //   .attr("y",margin-10)
    //   .attr("width",20)
    //   .attr("height",10)
    //   .attr("fill","rgb(141,180,209)");
    
    // svg.append("rect")
    //   .attr("x",width-100-margin-25)
    //   .attr("y",margin-10)
    //   .attr("width",20)
    //   .attr("height",10)
    //   .attr("fill","rgb(241,138,129)");
        
    svg.append("text")
      .attr("x",(width/2)+margin)
      .attr("y",margin)
      .attr("text-anchor","middle")
      .text("Runners per mile");
    
};

var minuteInterval = 2;
d3.csv("data/runners.tsv",draw);




// function drawDensity(data){
  
  
//   var filtered = data.filter()
  
  
//   var margin = 25;
//   var width = $("#densityPlot").width()-margin;
//   var height= $("#densityPlot").height()-margin;
  
//   var svg = d3.select("#densityPlot")
//     .append("svg")
//       .attr("width",width+2*margin)
//       .attr("height",height+2*margin)
//     .append("g")
//       .attr("class","densityChart");
      
//   var xScale = d3.scale.linear()
//               .domain([0,26])
//               .range([margin,width+margin]);
              
  
  
  
  
// }


// d3.csv("data/Densities.csv",drawDensity);