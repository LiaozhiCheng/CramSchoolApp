var days = [ "mon" , "tue" , "wed" , "thr" , "fri" , "sat" , "sun" ];

var time = [ "上午" , "下午" , "晚上" ];

var rescheduleTime = [ "PM5~PM7" , "PM7~PM9" , "PM9~PM11" ];

var courseID;

var courseName;


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


