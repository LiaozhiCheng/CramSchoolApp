var currID = "";

//set current choosed cell
function setCurr(theCell){
    //紀錄目前選擇的時間段
    currID = theCell.name;
    console.log(currID);
}

//send reservation to db
function sendReservation(courseName, lessonId){
    var myTime = new Date();
    var reservation = { "datetime" : myTime , "course_name" : courseName , "lesson_id" : lessonId };
    
    $.ajax({
        url: "/student_add_reservation",
        type: "POST",
        data: JSON.stringify(reservation),
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            alert("send success!");
            console.log(data);
        },
        
        error: function(){
            alert("send error!!!");
        }
    });
}

//get reservation from form
function getReservation(){
    
    //取得目標課程&課堂的index
    var courseIdx = document.getElementById("chooseCourse").selectedIndex;
    var lessonIdx = document.getElementById("chooseLesson").selectedIndex;
    
    //判斷是否都已選擇
    //未完成選擇，發出提醒
    if(courseIdx=='' || lessonIdx==''){
        alert("請選擇課程/課堂");
    }
    //完成選擇，傳送資料
    else{
        sendReservation(missedCourse[courseIdx-1], missedLessonID[courseIdx-1][lessonIdx]);
        var C_Name = document.getElementById("chooseCourse")[courseIdx].text;
        var L_Name = document.getElementById("chooseLesson")[lessonIdx].text;
        
        reservedTd(currID, C_Name, L_Name);
        currID = "";
    }
}

//cancel reservation
function cancelReservation(){
    console.log("target: " + currID + "呼叫刪除補課API");
    
    //double check alert;
    
    //create delete data
    var cancelData = {};
    
    //call delete API
    $.ajax({
        url: "",
        type: "POST",
        data: JSON.stringify(cancelData),
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(){
            console.log("cancel successfully!!!");
        },
        
        error: function(){
            console.log("cancel error!!!");
        }
    });
    
    //
    resetTd(currID);
    
    setTimeout(function(){
        window.location.reload();
    }, 3000);
    
}




