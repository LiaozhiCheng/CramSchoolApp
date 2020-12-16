var globalData;

function Click() {
    createTable(globalData, document.getElementById("pick_date").selectedIndex);
}

function createPickDate(data) {
    console.log("data: " + data);
    var content = "";
    var day_list = ["日", "一", "二", "三", "四", "五", "六"];

    for (var i = 0; i < data.length; i++) {
        var date = data[i].lesson_time.replace(/-/g, "/");
        var day = new Date(date).getDay();   //0為星期日，1為星期一以此類推
        if (i == 0) {
            content += "<option selected>" + date + "(" + day_list[day] + ")" + "</option>";
        } else {
            content += "<option>" + date + "(" + day_list[day] + ")" + "</option>";
        }
    }
    document.getElementById("pick_date").innerHTML = content;
}

function createTable(data, date) {
    console.log("data: " + data);
    var content = "";

    for (var i = 0; i < data[date].attendence_list.length; i++) {
        content += "<tr><td>" + data[date].attendence_list[i].student_name + "</td>"
            + "<td>" + data[date].attendence_list[i].email + "</td>"
            + "<td>" + data[date].attendence_list[i].phone + "</td>";
        if (data[date].attendence_list[i].state) {
            content += "<td class='attend'>出席</td>";
        } else if (data[date].attendence_list[i].state == false) {
            content += "<td class='absent'>缺席</td>";
        }
    }
    document.getElementById("tbody").innerHTML = content;
}

function start() {
    globalData = JSON.parse(sessionStorage.getItem("data"));
    console.log(globalData[0]);
    createPickDate(globalData);
    createTable(globalData, 0);
}

window.addEventListener("load", start, false);