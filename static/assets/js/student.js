var days = [ "mon" , "tue" , "wed" , "thr" , "fri" , "sat" , "sun" ];

var time = [ "上午" , "下午" , "晚上" ];

var rescheduleTime = [ "PM5~PM7" , "PM7~PM9" , "PM9~PM11" ];

var courseID;

var courseName;

var ngrok = "";

//api url
var api_student_schedule = ngrok + "/schedule";
var api_student_personal_info = ngrok + "/personal_info";
var api_student_course_info = ngrok + "/course_info?course_id=";
var api_student_reschedule_list = ngrok + "/student_reschedule_list";
var api_student_missed_lesson = ngrok + "/student_miss_lesson";
var api_student_add_reservation = ngrok + "/student_add_reservation";
var api_student_cancel_reservation = ngrok + "/student_cancel_reservation";
var api_student_course_progress = ngrok + "/student_course_progress?course_id=";
var api_student_course_hw = ngrok + "/student_course_homework?course_id=";
var api_student_course_grade = ngrok + "/student_course_grade?course_id=";
var api_student_course_attendence = ngrok + "/student_course_attendence?course_id=";
var api_student_course_personal_plan = ngrok + "/student_course_personal_plan?course_id=";

//web url
var url_student = "student";
var url_student_attendence = "student_attendence";
var url_student_course_process = "student_course_process";
var url_student_grade = "student_grade";
var url_student_homework = "student_homework";
var url_student_learning_plan = "student_learning_plan";
var url_student_lesson_makeup = "student_lesson_makeup";


//<div id='dismiss'><i class='fas fa-arrow-left'></i></div>
function setSideBar(version){
    var obj = document.getElementById("sidebar");
    if(version == "main"){
        obj.innerHTML = "<div id='dismiss'><i class='fas fa-arrow-left'></i></div>" + 
                        "<div class='sidebar-header'><h3>CS管理系統</h3></div>" + 
                        "<ul class='list-unstyled'><li class='active'><a href='" + url_student +
                        "'>首頁</a></li><li><a href='" + url_student_lesson_makeup + 
                        "'>預約補課</a></li></ul>";
    }
    else if(version == "makeup"){
        obj.innerHTML = "<div id='dismiss'><i class='fas fa-arrow-left'></i></div>" + 
                        "<div class='sidebar-header'><h3>CS管理系統</h3></div>" + 
                        "<ul class='list-unstyled'><li><a href='" + url_student +
                        "'>首頁</a></li><li class='active'><a href='" + url_student_lesson_makeup + 
                        "'>預約補課</a></li></ul>";
    }
    else{
        obj.innerHTML = "<div id='dismiss'><i class='fas fa-arrow-left'></i></div>" + 
                        "<div class='sidebar-header'><h3>CS管理系統</h3></div>" + 
                        "<ul class='list-unstyled'><li><a href='" + url_student +
                        "'>首頁</a></li><li><a href='" + url_student_lesson_makeup + 
                        "'>預約補課</a></li><li class='active'><a href='#pageSubmenu' data-toggle='collapse' aria-expanded='false'>課程相關項目</a>" + 
                        "<ul class='list-unstyled' id='pageSubmenu'><li><a href='" + url_student_course_process +
                        "'>課程進度</a></li><li><a href='" + url_student_homework + 
                        "'>課程作業</a></li><li><a href='" + url_student_grade + 
                        "'>考試成績</a></li><li><a href='" + url_student_attendence +
                        "'>出缺勤紀錄</a></li><li><a href='" + url_student_learning_plan + 
                        "'>個人計畫</a></li></ul></li></ul>";
    }
}



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
        window.location.replace(url_student);
		//window.location.href = url_student;
    }
    
}


