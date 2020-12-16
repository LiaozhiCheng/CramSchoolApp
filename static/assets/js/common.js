var ngrok = "";

//web url
var url_cramschool = "/cramschool";
var url_cramschool_course = "/cramschool_course";
var url_cramschool_staffstudent = "/cramschool_staffstudent";
var url_cramschool_attendence = "/cramschool_attendence";
var url_cramschool_makeup_class = "/cramschool_makeup_class";
var url_cramschool_classroom = "/cramschool_classroom";

function setSideBar(){
    var obj = document.getElementById("sidebar");
    var content="";
    content += '<div id="dismiss"><i class="fas fa-arrow-left"></i></div><div class="sidebar-header"><h3>CS管理系統</h3></div>';
    
    content += '<ul class="list-unstyled"><li><a href="cramschool_finish.html">首頁</a></li><li><a href="cramschool_course_finish.html">課程</a></li><li><a href="cramschool_staffstudent_finish.html">成員列表</a></li><li><a href="cramschool_attendence_finish.html">出缺勤</a></li><li><a href="cramschool_makeup_class_finish.html">補課</a></li><li><a href="cramschool_classroom_finish.html">教室</a></li></ul>';
    
    obj.innerHTML=content;
}