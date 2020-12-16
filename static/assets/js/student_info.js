window.onload = function init(){
    setSchedule();
    getSchedule();
    getStudentInfo();
    document.getElementById("page-title").innerHTML = "首頁";
}

//get & set student information
function getStudentInfo(){
    var apiURL = "testContent/studentInfo.json";
    $.ajax({
        //url: apiURL,
        url: "https://38049d8c9137.ngrok.io/user/personal_info",
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


