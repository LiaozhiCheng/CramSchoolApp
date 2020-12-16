window.onload = function init() {
    //get student's missed lessons
    getMissedLesson();
    
    //set sidebar
    setSideBar("makeup");
    
    //set page title
    document.getElementById("page-title").innerHTML = "預約補課";
    
    //get opened time for 
    getValidTime();
    
    //set valid reserve time
    setTable();
    setReserveModal();
    $("#reserve").on('hidden.bs.modal', function(){
        resetReserve();
    });
    
    
}

//設定與習班已開放的補課時間資訊

//set time table
function setTable(){
    //取得table物件
    var t = document.getElementById("valid_time").getElementsByTagName("tbody")[0];
    var rows = "";
    
    //create new rows
    //給每個欄位特定的ID
    for(var i=0; i<rescheduleTime.length; i++){
        rows += "<tr><td>" + rescheduleTime[i] + "</td>";
        for(var j=0; j<days.length; j++){
            rows += "<td id='" + days[j] + "-" + i +"'></td>";
        }
        rows += "</tr>";
    }
    
    t.innerHTML = rows;
}

//get time Range
function getTimeRange(time){
    var tempTime = time.split('-');
    var hour = parseInt(tempTime[1]);
    var weekDay = parseInt(tempTime[0]);
    if(weekDay == 0){ weekDay = 7; }
    
    var td_id = "";
    if(hour == 17){
        td_id = days[weekDay-1] + '-0';
    }
    else if(hour == 19){
        td_id = days[weekDay-1] + '-1';
    }
    else if(hour == 21){
        td_id = days[weekDay-1] + '-2';
    }
    return td_id;
}

//get available time
function getValidTime(){
    $.ajax({
        url: api_student_reschedule_list,
        //url: "https://38049d8c9137.ngrok.io/student/reschedule_list",
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            console.log("getVaildTime: ", data);
            for(var i=0; i<data.length; i++){
                var time = data[i].datetime.split('+');
                var td_id = getTimeRange(time[1]);
                switch(data[i].state){
                    case 'available':
                        resetTd(td_id, time[0]);
                        break;
                    case 'full':
                        fullTd(td_id, time[0]);
                        break;
                    case 'reserved':
                        reservedTd(td_id, data[i].course_name, data[i].lesson_progress, data[i].lesson_id, time[0]);
                }
            }
        },
        
        error: function(){
            console.log("getValidTime error!!!!!!");
        }
        
    });
}

//set to unreserve state
function resetTd(td_id, date){
    var target = document.getElementById(td_id);
    var str = "<a href='#' class='normal' name='" + td_id + "+" + date + "' " 
            + "data-toggle='modal' data-target='#reserve' " 
            + "onclick='setCurr(this)'>預約補課</a>";
    target.innerHTML = str;
}

//set to full state
function fullTd(td_id, date){
    var target = document.getElementById(td_id);
    var str = "<a href='#' class='disabled' name='" + td_id + '+' + date
            + "'>預約已滿</a>";
    target.innerHTML = str;
}

//set to reserved state
function reservedTd(td_id, c_name, l_name, l_id, date){
    var target = document.getElementById(td_id);
    var display = l_name;
    if(l_name === undefined){ display = l_id; }
    var str = "<a href='#' class='normal' name='" + td_id + '+' + date + "' " 
            + "data-toggle='modal' data-target='#checkoutInfo' " 
            + "onclick='setCheckInfo(this)' id='" + l_id + "'>" 
            + c_name + "/" + display + "</a>";
    target.innerHTML = str;
}






