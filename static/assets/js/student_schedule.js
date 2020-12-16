//get schedule data
function getSchedule(){
    $.ajax({
        url: "/schedule",
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            for(var i=0; i<data.length; i++){
                addCourse(data[i].course, data[i].time, data[i].course_id);
            }
        },
        
        error: function(){
            console.log("getSchedule error");
        }
    });
}

//create schedule
function setSchedule(){
    var t = document.getElementById("studentschedule").getElementsByTagName("tbody");
    var rows = "";
    for(var i=1; i<=3; i++){
        rows += "<tr><td>" + time[i-1] + "</td>";
        for(var j=0; j<7; j++){
            rows += "<td id='" + i + "-" + days[j] + "'></td>";
        }
        rows += "</tr>"
    }
    t[0].innerHTML = rows;
}

//add course to table
function addCourse(course, time, id){
    //setup time
    var temp = time.split("-");
    temp = temp[0].split("~");
    temp = temp[1].split(":");
    var idx = defTime(temp[0]) + '-' + days[time.split("-")[1]-1];
    document.getElementById(idx).innerHTML += "<a href='student_course_process.html'  id='" + id + "' class='normal' onclick='setCourseID(this)'>"+ time.split("-")[0] + "<br>" + course + "</a>";
}

//when does the course take
function defTime(time){
    if(time<=12){ return 1; }
    else if( time>12 && time<=18 ){ return 2; }
    else{ return 3; }
}












