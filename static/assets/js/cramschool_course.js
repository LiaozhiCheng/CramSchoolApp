//測試 done

var weekday=['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat'];
//不要傳來傳去，太多function了，傳不完勒：）
var old_tea_id = "";

function init(){
    var myURL = ngrok + "cs_course_list";
    //初始
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
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
        content += "<tr>"
        +'<td id="'+data[i].course_id+'_name">'+data[i].name+"</td>"
        +'<td id="'+data[i].course_id+'_id">'+data[i].course_id+"</td>"
        +'<td id="'+data[i].course_id+'_week">'+data[i].course_time.slice(12,15)+"</td>"
        +'<td id="'+data[i].course_id+'_time">'+data[i].course_time.slice(0,11)+"</td>"
        +'<td id="'+data[i].course_id+'_startdate">'+data[i].start_time.slice(12, 16)+' '+data[i].start_time.slice(8,11)+' '+data[i].start_time.slice(5,7)+'</td>'
        //+'<td id="'+data[i].course_id+'_startdate">'+data[i].start_time+'</td>'
        +'<td id="'+data[i].course_id+'_teacher">'+data[i].teacher+"</td>"
        +'<td id="'+data[i].course_id+'_student">'+'<button class="btn btn-outline-secondary" type="button" data-toggle="modal" data-target="#example"  onclick="showStudent('+"'"+data[i].course_id+"'"+')">點我</button>'+"</td>"
        +'<td id="'+data[i].course_id+'_classroom">'+(data[i].classroom).name+"</td>"
        +'<td id="'+data[i].course_id+'"><button class="btn btn-secondary" type="button" data-toggle="modal" data-target="#example" onclick="edit('+"'"+data[i].course_id+"'"+')">編輯</button></td></tr>';
    }
    document.getElementById("tbody").innerHTML = content;
}

//按點我後，顯示有修課之學生清單
function showStudent(course_id){
    document.getElementById("myContent").innerHTML = "";
    
    document.getElementById("exampleModalLabel").innerHTML = "學生清單";
    
    var content = "";
    var myURL = ngrok + "cs_course_student_list?course_id="+course_id;
    console.log("myURL: "+myURL);
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            //跳出表單
            var content="";
            content += '<form>';
            content += '<div class="form-group"><label class="col-form-label">';

            if(response.length==0){
               content += "<h5>尚未有學生</h5>"
            }
            else{
                for(var i=0; i<response.length; i++){
                content += response[i] +"<br>";
                }
            }
            content += '</label></div>';

            content += '</form>';
            document.getElementById("myContent").innerHTML = content;
            document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>';
        },
        error: function(){
            console.log("error");
        }
    });
}

//搜尋課程名稱＆顯示
function search(){
    if($("#myval").val()==""){
        window.alert("不是啊～ 你要告訴我你要查什麼課！！！\n請重新輸入：）");
    }
    else{
        var myURL = ngrok+"cs_course_info_by_name?name="+$("#myval").val();
        console.log("myURL: "+myURL);
        $.ajax({
            url: myURL,
            type: "GET",
            dataType: "json",
            contentType: 'application/json; charset=utf-8',
            success: function(response){
                if(response[0].message == undefined){
                    createTable(response);
                }
                else{
                    window.alert(response[0].message);
                }
            },
            error: function(){
                console.log("error");
            }
        });
    }   
}

//抓老師列表，放在表單
function getTeacherOption(name){
    var tea="";
    old_tea_id = "";
    $.ajax({
        url: ngrok+"tea_member_list",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            if(response[0].message == undefined){
                for(var i=0; i<response.length; i++){
                    if(name == response[i].name){
                        old_tea_id = response[i].user_id;
                        tea += '<option id="'+response[i].user_id+'" selected>'+ response[i].name +"</option>";
                    }
                    else{
                        tea += '<option id="'+response[i].user_id+'">'+ response[i].name +"</option>";
                    }
                }
                document.getElementById("teacher").innerHTML = tea;
            }
            else{
                window.alert("出了點錯，請稍後再試！");
            }
        },
        error: function(){
            console.log("error");
        }
    })
}

//抓教室列表，放在表單
function getClassroomOption(name){
    //拿到教室的選項
    var temp="";
    $.ajax({
        url: ngrok + "cs_classroom_list",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            if(response[0].message == undefined){
                for(var i=0; i<response.length; i++){
                    if(response[i].name == name){
                       temp += "<option selected>"+ response[i].name +"</option>";
                        temp += '<option id="'+response[i].classroom_id+'" selected>'+ response[i].name +"</option>";
                    }
                    else{
                        temp += '<option id="'+response[i].classroom_id+'">'+ response[i].name +"</option>";
                    }
                }
                document.getElementById("classroom").innerHTML = temp;
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

//新增課程
function add(){
    var temp = "";
    
    //跳出表單
    var content="";
    content += '<form>';
    content += '<div class="form-group"><label class="col-form-label">課程名稱：<input type="text" class="form-control" id="course_name" placeholder="課程名稱 ex.1101軟工"></label></div>';
    //用選的
    content += '<div class="form-group"><label class="col-form-label">開始日期：<input type="date" class="form-control" id="start_date" value=""></label></div>';
    //用選的
    content += '<div class="form-group"><label class="col-form-label">星期：<select class="form-control" id="week"></select></label></div>';
    //用選的
    content += '<div class="form-group"><label class="col-form-label">時間：<input type="time" class="form-control" id="start_time" value="">~<input type="time" class="form-control" id="end_time" value=""></label></div>';

//    content += '<div class="form-group"><label class="col-form-label">老師：<select class="form-control" id="teacher"></select></label></div>';
    
    //用選的
    content += '<div class="form-group"><label class="col-form-label">教室：<select class="form-control" id="classroom"></select></label></div>';
    
    content += '<div class="form-group"><label class="col-form-label">總結：<input type="text" class="form-control" id="summary" placeholder="總結"></label></div>';

    content += '</form>'
    document.getElementById("myContent").innerHTML = content;
    document.getElementById("exampleModalLabel").innerHTML = "新增課程";
    
    //拿到星期幾的選項
    for(var i=0; i<weekday.length; i++){
        temp += "<option>"+ weekday[i] +"</option>"
    }
    document.getElementById("week").innerHTML = temp;
    
    //拿到老師的選項
//    getTeacherOption("");
    
    //拿到教室的選項
    getClassroomOption("");
    
    document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>'
        +'<button type="button" class="btn btn-primary" onclick="addCourse()" data-dismiss="modal">Submit</button>';
}

//把新增的課程資料傳到後端
function addCourse(){
    var setTime = $("#start_time").val()+"~"+$("#end_time").val()+"-"+$("#week").val();
    
//    var myselect=document.getElementById("teacher");
//    var index=myselect.selectedIndex;
//    var tea_id = myselect.options[index].id;
    
    myselect=document.getElementById("classroom");
    index=myselect.selectedIndex;
    var classroom_id = myselect.options[index].id;
    
    var summary;
    
    if($("#summary").val()==null){
        summary = "";
    }
    else{
        summary = $("#summary").val();
    }
    
    if($("#start_time").val()>$("#end_time").val()){
        window.alert("你在跟我開玩笑？\n開始時間比結束時間晚誒！！\n請重新輸入");
    }
    else{
        var temp="";
        var myURL = ngrok+"cs_classroom_info?classroom_id="+classroom_id;
        $.ajax({
            url: myURL,
            type: "GET",
            dataType: "json",
            contentType: 'application/json; charset=utf-8',
            success: function(response){

                //拿到教室的詳細資訊
                if(response.message == undefined){
                    console.log("myURL: "+myURL);
                    var classroom = {"capacity" : response.capacity,
                                    "classroom_id" : response.classroom_id,
                                    "name" : response.name};
                    //把所有參數傳到send
                    sendData(null, $("#course_name").val(), $("#start_date").val(), setTime, null, summary, classroom, "add");
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
}

//編輯課程
function edit(id){
    var choice="", content="", temp="",
        start_year = document.getElementById(id+"_startdate").innerText.slice(0, 4),
        start_month = month.indexOf(document.getElementById(id+"_startdate").innerText.slice(5, 8)),
        start_day = document.getElementById(id+"_startdate").innerText.slice(9, 11),
        week=document.getElementById(id+"_week").innerText,
        teacher = document.getElementById(id+"_teacher").innerText,
        start_time = document.getElementById(id+"_time").innerText.slice(0,5),
        end_time = document.getElementById(id+"_time").innerText.slice(6,11),
        classroom = document.getElementById(id+"_classroom").innerText;
    
    if(parseInt(start_month)<10){
        start_month = "0"+start_month;
    }
    
        var start_date = start_year+"-"+start_month+"-"+start_day;
    document.getElementById("exampleModalLabel").innerHTML = "編輯課程";

    
    content += '<form>';
    //編輯開始日期
    content += '<div class="form-group"><label class="col-form-label">開始日期：<input type="date" class="form-control" id="start_date" value="'+start_date+'"></label></div>';
    
    //編輯星期幾
    content += '<div class="form-group"><label class="col-form-label">星期：<select class="form-control" id="week"></select></label></div>';
    
    //編輯時間
    content += '<div class="form-group"><label class="col-form-label">時間：<input type="time" class="form-control" id="start_time" value="'+start_time+'">~<input type="time" class="form-control" id="end_time" value="'+end_time+'"></label></div>';
    
    //編輯老師
    content += '<div class="form-group"><label class="col-form-label">老師：<select class="form-control" id="teacher"></select></label></div>';
    
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
    
    getTeacherOption(teacher);
    
    getClassroomOption(classroom);
    
    document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancle</button>'
        +'<button type="button" class="btn btn-primary" onclick="editCourse('+"'"+id+"'"+')" data-dismiss="modal">Submit</button>';
}

//把編輯的課程資料傳到後端
function editCourse(id){
    
    //要給後端舊老師的id
    var myselect=document.getElementById("teacher");
    var index=myselect.selectedIndex;
    var tea_id = myselect.options[index].id;
    
    myselect=document.getElementById("classroom");
    index=myselect.selectedIndex;
    var classroom_id = myselect.options[index].id;

           
    var name=document.getElementById(id+"_name").innerText,
        startdate = $("#start_date").val(),
        setTime = $("#start_time").val()+"~"+$("#end_time").val()+"-"+$("#week").val(),
        teacher = tea_id,
        summary = $("#summary").val();
    
    if($("#start_time").val()>$("#end_time").val()){
        window.alert("你在跟我開玩笑？\n開始時間比結束時間晚誒！！\n請重新輸入");
    }
    else{
        var temp="";
        var myURL = ngrok+"cs_classroom_info?classroom_id="+classroom_id;
        $.ajax({
            url: myURL,
            type: "GET",
            dataType: "json",
            contentType: 'application/json; charset=utf-8',
            success: function(response){

                //拿到教室的詳細資訊
                if(response.message == undefined){
                    var classroom = {"capacity" : response.capacity,
                                "classroom_id" : response.classroom_id,
                                "name" : response.name};
                    sendData(id, name, startdate, setTime, teacher, summary, classroom, "edit");
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
        
}

//傳新增｜編輯的資料到後端
function sendData(id, name, start_time, course_time, teacher, summary, classroom, choice){
    var myURL="";
    if(choice=="add"){
        myURL = ngrok + "insert_cs_course_info";
        var send={
            "name" : name,
            "start_time": start_time,//開始日期
            "course_time": course_time,//時間幾點～幾點
            "summary": summary,
            "classroom": classroom
        };
    }
    else if(choice=="edit"){
        myURL = ngrok + "edit_cs_course_info";
        var send={
            "course_id": id,
            "name" : name,
            "start_time": start_time,
            "course_time": course_time,
            "new_teacher": teacher,
            "old_teacher": old_tea_id,
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
        success: function(response){
            if(response[0].message == undefined){
                init();
            }
            else{
                window.alert("您的輸入資料出了點錯，請再試一次！");
            }
        }
    });
}

//刪除課程
function del(){
    //跳出表單
    var content="";
    content += '<form>';
    content += '<div class="form-group"><label class="col-form-label">課程ID：<input type="text" class="form-control" id="course_id" placeholder="課程ID ex.C-001"></label></div></form>';
    
    document.getElementById("myContent").innerHTML = content;
    document.getElementById("exampleModalLabel").innerHTML = "刪除課程";
    document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>'
        +'<button id="submit" type="button" class="btn btn-primary" onclick="delCourse()" data-dismiss="modal">Submit</button>';
}

//把刪除的課程ID傳到後端
function delCourse(){
    var myURL = ngrok + "delete_cs_course_info?course_id="+$("#course_id").val();
    console.log("URL: "+myURL);
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
        }
    });
}

//start
function start(){
    init();
    setSideBar();
}

window.addEventListener("load", start, false);