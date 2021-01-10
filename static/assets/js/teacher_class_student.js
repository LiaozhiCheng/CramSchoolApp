var globalData;

function Click(id) {
    sessionStorage.setItem("studentId", globalData[id].student_id);
}

function createTable(data) {
    console.log("data: " + data);
    var content = "";

    for (var i = 0; i < data.length; i++) {
        content += "<tr><td><a href='"+url_teacher_personal_plan+"' onclick='Click(" + i + ")'>" + data[i].student_name + "</a></td>"
            + "<td>" + data[i].student_id + "</td>"
            + "<td>" + data[i].email + "</td>"
            + "<td>" + data[i].phone + "</td>"
    }
    document.getElementById("tbody").innerHTML = content;
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
        url: api_course_student_list + course_id, //放你的url，這裡先放本地端檔案
        //url: "https://38049d8c9137.ngrok.io/teacher/course_student_list?course_id=C-001", 之後長這樣
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',

        //如果成功的話
        success: function (data) {//這裡拿到的data是一個Object陣列
            console.log("success");//看到時候有沒有成功

            globalData = data;
            createTable(data);
            console.log(data);
            for (var i = 0; i < data.length; i++) {
                //利用key去找value
                console.log("student_name: " + data[i].student_name);
                console.log("student_id: " + data[i].student_id);
                console.log("email: " + data[i].email);
                console.log("phone: " + data[i].phone);
            }
        },

        //如果失敗的話
        error: function () {
            console.log("error");
        }
    });
}

window.addEventListener("load", start, false);
