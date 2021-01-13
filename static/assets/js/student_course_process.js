window.onload = function init(){
    //courseID & name
    getSavedData();
    
    //set sidebar
    setSideBar("all");
    
    //set page title
    document.getElementById("page-title").innerHTML = "課程進度";
    
    //set course information
    getCourseInfo();
    
    //set course progress
    getLessonInfo();
}

//get course information
function getCourseInfo(){
    $.ajax({
        url: api_student_course_info + courseID,
        //url: "https://38049d8c9137.ngrok.io/user/course_info?course_id=" + courseID,
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            var content = "<h5 class='card-title'>" + data.course + 
                        "</h5><h7 class='card-subtitle'>授課教師：" + data.teacher + 
                        "</h7><p class='card-text'>課程簡介：<br>" + data.summary + 
                        "</p><h7 class='card-subtitle'>教室：" + data.classroom + 
                        "<h7>";
            document.getElementById("course-info").innerHTML = content;
        },
        
        error: function(){
            console.log("getCourseInfo error!!!");
        }
    });
}


//get lessons data
function getLessonInfo(){
    $.ajax({
        url: api_student_course_progress + courseID,
        //url: "https://38049d8c9137.ngrok.io/student/course_progress?course_id=" + courseID,
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            for(var i=0; i<data.length; i++){
                var time = setLessonDate(data[i].lesson_time);
                setLessonInfo(time, data[i].progress);
            }
        },
        
        error: function(){
            console.log("getCourseInfo error!!");
        }
        
    });
}

//set lessons table
function setLessonInfo(time, progress){
    //testing();
    var row = "<tr><td>" + time + "</td><td>" + progress + "</td></tr>";
    document.getElementById("lessons").getElementsByTagName("tbody")[0].innerHTML += row;
}















