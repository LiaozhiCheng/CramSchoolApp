//設定所有與補課相關的資訊
//該學生可補課的選項會load在此
var missedCourse = new Array();
var missedLesson = new Array();
var missedLessonID = new Array();


//get student missed lesson
function getMissedLesson(){
    $.ajax({
        url: api_student_missed_lesson,
        //url: "https://38049d8c9137.ngrok.io/student/miss_lesson",
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            console.log(data);
            for(var i=0; i<data.length; i++){
                missedCourse.push(data[i].course_name);
                missedLesson[i] = new Array();
                missedLessonID[i] = new Array();
                for(var j=0; j<data[i].miss_lessons.length; j++){
                    missedLesson[i].push(data[i].miss_lessons[j].progress);
                    missedLessonID[i].push(data[i].miss_lessons[j].lesson_id);
                }
            }
            console.log(missedLessonID);
            setReserveModal();
        },
        
        error: function(){
            console.log("getMissedLesson error!!!");
        }
    });
}

//reserve modal: chooseCourse option
function setReserveModal() {
    var ops = "<option value='' disabled selected>選擇課程</option>";
    for (var i in missedCourse){
        ops += "<option value='" + i + "'>" + missedCourse[i] + "</option>";
    }
    document.getElementById("chooseCourse").innerHTML = ops;
}

//reserve modal: chooseLesson option
function setLesson(ch){
    var index = parseInt(ch.selectedIndex);
    var t = document.getElementById("chooseLesson");
    var ops = "<option value='' disabled selected>選擇課堂</option>";
    for(var i in missedLesson[index-1]){
        var info = "";
        if(missedLesson[index-1][i].length > 0){
            info = missedLesson[index-1][i];
        }
        else{
            info = missedLessonID[index-1][i];
        }
        
        ops += "<option value='" + i + "'>" + info + "</option>";
    }
    t.innerHTML = ops;
}

//reset reserve modal
function resetReserve(){
    setReserveModal();
    document.getElementById("chooseLesson").innerHTML = "";
}

//set checkout info
function setCheckInfo(info){
    console.log(info.text);
    var list = info.text.split('/');
    document.getElementById("courseInfo").placeholder = list[0]; document.getElementById("lessonInfo").placeholder = list[1];
    currID = info.name;
}