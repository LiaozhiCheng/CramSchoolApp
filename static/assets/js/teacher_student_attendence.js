function doClick(op) {
    iframe = document.getElementById("iframe");
    if (op == "一天") {
        iframe.setAttribute("src", url_teacher_student_attendenceA);
        day.setAttribute("class", "click");
        semester.setAttribute("class", "attendence");
    } else if (op == "一學期") {
        iframe.setAttribute("src", url_teacher_student_attendenceB);
        day.setAttribute("class", "attendence");
        semester.setAttribute("class", "click");
    }
}

function start() {
    setSideBar()
    var course_id = sessionStorage.getItem("course");
    console.log(course_id);
    if(course_id==null){
                            alert("未知課程，請回課表選擇課程");
                            window.location.replace(url_teacher);
                        }
    $.ajax({

        url: api_course_attendence + course_id, //放你的url，這裡先放本地端檔案
        //url: "https://3aac3445b286.ngrok.io/teacher/course_attendence?course_id=C-001", 之後長這樣
        //student_attendence.json
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',

        //如果成功的話
        success: function (data) {//這裡拿到的data是一個Object陣列
            console.log("success");//看到時候有沒有成功
            console.log(data);
            sessionStorage.setItem("data", JSON.stringify(data));
            document.getElementById("iframeDiv").innerHTML = "<iframe id='iframe' src='/teacher_student_attendenceA' width='100%' height='600' overflow='scroll'></iframe>";
        },

        //如果失敗的話
        error: function () {
            console.log("error");
        }
    });
}

window.addEventListener("load", start, false);
