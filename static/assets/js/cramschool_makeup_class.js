//測試 done

var tbody = document.getElementById("tbody");
var week=["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"];

//初始
function init(){
    var myURL=ngrok + "cs_reschedule_list";
    console.log("myURL: "+myURL);
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            if(response.message == undefined){
                for(var i=0; i<response.length; i++){
                    var myID = (parseInt(response[i].datetime.slice(17,19)-17)/2)*7 + week.indexOf(response[i].weekday);

                    console.log("myID: "+myID);
                    console.log("full: "+response[i].full);
                    console.log("state: "+response[i].state);

                    temp = document.getElementById(myID);
                    //如果滿了，就顯示full
                    if(response[i].full == true){
                        temp.innerHTML='<button class="btn btn-outline-danger" type="button" data-toggle="modal" data-target="#example" onclick="show('+"'"+myID+"'"+')">滿！</button>';
                    }
                    //如果尚未開啟，就會有按鈕可以按
                    else if(response[i].state == false){
                        temp.innerHTML='<button class="btn btn-secondary" onclick="makeup('+"'"+myID+"'"+')">開放</button>';
                    }
                    //如果有開放，但尚未滿
                    else if(response[i].state==true && response[i].full==false){
                        console.log("未滿： "+myID);
                        temp.innerHTML='<button class="btn btn-outline-secondary" type="button" data-toggle="modal" data-target="#example" onclick="show('+"'"+myID+"'"+')">未滿</button>';
                    }
                }
            }
            else{
                window.alert("出了點錯，請稍後再試！");
            }
        },
        error: function(){
            console.log("error");
        }
    }); 
}

//點了那個格子，要show出詳細資訊 ex.誰來補什麼時候的課 未完成
function show(id){
    document.getElementById("exampleModalLabel").innerHTML = "詳細資訊";
    var content="", myURL = ngrok+"cs_reschedule_info?weekday="+week[id%7]+"&time="+(Math.floor(id/7)*2+17)+":00";
    console.log("myURL: "+myURL);
    
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            if(response.message == undefined){
                content += "<form>";
                for(var i=0; i<response.length; i++){
                    content += '<div class="form-group">';
                    content += '<ul>';

                    content += '<li>'+response[i].name+" /  "+response[i].lesson_time.slice(8,11)+" "+response[i].lesson_time.slice(5,7)+" / "+response[i].course_name;

                    content += '</li></div>';
                     if(i==response.length-1){
                         content += '</ul>';
                     }
                }
                if(response.length==0){
                    content +="尚未有人來補課";
                }
               content+='</form>'; document.getElementById("myContent").innerHTML = content;
            }
            else{
                window.alert("出了點錯，請稍後再試！");
            }
        },
        error: function(){
            console.log("error");
        }
    });
    
    document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal" onclick="miss()">Cancle</button>';
}

//為了不要顯示上一次的資訊
function miss(){
    document.getElementById("myContent").innerHTML = "";
}

//按了open打開
function makeup(id){
    
    var myURL = ngrok+"edit_cs_reschedule_list?weekday="+week[id%7]+"&time="+(Math.floor(id/7)*2+17)+":00&new_state=1";
    
    console.log("myURL: "+myURL);
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            if(response[0].message == undefined){
                init();
            }
            else{
                window.alert("出了點錯，請稍後再試！");
            }
        },
        error: function(){
            console.log("error");
        }
    });
    
}

//start
function start(){
    var i, content="", t=5, temp;
    
    for(i=0; i<21; i++){
        if(i%7==0){
            content+='<tr><th>PM'+t+'~'+(t+2)+'</th>';
            t+=2;
        }
        content+='<td id="'+i+'"></td>';
        if(i%7==6){
            content+='</tr>';
        }
        tbody.innerHTML=content;
    }
    init();
    setSideBar();
}

window.addEventListener("load", start, false);
