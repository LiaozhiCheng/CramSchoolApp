function createTable(data) {
    console.log("data: " + data);
    var contentHead = "<tr><th>name</th>";
    var contentBody = "";

    for (var i = 0; i < data.length; i++) {
        var splitDate = data[i].lesson_time.split("-");
        contentHead += "<th>" + splitDate[1] + "/" + splitDate[2] + "</th>";
    }

    for (var i = 0; i < data[0].attendence_list.length; i++) {
        contentBody += "<tr><td>" + data[0].attendence_list[i].student_name + "</td>";
        for (var j = 0; j < data.length; j++) {
            if (data[j].attendence_list[i].state) {
                contentBody += "<td class='attend'>O</td>";
            } else if (data[j].attendence_list[i].state == false) {
                contentBody += "<td class='absent'>X</td>";
            }
        }
    }
    document.getElementById("thead").innerHTML = contentHead;
    document.getElementById("tbody").innerHTML = contentBody;
}

function start() {
    createTable(JSON.parse(sessionStorage.getItem("data")));
}

window.addEventListener("load", start, false);
