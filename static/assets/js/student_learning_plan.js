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
        //url: "testContent/studentPersonalPlan.json",
        url: "https://38049d8c9137.ngrok.io/student/course_personal_plan?course_id=" + courseID,
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            for(var i=0; i<data.length; i++){
                setPlan(setLessonDate(data[i].lesson_time), data[i].progress, data[i].context, setLessonDate(data[i].deadline));
            }
        },
        
        error: function(){
            console.log("getPlan error!!!");
        }
    });
}

//add row to table
function setPlan(date, lesson, plan, deadline){
    var row = "<tr><td>" + date 
            + "</td><td>" + lesson 
            + "</td><td>" + plan 
            + "</td><td>" + deadline + "</td></tr>";
    
    document.getElementById("person-plan").getElementsByTagName("tbody")[0].innerHTML += row;
}














