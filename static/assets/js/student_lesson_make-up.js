window.onload = function init() {
    //get student's missed lessons
    getMissedLesson();
    
    //set page title
    document.getElementById("page-title").innerHTML = "預約補課";
    
    //::test::
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
    if(hour == 17){
        return days[weekDay-1] + '-0';
    }
    else if(hour == 19){
        return days[weekDay-1] + '-1';
    }
    else if(hour == 21){
        return days[weekDay-1] + '-2';
    }
}

//get available time
function getValidTime(){
    $.ajax({
        url: "testContent/rescheduleList.json",
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            for(var i=0; i<data.length; i++){
                var td_id = getTimeRange(data[i].datetime);
                switch(data[i].state){
                    case 'available':
                        resetTd(td_id);
                        break;
                    case 'full':
                        fullTd(td_id);
                        break;
                    case 'reserved':
                        reservedTd(td_id, data[i].course_name, data[i].lesson_progress, data[i].lesson_id);
                }
            }
        },
        
        error: function(){
            console.log("getValidTime error!!!!!!");
        }
        
    });
}

//set to unreserve state
function resetTd(td_id){
    var target = document.getElementById(td_id);
    var str = "<a href='#' class='normal' name='" + td_id + "' " 
            + "data-toggle='modal' data-target='#reserve' " 
            + "onclick='setCurr(this)'>預約補課</a>";
    target.innerHTML = str;
}

//set to full state
function fullTd(td_id){
    var target = document.getElementById(td_id);
    var str = "<a href='#' class='disabled' name='" + td_id 
            + "'>預約已滿</a>";
    target.innerHTML = str;
}

//set to reserved state
function reservedTd(td_id, c_name, l_name, l_id){
    var target = document.getElementById(td_id);
    var str = "<a href='#' class='normal' name='" + td_id + "' " 
            + "data-toggle='modal' data-target='#checkoutInfo' " 
            + "onclick='setCheckInfo(this)' id='" + l_id + "'>" 
            + c_name + "-" + l_name + "</a>";
    target.innerHTML = str;
}

//test: testing available time
function testing(){
    resetTd("mon-2");
    resetTd("sun-0");
    resetTd("sun-1");
    resetTd("sat-0");
    resetTd("sat-1");
}




