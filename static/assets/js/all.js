	var ngrok = "http://140.121.197.130:55001";
	var api_schedule = ngrok + "/schedule";
	var api_personal_info = ngrok + "/personal_info";
	var api_course_info = ngrok + "/course_info?course_id=";
	var api_communication_book = ngrok + "/teacher_course_communication_book?course_id=";
	var api_edit_communication_book = ngrok + "/teacher_edit_course_communication_book";
	var api_delete_communication_book = ngrok + "/teacher_delete_course_communication_book?lesson_id=";
	var api_student_personal_info = ngrok + "/teacher_student_personal_info?student_id=";
	var api_personal_plan = ngrok + "/teacher_course_personal_plan?student_id=";
	var api_add_personal_plan = ngrok + "/teacher_no_plan_lesson_time?student_id=";
	var api_edit_personal_plan = ngrok + "/teacher_edit_course_personal_plan";
	var api_delete_personal_plan = ngrok + "/teacher_delete_course_personal_plan";
	var api_course_student_list = ngrok + "/teacher_course_student_list?course_id=";
	var api_course_attendence = ngrok + "/teacher_course_attendence?course_id=";
	var api_course_grade = ngrok + "/teacher_course_grade?course_id=";
	var api_edit_course_grade = ngrok + "/teacher_edit_course_grade";
	var api_delete_course_grade = ngrok + "/teacher_delete_course_grade?lesson_id=";

	var url_teacher = "/teacher";
	var url_teacher_class_student = "/teacher_class_student";
	var url_teacher_communication_book = "/teacher_communication_book";
	var url_teacher_courseinfo = "/teacher_courseinfo";
	var url_teacher_homework = "/teacher_homework";
	var url_teacher_grade = "/teacher_grade";
	var url_teacher_personal_plan = "/teacher_personal_plan";
	var url_teacher_student_attendence = "/teacher_student_attendence";
	var url_teacher_student_attendenceA = "/teacher_student_attendenceA";
	var url_teacher_student_attendenceB = "/teacher_student_attendenceB";


	function setSideBar(){
		var obj = document.getElementById("sidebar");
		obj.innerHTML = "<div id='dismiss'><i class='fas fa-arrow-left'></i></div><div class='sidebar-header'><h3>CS管理系統</h3></div><ul class='list-unstyled'><li class='active'><a href='"+url_teacher+"'>首頁</a></li><li><a href='"+url_teacher_courseinfo+"'>課程資訊</a></li><li><a href='"+url_teacher_class_student+"'>學生</a></li><li><a href='"+url_teacher_grade+"'>成績</a></li><li><a href='"+url_teacher_student_attendence+"'>出缺勤</a></li><li><a href='"+url_teacher_communication_book+"'>聯絡簿</a></li></ul><footer class='m-3' style='position:fixed; bottom: 0; height: 40px; width:inherit;'><a href='/logout' class='m-3' role='button' style='font-size: 20px;'>登出</a></footer>"
	}
