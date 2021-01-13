var globalData;

function uploadData(grade_no) {
    var data = JSON.stringify(globalData[grade_no]);
    $.ajax({
        url: api_edit_course_grade,   //後端的URL
        type: "POST",   //用POST的方式
        dataType: "json",   //response的資料格式
        contentType: 'application/json; charset=utf-8',
        data: data, //傳送給後端的資料
        success: function (data) {
            console.log(data);  //成功後回傳的資料
        },

        //如果失敗的話
        error: function () {
            console.log("error");
        }
    });
}

function deleteGrade(grade_no) {
    $.ajax({
        url: api_delete_course_grade + globalData[grade_no].lesson_id, //放你的url，這裡先放本地端檔案
        //url: "grade.json", 之後長這樣
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',

        //如果成功的話
        success: function (data) {//這裡拿到的data是一個Object陣列
            console.log(data);//看到時候有沒有成功

            globalData[grade_no].grade_list = data.grade_list;
            createTable(globalData);
        },

        //如果失敗的話
        error: function () {
            console.log("error");
        }
    });
}

function saveGrade(grade_no) {
    if(document.getElementById("testname" + grade_no).value==""){
        window.alert("考試範圍輸入錯誤");
        createTable(globalData);
        return;
    }
    globalData[grade_no].quiz_name = document.getElementById("testname" + grade_no).value;
    document.getElementById("testname" + grade_no).disabled = true;
    document.getElementById("testname" + grade_no).setAttribute("class", "gradeTestNameDisabled");
    document.getElementById("button" + String(grade_no)).innerHTML = "<button type='button' class='btn btn-outline-info' onclick='editGrade(" + grade_no + ")'>edit button</button>";
    for (var i = 0; i < globalData[grade_no].grade_list.length; i++) {
        if(document.getElementById("row" + String(i) + "col" + String(grade_no)).value == ""){
            globalData[grade_no].grade_list[i].student_grade = null;
        }else{
            globalData[grade_no].grade_list[i].student_grade = parseInt(document.getElementById("row" + String(i) + "col" + String(grade_no)).value);
        }
        document.getElementById("row" + String(i) + "col" + String(grade_no)).disabled = true;
        document.getElementById("row" + String(i) + "col" + String(grade_no)).setAttribute("class", "gradeTextDisabled");
    }
    uploadData(grade_no);
}

function editGrade(grade_no) {
    document.getElementById("testname" + grade_no).disabled = false;
    document.getElementById("testname" + grade_no).setAttribute("class", "gradeTestName");
    document.getElementById("button" + String(grade_no)).innerHTML = "<div align='left' style='float:left'><button type='button' class='btn btn-outline-success' onclick='saveGrade(" + grade_no + ")'>save</button></div>"
        + "<div align='right'><button type='button' class='btn btn-outline-danger' onclick='deleteGrade(" + grade_no + ")'>delete</button></div>";
    for (var i = 0; i < globalData[grade_no].grade_list.length; i++) {
        document.getElementById("row" + String(i) + "col" + String(grade_no)).disabled = false;
        document.getElementById("row" + String(i) + "col" + String(grade_no)).setAttribute("class", "gradeText");
    }
}

function showDate() {
    var rangeData = []
    var contentHead = "<tr><th>name</th>";
    var contentBody = "";
    var minDate = document.getElementById("date1").value;
    var maxDate = document.getElementById("date2").value;

    if(minDate!="" && maxDate!="" && minDate > maxDate){
        window.alert("日期輸入錯誤")
        return;
    }

    for (var i = 0; i < globalData.length; i++) {
        var compare = new Date(globalData[i].lesson_time.replace(/-/g, "/"));
        if (minDate != "") {
            var min = new Date(minDate.replace(/-/g, "/"));
            if (compare < min) {
                continue;
            }
        }

        if (maxDate != "") {
            var max = new Date(maxDate.replace(/-/g, "/"));
            if (compare > max) {
                continue;
            }
        }

        var splitDate = globalData[i].lesson_time.split("-");
        contentHead += "<th>" + splitDate[1] + "/" + splitDate[2]
                 + "<br><input id=testname" + String(i) + " class='gradeTestNameDisabled' type='text' placeholder='' value=" + globalData[i].quiz_name
                 + " disabled><br><div id=button" + i + "><button type='button' class='btn btn-outline-info' onclick='editGrade(" + i + ")'>edit button</button></div></th>";
        rangeData.push(i);
    }

    for (var i = 0; i < globalData[0].grade_list.length; i++) {
        contentBody += "<tr><td>" + globalData[0].grade_list[i].student_name + "</td>";
        for (var j = 0; j < rangeData.length; j++) {
            if (globalData[j].grade_list[i].student_grade == null) {
                contentBody += "<td><input id=row" + String(i) + "col" + String(rangeData[j]) + " class='gradeTextDisabled' type='text' placeholder='' value='' disabled></td>";
            } else {
                contentBody += "<td><input id=row" + String(i) + "col" + String(rangeData[j]) + " class='gradeTextDisabled' type='text' placeholder='' value=" + globalData[rangeData[j]].grade_list[i].student_grade + " disabled></td>";
            }

        }
    }
    document.getElementById("thead").innerHTML = contentHead;
    document.getElementById("tbody").innerHTML = contentBody;
}

function createTable(data) {
    var contentHead = "<tr><th>name</th>";
    var contentBody = "";

    for (var i = 0; i < data.length; i++) {
        var splitDate = data[i].lesson_time.split("-");
        contentHead += "<th>" + splitDate[1] + "/" + splitDate[2]
                 + "<br><input id=testname" + String(i) + " class='gradeTestNameDisabled' type='text' placeholder='' value=" + data[i].quiz_name
                 + " disabled><br><div id=button" + i + "><button type='button' class='btn btn-outline-info' onclick='editGrade(" + i + ")'>edit button</button></div></th>";
    }

    for (var i = 0; i < data[0].grade_list.length; i++) {
        contentBody += "<tr><td>" + data[0].grade_list[i].student_name + "</td>";
        for (var j = 0; j < data.length; j++) {
            if (data[j].grade_list[i].student_grade == null ) {
                contentBody += "<td><input id=row" + String(i) + "col" + String(j) + " class='gradeTextDisabled' type='text' placeholder='' value='' disabled></td>";
            } else {
                contentBody += "<td><input id=row" + String(i) + "col" + String(j) + " class='gradeTextDisabled' type='text' placeholder='' value=" + data[j].grade_list[i].student_grade + " disabled></td>";
            }
        }
    }


    document.getElementById("thead").innerHTML = contentHead;
    console.log(document.getElementById("testname1"));
    document.getElementById("tbody").innerHTML = contentBody;
}

function start() {
    setSideBar()
    var course_id = sessionStorage.getItem("course");
    console.log(course_id);
    $.ajax({
        url: api_course_grade + course_id, //放你的url，這裡先放本地端檔案
        //url: "grade.json", 之後長這樣
        //api_course_grade + course_id
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',

        //如果成功的話
        success: function (data) {//這裡拿到的data是一個Object陣列
            console.log("success");//看到時候有沒有成功
            console.log(data);
            globalData = data;
            createTable(data);
        },

        //如果失敗的話
        error: function () {
            console.log("error");
        }
    });
}

window.addEventListener("load", start, false);
