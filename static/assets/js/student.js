var days = [ "mon" , "tue" , "wed" , "thr" , "fri" , "sat" , "sun" ];

var time = [ "上午" , "下午" , "晚上" ];

var rescheduleTime = [ "PM5~PM7" , "PM7~PM9" , "PM9~PM11" ];

var courseID;

var courseName;

//api url
var api_student_schedule = "/schedule";
var api_student_personal_info = "/personal_info";
var api_student_course_info = "/course_info?course_id=";
var api_student_reschedule_list = "/student_reschedule_list";
var api_student_missed_lesson = "/student_miss_lesson";
var api_student_add_reservation = "/student_add_reservation";
var api_student_cancel_reservation = "/student_cancel_reservation";
var api_student_course_progress = "/student_course_progress?course_id=";
var api_student_course_hw = "/student_course_homework?course_id=";
var api_student_course_grade = "/student_course_grade?course_id=";
var api_student_course_attendence = "/student_course_attendence?course_id=";
var api_student_course_personal_plan = "/student_course_personal_plan?course_id=";

//web url
var url_student = "student/student";
var url_student_attendence = "student/student_attendence";
var url_student_course_process = "student/student_course_process";
var url_student_grade = "student/student_grade";
var url_student_homework = "student/student_homework";
var url_student_learning_plan = "student/student_learning_plan";
var url_student_lesson_makeup = "student/student_lesson_makeup";


function setCourseID(obj){
    var word = obj.innerHTML.split('<br>');
    var info = [ obj.id, word[1] ];
    sessionStorage.setItem("course", info);
}

//set lessons date
function setLessonDate(str){
    var time = str.split(' ');
    return time[3] + '-' + time[2] + '-' + time[1];
}

function getSavedData(){
    try{
        var temp = sessionStorage.getItem('course').split(',');
        courseID = temp[0];
        courseName = temp[1];
    }
    catch(e){
        alert("未知課程，請回課表選擇課程");
        window.location.replace("student.html");
    }
    
}


