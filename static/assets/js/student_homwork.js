window.onload = function init(){
    //courseID & name
    getSavedData();
    
    //set page title
    document.getElementById("page-title").innerHTML = courseName + "-課程作業";
    
    //set homework table
    getStudentHW();
}


//getHW
function getStudentHW(){
    $.ajax({
        url: "testContent/studentHW.json",
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            for(var i=0; i<data.length; i++){
                setHW(data[i].time, data[i].lesson, data[i].homework, data[i].deadline);
            }
        },
        
        error: function(){
            console.log("getHW error!!!");
        }
    });
}


//setHW
function setHW(time, lesson, homework, deadline){
    var row = "<tr><td>" + time + 
            "</td><td>" + lesson + 
            "</td><td>" + homework + 
            "</td><td>" + deadline + 
            "</td></tr>";
    document.getElementById("homeworks").getElementsByTagName("tbody")[0].innerHTML += row;
}



