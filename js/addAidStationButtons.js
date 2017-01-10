/// HELPER FUNCTION

function InsertCheckBoxes(number,Text){
    
    var CheckBoxesHolder = AidBoxes.append("div")
    .attr("class","checkBoxHolder");
    2
    var CheckBoxes = CheckBoxesHolder.append("input")
    .attr("class","checkBox")
    .attr("type","radio")
    .attr("name",function(d){
        return "AS_status"+d.Location;
    })
    .attr("id",function(d,i){
        return "AS_status"+d.Location+"_"+number;
    })
    .attr("value",number)
    .property("checked",function(d){
        //determine if it's checked or not by looking at original status
        return (+d.Status)==number;
        
    });
    
    var Textbox = CheckBoxesHolder.append("div")
                .attr("class",function(){
                    return "checkBoxTxt "+Text;
                })
                .text(Text);



    
}


function InsertDisplay(){
    
    var displayAidHolder = AidBoxes.append("div")
    .attr("class","displayAidHolder");
    
    var CheckBoxes = displayAidHolder.append("input")
    .attr("name",function(d){
        return d.Type+"_Display"+d.Location;
    })
    .attr("class","checkBox")
    .attr("type","checkbox")
    .property("checked",function(d){
        console.table(d);
        console.log(d.Location+":"+d.Display);
        return +d.Display==1;
    });
    
    var Textbox = displayAidHolder.append("div")
                .attr("class",function(){
                    return "checkBoxTxt ";
                })
                .text("Display");
}

// function selectOnlyAS(obj){
//     return obj.Type=="AS";
// }
// function selectOnlyMS(obj){
//     return obj.Type=="MT";
// }

///MAIN FUNCTION


    
//now that I have the object for all data
//will show those objects in the space
var w=1000;
var h=500;

console.log(Stations);
// var AidStations = Stations.filter(selectOnlyAS);
AidStations = Stations;
console.log(AidStations);
// AidStations is the array loaded from php (from database)
console.table(AidStations);

    // select input form (doesnt' exist yet)
var AidBoxes = d3.select(".inputform")
    //select all the divs (which don't exist yet)
    .selectAll("div")
    // bind each element of the array to a div (that doesn't exist)
    .data(AidStations)
    // creates as many divs as it needs to match the number of elements in the array
    .enter()
    // FROM HERE ON, EVERYTHING IS REPEATED len(AidStations) TIMES
    // actually put the div in the page
    .append("div")
    // give it attributes, text, anything you want
    //class can be a funciton of the data inside the array
    // d in function(d) is the element in the array
    // i = index
    .attr("class",function(d, i){
        if (d.Type=="AS"){
            return "AidBox";
        }
        else{
            return "MTBox";
        }
    })
    .attr("number",function(d,i){ return +i});
    

var Titles = AidBoxes.append("div")
    .attr("class","Titles")
    .text(function(d){
        if (d.Type=="MT"){
            return d.Location;
        }
        else{
            return d.Location;
        }
    });
    
var CurrentInfo = AidBoxes.append("div")
    .attr("class","CurrentPatients")
    .text(function(d){
       return "Current: "+d.CurrentPatients+" "; 
    });
var CurrentCapacity = AidBoxes.append("div")
    .attr("class","Capacity")
    .text(function(d){
        return "Capacity: "+d.Beds+" ";
    });
    
var Fields = AidBoxes.append("input")
    .attr("class","input_field")
    .attr("type","text")
    .attr("id",function(d){
        if (d.Type=="AS"){ return "AS"+d.Location; }
        else { return "MT"+d.Location; }
    })
    .attr("name",function(d){
        if (d.Type=="AS") {return "AS_Current"+d.Location; }
        else { return "MT_Current"+d.Location; }
    })
    .attr("value",function(d){
        return +d.CurrentPatients;
    });
    
var CumulativePatients = AidBoxes.append("div")
    .attr("class", "CumulativePatients")
    .text(function(d){
        return "Cumulative: " + d.CumulativePatients;
    });
    
var Fields = AidBoxes.append("input")
    .attr("class","input_field")
    .attr("type","text")
    .attr("id",function(d){
        if (d.Type=="AS"){
            return "AS_Cumulative"+d.Location;
        }
        else{
            return "MT_Cumulative"+d.Location;
        }
    })
    .attr("name",function(d){
        if (d.Type=="AS"){
            return "AS_Cumulative"+d.Location;
        }
        else{
            return "MT_Cumulative"+d.Location;
        }
    })
    .attr("value",function(d){
        return +d.CumulativePatients;
    });
    
// var Minuses = AidBoxes.append("div")
//     .attr("class","Minus")
//     .append("div")
//     .attr("class","minusSign Sign")
//     .text("-")
//     .on("click",function(d,i){
//         var myId = "AS"+d.Location;
//         var value = +document.getElementById(myId).value;
//         document.getElementById(myId).value =  +value-1;
//     });


//now put the check-boxes to select status of the aid station
InsertCheckBoxes(0,'open');
InsertCheckBoxes(2,'closed');
InsertDisplay();
/////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////

//submit button

var submit = d3.select("form")
                .append("div")
                .attr("value","Update")
                .attr("class","submit")
                .text("UPDATE")
                .on("click",function(){
                    var form = document.getElementById("inputform");
                    form.submit();
                });
                