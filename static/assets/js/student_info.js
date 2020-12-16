window.onload = function init(){
    //set sidebar
    setSideBar("main");
    
    //set schedule
    setSchedule();
    getSchedule();
    
    //set student info
    getStudentInfo();
    
    //set page title
    document.getElementById("page-title").innerHTML = "首頁";
}

//get & set student information
function getStudentInfo(){
    $.ajax({
        url: api_student_personal_info,
        //url: "https://38049d8c9137.ngrok.io/user/personal_info",
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            var studentInfo = "<h5 class='card-title'>" + data.name + 
                            "</h5><p class='card-text'>學生號碼：" + data.user_id + 
                            "<br>聯絡電話：" + data.phone +
                            "<br>email：" + data.email + "</p>";
            document.getElementById("st-info").innerHTML = studentInfo;
        },
        
        error: function(){
            console.log("getStudentInfo error!!");
        }
        
    });
}


