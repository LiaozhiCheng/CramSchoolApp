//var ngrok = "http://140.121.197.130:55001/";
var ngrok = "http://127.0.0.1:5000/";
var month = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

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
    
    content += '<ul class="list-unstyled"><li><a href="'+url_cramschool+'">首頁</a></li><li><a href="'+url_cramschool_course+'">課程</a></li><li><a href="'+url_cramschool_staffstudent+'">成員列表</a></li><li><a href="'+url_cramschool_attendence+'">出缺勤</a></li><li><a href="'+url_cramschool_makeup_class+'">補課</a></li><li><a href="'+url_cramschool_classroom+'">教室</a></li></ul>';
    
    obj.innerHTML=content;
    obj.innerHTML += "<footer class='m-3' style='position:fixed; bottom: 0; height: 40px; width:inherit;'>";
     obj.innerHTML += "<a href='/logout' class='m-3' role='button' style='font-size: 20px;'>登出</a>";
     obj.innerHTML += "</footer>";
}
