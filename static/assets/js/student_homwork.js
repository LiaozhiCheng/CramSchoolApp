window.onload = function init(){
    //courseID & name
    getSavedData();
    
    //set sidebar
    setSideBar("all");
    
    //set page title
    document.getElementById("page-title").innerHTML = courseName + "-課程作業";
    
    //set homework table
    getStudentHW();
}


//getHW
function getStudentHW(){
    $.ajax({
        url: api_student_course_hw + courseID,
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            for(var i=0; i<data.length; i++){
				if(data[i].deadline != null){
					var deadline = setLessonDate(data[i].deadline);
				}
				else{
					var deadline = "";
				}
                var startTime = setLessonDate(data[i].lesson_time);
                setHW(startTime, data[i].progress, data[i].homework, deadline);
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



