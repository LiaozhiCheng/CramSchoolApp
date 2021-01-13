window.onload = function init(){
    //courseID & name
    getSavedData();
    
    //set sidebar
    setSideBar("all");
    
    //set page title
    document.getElementById("page-title").innerHTML = courseName + "-考試成績";
    
    //grade table
    getGrade();
}


//get student grades
function getGrade(){
    $.ajax({
        url: api_student_course_grade + courseID,
        //url: "https://38049d8c9137.ngrok.io/student/course_grade?course_id=" + courseID,
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
			console.log(data);
            for(var i=0; i<data.length; i++){
                setGrade(setLessonDate(data[i].quiz_date), data[i].quiz_name, data[i].grade);
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
