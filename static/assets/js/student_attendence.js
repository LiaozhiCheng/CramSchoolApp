window.onload = function init(){
    //courseID & name
    getSavedData();
    
    //set nav title
    document.getElementById("page-title").innerHTML = courseName + "-出缺勤紀錄";
    
    //set table
    getAttendency();
}

//get attendence data from db
function getAttendency(){
    //load json
    $.ajax({
        url: "testContent/studentAttendence.json",
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            for(var i=0; i<data.length; i++){
                setAttendenceState(data[i].time, data[i].lesson, data[i].state);
            }
        },
        
        error: function(){
            console.log("getAttendence error!!!");
        }
        
    });
}

//set attendence table state
function setAttendenceState(time, lesson, state){
    var row = "<tr><td>" + time + "</td><td>" + lesson + "</td>";
    if(state){
        row += "<td class='text-success'>出席</td>";
    }
    else{
        row += "<td class='text-danger'>缺席</td>";
    }
    
    document.getElementById("student-attend").getElementsByTagName("tbody")[0].innerHTML += row;
}
