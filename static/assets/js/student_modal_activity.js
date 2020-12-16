var currID = "";

//set current choosed cell
function setCurr(theCell){
    //紀錄目前選擇的時間段
    currID = theCell.name;
}

function setTimeData(currID){
    var tempTime = currID.split("+");
    var weekDay = tempTime[0].split('-');
    var index = days.indexOf(weekDay[0]);
    if(index == 6){ index = 0; }
    else{ index += 1; }
    
    var time = parseInt(weekDay[1]);
    if(time == 0){ time = 17; }
    else if(time == 1){ time = 19; }
    else{ time = 21; }
    
    return tempTime[1] + '+' + index + '-' + time;
}

//send reservation to db
function sendReservation(courseName, lessonId){
    var myTime = setTimeData(currID);
    var reservation = { "datetime" : myTime , "course_name" : courseName , "lesson_id" : lessonId };
    console.log(lessonId);
    $.ajax({
        url: api_student_add_reservation,
        //url: "https://38049d8c9137.ngrok.io/student/add_reservation",
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
        var l_id = missedLessonID[missedCourse.indexOf(C_Name)][missedLesson[missedCourse.indexOf(C_Name)].indexOf(L_Name)];
        reservedTd(currID.split('+')[0], C_Name, L_Name, l_id, currID.split('+')[1]);
        currID = "";
    }
}

//cancel reservation
function cancelReservation(){
    console.log("target: " + currID + "呼叫刪除補課API");
    
    //double check alert;
    
    //create delete data
    var myTime = setTimeData(currID);
    var C_Name = document.getElementById("chooseCourse")[courseIdx].text;
    var L_Name = document.getElementById("chooseLesson")[lessonIdx].text;
    var l_id = missedLessonID[missedCourse.indexOf(C_Name)][missedLesson[missedCourse.indexOf(C_Name)].indexOf(L_Name)];
    var cancelData = { "datetime" : myTime , "course_name" : C_Name , "lesson_id" : l_id };
    
    //call delete API
    $.ajax({
        url: api_student_cancel_reservation,
        //url: "https://38049d8c9137.ngrok.io/student/cancel_reservation",
        type: "POST",
        data: JSON.stringify(cancelData),
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            console.log(data);
            alert("cancel successfully!!!");
        },
        
        error: function(){
            console.log("cancel error!!!");
        }
    });
    
    //
    resetTd(currID.split('+')[0], "");
    
//    setTimeout(function(){
//        window.location.reload();
//    }, 3000);
    
}




