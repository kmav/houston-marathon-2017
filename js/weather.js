// Docs at http://simpleweatherjs.com
function displayWeather(data) {
  var temp = data[0].temperature;
  var windDirec = data[0].windDirection;
  var windSpeed = data[0].windSpeed;
  var humid = data[0].humidity;
  var status = data[0].AlertStatus;
  
  $(document).ready(function() {
        html = '<h2 style="color:black"><i class="temp" style="color:black"></i> ' + temp + '&deg;' + ' WBGT' + '</h2>';
        
        //trying to get the sun icon to show up
        //html += '<i id = "icon" width = "100px" height="100px"></i>';
        
        html += '<ul><li>' +'Memorial Park</li>';
        html += '<li class="currently">' + humid + '% RH</li>';
        
        if(windDirec=='N')
        html += '<li class="wind" style="text-transform: uppercase;"> '+ windSpeed + ' MPH &#8595</li></ul>';
        
        else if(windDirec=='E')
        html += '<li class="wind" style="text-transform: uppercase;"> '+ windSpeed + ' MPH &#8592</li></ul>';
        
        else if(windDirec='S')
        html += '<li class="wind" style="text-transform: uppercase;"> '+ windSpeed + ' MPH &#8593</li></ul>';
        
        else if(windDirec=='W')
        html += '<li class="wind" style="text-transform: uppercase;"> '+ windSpeed + ' MPH &#8594</li></ul>';
        
        else if(windDirec=='NE')
        html += '<li class="wind" style="text-transform: uppercase;"> '+ windSpeed + ' MPH &#8601</li></ul>';
        
        else if(windDirec=='NW')
        html += '<li class="wind" style="text-transform: uppercase;"> '+ windSpeed + ' MPH &#8600</li></ul>';
        
        else if(windDirec=='SE')
        html += '<li class="wind" style="text-transform: uppercase;"> '+ windSpeed + ' MPH &#8598</li></ul>';
        
        else if(windDirec=='SW')
        html += '<li class="wind" style="text-transform: uppercase;"> '+ windSpeed + ' MPH &#8599</li></ul>';
        

        
  $("#weather").html(html);
  
  //trying to get the sun icon to work
  // $("#icon")[0].style.width = '100px';
  
  // $("#icon")[0].style.height = '100px';
  
  // $('#icon')[0].style.background = "url('img/sun.png')";
  
  
  });


  // $(document).ready(function() {
  //   html = '<h2 style="color:black"><i class="icon-' + weather.code + '" style="color:black"></i> ' + temp + '&deg;' + ' WBGT' + '</h2>';
  //   $.simpleWeather({
  //     location: 'Houston, TX',
  //     woeid: '',
  //     unit: 'f',
  //     success: function(weather) {
  //       if (status==1)//alert level yellow 
  //       {
  //         html = '<h2 style="color:black"><i class="icon-' + weather.code + '" style="color:black"></i> ' + temp + '&deg;' + ' WBGT' + '</h2>';
  //       }
        
  //       else
  //       {
  //         html = '<h2 style="color:black"><i class="icon-' + weather.code + '" style="color:black"></i> ' + temp + '&deg;' + ' WBGT' + '</h2>';
  //       }

  //       html += '<ul><li>' +'Memorial Park</li>';
  //       html += '<li class="currently">' + humid + '% RH</li>';
        
  //       if(windDirec=='N')
  //       html += '<li class="wind" style="text-transform: uppercase;"> '+ windSpeed + ' MPH &#8595</li></ul>';
        
  //       else if(windDirec=='E')
  //       html += '<li class="wind" style="text-transform: uppercase;"> '+ windSpeed + ' MPH &#8592</li></ul>';
        
  //       else if(windDirec='S')
  //       html += '<li class="wind" style="text-transform: uppercase;"> '+ windSpeed + ' MPH &#8593</li></ul>';
        
  //       else if(windDirec=='W')
  //       html += '<li class="wind" style="text-transform: uppercase;"> '+ windSpeed + ' MPH &#8594</li></ul>';
        
  //       else if(windDirec=='NE')
  //       html += '<li class="wind" style="text-transform: uppercase;"> '+ windSpeed + ' MPH &#8601</li></ul>';
        
  //       else if(windDirec=='NW')
  //       html += '<li class="wind" style="text-transform: uppercase;"> '+ windSpeed + ' MPH &#8600</li></ul>';
        
  //       else if(windDirec=='SE')
  //       html += '<li class="wind" style="text-transform: uppercase;"> '+ windSpeed + ' MPH &#8598</li></ul>';
        
  //       else if(windDirec=='SW')
  //       html += '<li class="wind" style="text-transform: uppercase;"> '+ windSpeed + ' MPH &#8599</li></ul>';
        
  //       $("#weather").html("Test");
  //       //$("#weather").html(html);
  //     },
  //     error: function(error) {
  //       $("#weather").html('<p>' + error + '</p>');
  //     }
      
      
      
  //   });
  // });

}
d3.csv("data/genInfo.csv", displayWeather)
