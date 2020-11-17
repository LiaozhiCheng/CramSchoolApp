window.onload = function init(){
    setSchedule();
    test();
}

//create student information


//create schedule
function setSchedule(){
    var t = document.getElementById("studentschedule").getElementsByTagName("tbody");
    var rows = "";
    var time = [ "上午" , "下午" , "晚上" ];
    for(var i=0; i<3; i++){
        rows += "<tr><td>" + time[i] + "</td>";
        for(var j=0; j<7; j++){
            rows += "<td id='" + i + "-" + j + "'></td>";
        }
        rows += "</tr>"
    }
    t[0].innerHTML = rows;
}

function test(){
    document.getElementById("0-1").innerHTML = "<a href='#' class='normal'>09:00-12:00 國文</a>";
}