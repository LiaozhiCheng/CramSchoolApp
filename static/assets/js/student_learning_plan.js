window.onload = function(){
    //courseID & name
    getSavedData();
    
    //set page title
    document.getElementById("page-title").innerHTML = courseName + "-個人計畫";
    
    //personal plan
    getPlan();
}

//get person's plan for db
function getPlan(){
    $.ajax({
        url: "testContent/studentPersonalPlan.json",
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            for(var i=0; i<data.length; i++){
                setPlan(data[i].time, data[i].lesson, data[i].personal_plan);
            }
        },
        
        error: function(){
            console.log("getPlan error!!!");
        }
    });
}

//add row to table
function setPlan(date, lesson, plan){
    var row = "<tr><td>" + date 
            + "</td><td>" + lesson 
            + "</td><td>" + plan + "</td></tr>";
    
    document.getElementById("person-plan").getElementsByTagName("tbody")[0].innerHTML += row;
}














