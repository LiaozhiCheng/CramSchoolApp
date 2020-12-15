var weekday=['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat'];

//有ajax
function init(){
    //初始
    $.ajax({
        url:"https://71b319ef9bad.ngrok.io/cs/cs_course_list",
        //url: "coursetest.json",
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            console.log("success");
            console.log("startdatein: "+response[0].start_time);
            createTable(response);
            
        },
        error: function(){
            console.log("error");
        }
    });
}

//初始化表格
function createTable(data){
    var content = "", setTime="";
    
    for(var i=0; i<data.length; i++){
        console.log("startdate: "+data[i].start_time);
        content += "<tr>"
        +'<td id="'+data[i].course_id+'_name">'+data[i].name+"</td>"
        +'<td id="'+data[i].course_id+'_id">'+data[i].course_id+"</td>"
        +'<td id="'+data[i].course_id+'_week">'+data[i].course_time.slice(12,15)+"</td>"
        +'<td id="'+data[i].course_id+'_time">'+data[i].course_time.slice(0,11)+"</td>"
        +'<td id="'+data[i].course_id+'_startdate">'+data[i].start_time.slice(8,11)+' '+data[i].start_time.slice(5,7)+'</td>'
        //+'<td id="'+data[i].course_id+'_startdate">'+data[i].start_time+'</td>'
        +'<td id="'+data[i].course_id+'_teacher">'+data[i].teacher+"</td>"
        +'<td id="'+data[i].course_id+'_student">'+"點我"+"</td>"
        +'<td id="'+data[i].course_id+'_classroom">'+(data[i].classroom).name+"</td>"
        +'<td id="'+data[i].course_id+'"><button class="btn btn-secondary" type="button" data-toggle="modal" data-target="#example" onclick="edit('+"'"+data[i].course_id+"'"+')">編輯</button></td></tr>';
    }
    document.getElementById("tbody").innerHTML = content;
}

//拿到某課程學生清單 未完成
function getStdList(id){
    var content="";
    $.ajax({
        //url:"https://f48f9286d0b6.ngrok.io/test/cs_course_list",
        //url: "coursetest.json",
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            console.log("success");
        },
        error: function(){
            console.log("error");
        }
    });
}

//搜尋課程名稱＆顯示
function search(){
    console.log("search");
    console.log($("#myval").val());
    var myURL="https://71b319ef9bad.ngrok.io/cs/cs_course_info?name="+$("#myval").val();
    console.log("myURL: "+myURL);
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            console.log("success");
            createTable(response);
        },
        error: function(){
            console.log("error");
        }
    });
}

//新增課程
function add(){
    var temp = "";
    
    //跳出表單
    var content="";
    content += '<form>';
    content += '<div class="form-group"><label class="col-form-label">課程名稱：<input type="text" class="form-control" id="course_name" value="課程名稱 ex.1101軟工"></label></div>';
    //用選的
    content += '<div class="form-group"><label class="col-form-label">開始日期：<input type="date" class="form-control" id="start_date" value=""></label></div>';
    //用選的
    content += '<div class="form-group"><label class="col-form-label">星期：<select class="form-control" id="week"></select></label></div>';
    //用選的
    content += '<div class="form-group"><label class="col-form-label">時間：<input type="time" class="form-control" id="start_time" value="">~<input type="time" class="form-control" id="end_time" value=""></label></div>';

    content += '<div class="form-group"><label class="col-form-label">老師：<input type="text" class="form-control" id="teacher" value="老師 ex.馬小彬"></label></div>';
    
    //用選的
    content += '<div class="form-group"><label class="col-form-label">教室：<select class="form-control" id="classroom"></select></label></div>';
    
    content += '<div class="form-group"><label class="col-form-label">總結：<input type="text" class="form-control" id="summary" value="總結"></label></div>';

    content += '</form>'
    document.getElementById("myContent").innerHTML = content;
    document.getElementById("exampleModalLabel").innerHTML = "新增課程";
    
    //拿到星期幾的選項
    for(var i=0; i<weekday.length; i++){
        temp += "<option>"+ weekday[i] +"</option>"
    }
    document.getElementById("week").innerHTML = temp;
    
    //拿到教室的選項
    temp="";
    $.ajax({
        url:"https://71b319ef9bad.ngrok.io/cs/cs_classroom_list",
        //type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            console.log("success");
            for(var i=0; i<response.length; i++){
                console.log("roomName: "+response[i].name);
                    temp += "<option>"+ response[i].name +"</option>"
            }
            document.getElementById("classroom").innerHTML = temp;
        },
        error: function(){
            console.log("error");
        }
    });
    
    
    document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancle</button>'
        +'<button type="button" class="btn btn-primary" onclick="addCourse()" data-dismiss="modal">Submit</button>';
}

//把新增的課程資料傳到後端（拿教室資訊）
function addCourse(){
    var setTime = $("#start_time").val()+"~"+$("#end_time").val()+"-"+$("#week").val();
    
     var myURL = "https://71b319ef9bad.ngrok.io/cs/cs_classroom_info_by_name?name="+$("#classroom").val();
    //拿到教室的dic
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            //把所有參數傳到send
            sendData(null, $("#course_name").val(), $("#start_date").val(), setTime, $("#teacher").val(), $("#summary").val(), response, "add");
        },
        error: function(){
            console.log("error");
        }
    });
}

//編輯課程
function edit(id){
    console.log("edit");
    var choice="", content="", temp="",
        week=document.getElementById(id+"_week").innerText,
        teacher = document.getElementById(id+"_teacher").innerText,
        start_time = document.getElementById(id+"_time").innerText.slice(0,5),
        end_time = document.getElementById(id+"_time").innerText.slice(6,11),
        classroom = document.getElementById(id+"_classroom").innerText;
    
    document.getElementById("exampleModalLabel").innerHTML = "編輯課程";
    
    content += '<form>';
    //編輯開始日期
    content += '<div class="form-group"><label class="col-form-label">開始日期：<input type="date" class="form-control" id="start_date" value=""></label></div>';
    
    //編輯星期幾
    content += '<div class="form-group"><label class="col-form-label">星期：<select class="form-control" id="week"></select></label></div>';
    
    //編輯時間
    content += '<div class="form-group"><label class="col-form-label">時間：<input type="time" class="form-control" id="start_time" value="'+start_time+'">~<input type="time" class="form-control" id="end_time" value="'+end_time+'"></label></div>';
    
    //編輯老師
    content += '<div class="form-group"><label class="col-form-label">老師：<input type="text" class="form-control" id="teacher" value="'+teacher+'"></label></div>';
    
    //編輯教室
    content += '<div class="form-group"><label class="col-form-label">教室：<select class="form-control" id="classroom"></select></label></div>';
    
    //編輯summary
    content += '<div class="form-group"><label class="col-form-label">總結：<input type="text" class="form-control" id="summary" value="總結"></label></div>';
    
    content +='</form>';
    
    document.getElementById("myContent").innerHTML = content;
    
    //拿到星期幾的選項
    for(var i=0; i<weekday.length; i++){
        if(week == weekday[i]){
            choice += "<option selected>"+ weekday[i] +"</option>";
        }
        else{
            choice += "<option>"+ weekday[i] +"</option>";
        }
    }
    document.getElementById("week").innerHTML = choice;
    //$("#week").val(week);
    
    //拿到教室的選項
    temp="";
    $.ajax({
        url:"https://71b319ef9bad.ngrok.io/cs/cs_classroom_list",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            for(var i=0; i<response.length; i++){
                if(classroom == response[i].name){
                   temp += "<option selected>"+ response[i].name +"</option>";
                }
                else{
                    temp += "<option>"+ response[i].name +"</option>";
                }
            }
            document.getElementById("classroom").innerHTML = temp;
        },
        error: function(){
            console.log("error");
        }
    });
    
    document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancle</button>'
        +'<button type="button" class="btn btn-primary" onclick="editCourse('+"'"+id+"'"+')" data-dismiss="modal">Submit</button>';
}

//把編輯的課程資料傳到後端（拿教室資訊）
function editCourse(id){
    
    console.log("room: "+$("#classroom").val());
    var myURL = "https://71b319ef9bad.ngrok.io/cs/cs_classroom_info_by_name?name="+$("#classroom").val();
    
    console.log("myURL: "+myURL);
    
    //拿到教室的名字
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            
            var name=document.getElementById(id+"_name").innerText,
                startdate = $("#start_date").val(),
                setTime = $("#start_time").val()+"~"+$("#end_time").val()+"-"+$("#week").val(),
                teacher = $("#teacher").val(),
                summary = $("#summary").val(),
                classroom = response;
                //console.log("editstartdate: "+startdate);
                sendData(id, name, startdate, setTime, teacher, summary, classroom, "edit");
        },
        error: function(){
            console.log("error");
        }
    });    
    
}

//傳新增｜編輯的資料到後端
function sendData(id, name, start_time, course_time, teacher, summary, classroom, choice){
    
    var myURL="";
    if(choice=="add"){
        myURL = "https://71b319ef9bad.ngrok.io/cs/insert_cs_course_info";
        var send={
            "name" : name,
            "start_time": start_time,
            "course_time": course_time,
            "teacher": teacher,
            "summary": summary,
            "classroom": classroom
        };
    }
    else if(choice=="edit"){
        myURL = "https://71b319ef9bad.ngrok.io/cs/edit_cs_course_info";
        console.log("course_id: "+id);
        console.log("name: "+name);
        console.log("start_time: "+start_time);
        console.log("course_time: "+course_time);
        console.log("teacher: "+teacher);
        console.log("summary: "+summary);
        console.log("classroom: "+classroom);
        console.log("classroom_name: "+classroom.name);
        var send={
            "course_id": id,
            "name" : name,
            "start_time": start_time,
            "course_time": course_time,
            "teacher": teacher,
            "summary": summary,
            "classroom": classroom
        };
    }
    
    
    $.ajax({
        url: myURL,
        type: "POST",
        dataType: "json",
        data: JSON.stringify(send),
        contentType: 'application/json; charset=utf-8',
    });
    
    init();
}

//刪除課程
function del(){
    //跳出表單
    var content="";
    content += '<form>';
    content += '<div class="form-group"><label class="col-form-label">課程ID：<input type="text" class="form-control" id="course_id" value="課程ID ex.C-001"></label></div></form>';
    
    document.getElementById("myContent").innerHTML = content;
    document.getElementById("exampleModalLabel").innerHTML = "刪除課程";
    document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancle</button>'
        +'<button id="submit" type="button" class="btn btn-primary" onclick="delCourse()" data-dismiss="modal">Submit</button>';
}

//把刪除的課程ID傳到後端
function delCourse(){
    var myURL = "https://71b319ef9bad.ngrok.io/cs/delete_cs_course_info?course_id="+$("#course_id").val();
    console.log("URL: "+myURL);
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
    });
    
    init();
}

//start
function start(){
    init();
}

window.addEventListener("load", start, false);