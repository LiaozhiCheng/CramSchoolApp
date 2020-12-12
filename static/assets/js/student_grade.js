window.onload = function init(){
    //courseID & name
    getSavedData();
    
    //set page title
    document.getElementById("page-title").innerHTML = courseName + "-考試成績";
    
    //grade table
    getGrade();
}


//get student grades
function getGrade(){
    $.ajax({
        url: "testContent/studentGrade.json",
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            for(var i=0; i<data.length; i++){
                setGrade(data[i].time, data[i].quiz_name, data[i].grade);
            }
        },
        
        error: function(){
            console.log("getGrade error!!!");
        }
    });
}

//set student grades
function setGrade(time, quiz, grade){
    var row = "<tr><td>" + time + "</td><td>" + quiz + "</td><td>" + grade + "</td></tr>";
    
    document.getElementById("grade").getElementsByTagName("tbody")[0].innerHTML += row;
}
