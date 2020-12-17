//初始
function init(role){
    //判斷是拿誰的
    var myURL =ngrok;
    if(role=="student"){
        myURL += "stu_member_list";
    }
    else if(role=="teacher"){
        myURL += "tea_member_list";
    }
    console.log("myURL: "+myURL);
    //放心去拿
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            console.log("success");
            createTable(response, role);
        },
        error: function(){
            console.log("error");
        }
    });
}
  
//創建表格
function createTable(data, role){
    
    //按鈕的顯示
   console.log("init role: "+role); document.getElementById(role).setAttribute("class", "btn btn-dark");
    if(role=="teacher"){
        document.getElementById("student").setAttribute("class", "btn btn-outline-dark");
    }
    else if(role=="student"){
        document.getElementById("teacher").setAttribute("class", "btn btn-outline-dark")
    }
    
    //表格裡的值
    var content = "";
    //一筆資料
    if(data.length==null){
        content += '<tr><td id="'+data.user_id+'_name">'+data.name+'</td>'
        +'<td id="'+data.user_id+'_id">'+data.user_id+'</td>'
        +'<td id="'+data.user_id+'_course">'+'<button class="btn btn-outline-secondary" type="button" data-toggle="modal" data-target="#example" onclick="showCourse('+"'"+data.name+"','"+role+"'"+')">點我</button>'+'</td>'
        +'<td id="'+data.user_id+'_phone">'+data.phone+'</td>'
        +'<td id="'+data.user_id+'_email">'+data.email+'</td>'
        +'<td id="'+data.course_id+'"><button class="btn btn-secondary" type="button" data-toggle="modal" data-target="#example" onclick="edit('+"'"+data.user_id+"'"+')">edit</button></td></tr>';
    }
    //多筆資料
    else{
        for(var i=0; i<data.length; i++){
            content += '<tr><td id="'+data[i].user_id+'_name">'+data[i].name+'</td>'
        +'<td id="'+data[i].user_id+'_id">'+data[i].user_id+'</td>'
        +'<td id="'+data[i].user_id+'_course">'+'<button class="btn btn-outline-secondary" type="button" data-toggle="modal" data-target="#example" onclick="showCourse('+"'"+data[i].name+"','"+role+"'"+')">點我</button>'+'</td>'
        +'<td id="'+data[i].user_id+'_phone">'+data[i].phone+'</td>'
        +'<td id="'+data[i].user_id+'_email">'+data[i].email+'</td>'
        +'<td id="'+data[i].course_id+'"><button class="btn btn-secondary" type="button" data-toggle="modal" data-target="#example" onclick="edit('+"'"+data[i].user_id+"','"+role+"'"+')">edit</button></td></tr>';
        }
    }
    document.getElementById("tbody").innerHTML = content;
    
}

//按點我之後拿到，他有上/教的課
function showCourse(name, role){
    document.getElementById("myContent").innerHTML = "";
    var content = "";
    var myURL = ngrok + "user_detail_info?name="+name;
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            console.log("success");
            
                
            //跳出表單
            var content="";
            content += '<form>';
            //填名字 id="user_name"
            content += '<div class="form-group"><label class="col-form-label">';

            for(var i=0; i<response[0].course_name_list.length; i++){
            console.log("course name: "+response[0].course_name_list[i]);
                content += response[0].course_name_list[i] +"<br>";
            }
            
            content += '</label></div>';

            content += '</form>';
            document.getElementById("myContent").innerHTML = content;
            document.getElementById("exampleModalLabel").innerHTML = "課程清單";
            
            document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>';
            
        },
        error: function(){
            console.log("error");
        }
    });
}

//搜尋成員姓名＆顯示
function search(){
    console.log("search");
    console.log($("#myval").val());
    var myURL = ngrok+"user_detail_info?name="+$("#myval").val();
    console.log("myURL: "+myURL);
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            console.log("success");
            createTable(response, response[0].role);
        },
        error: function(){
            console.log("error");
        }
    });
}

//新增成員
function add(){
    document.getElementById("myContent").innerHTML = "";
    var temp = "";
    
    //跳出表單
    var content="";
    content += '<form>';
    //填名字 id="user_name"
    content += '<div class="form-group"><label class="col-form-label">名字：<input type="text" class="form-control" id="user_name" value="名字"></label></div>';
    
    //填密碼 id="password"
    content += '<div class="form-group"><label class="col-form-label">密碼：<input type="text" class="form-control" id="password" value="密碼"></label></div>';
    
    //填電話 id="phone"
    content += '<div class="form-group"><label class="col-form-label">電話：<input type="tel" class="form-control" id="phone" value="電話" pattern="\d{10}"></label></div>';
    
    //填email id="email"
    content += '<div class="form-group"><label class="col-form-label">email：<input type="email" class="form-control" id="email" value="email"></label></div>';
    
    //選擇角色 id="role"
    content += '<div class="form-group"><label class="col-form-label">身份：<select class="form-control" id="role" onchange="setForm(this)"><option selected>學生</option><option>老師</option></select></label></div>';
    
    //(預設)選課程 id="choose"
    content += '<div class="form-group" id="dynamite"><label class="col-form-label">課程：<select class="form-control" id="choose"></select></label></div>';
    
    content += '</form>'
    document.getElementById("myContent").innerHTML = content;
    document.getElementById("exampleModalLabel").innerHTML = "新增成員";
    
    //拿到course&teacher
    temp="";
    var myURL = ngrok +"cs_course_list"
    $.ajax({
        url: myURL,
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            console.log("success");
            for(var i=0; i<response.length; i++){
                temp += "<option>"+ response[i].name +" - "+response[i].teacher+"</option>";
            }
            document.getElementById("choose").innerHTML = temp;
        },
        error: function(){
            console.log("error");
        }
    });
    
    document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>'
        +'<button type="button" class="btn btn-primary" onclick="addUser()" data-dismiss="modal">Submit</button>';
}

//動態設定表單
function setForm(temp){
    var index = parseInt(temp.selectedIndex);
    console.log("index: "+index);
    
       var change = "";
    if(index==0){
        //選課程 id="choose"
        change= '<label class="col-form-label">課程：<select class="form-control" id="choose"></select></label>';
        
    //拿到course&teacher
    var temp="";
    var myURL=ngrok + "cs_course_list";
    $.ajax({
        url: myURL,
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            console.log("success");
            for(var i=0; i<response.length; i++){
                temp += "<option>"+ response[i].name +" - "+response[i].teacher+"</option>";
            }
            document.getElementById("choose").innerHTML = temp;
        },
        error: function(){
            console.log("error");
        }
    });
        }
        else if(index==1){
           //填專業科目 id="choose"
            change = '<label class="col-form-label">專業科目：<input type="text" class="form-control" id="choose" value="專業科目"></label>'; 
        }
        document.getElementById("dynamite").innerHTML = change;
}

//傳新增的成員資料到後端
function addUser(){
    
    var major=null, course_list=[]; 
    //判斷是誰
    if($("#role").val()=="學生"){
        course_list[0] = $("#choose").val();
    }
    else if($("#role").val()=="老師"){
        major = $("#choose").val();
    }
    
    //送資料
    console.log($("#password").val(), $("#user_name").val(), course_list, $("#phone").val(), $("#email").val(), major, $("#role").val());
    sendData(null, $("#password").val(), $("#user_name").val(), course_list, $("#phone").val(), $("#email").val(), major, null, $("#role").val(), "add");
    //sendData(null, $("#password").text(), $("#user_name").text(), course_list, $("#phone").text(), $("#email").text(), major, null, $("#role").text(), "add");
}

//未完成
function edit(id, role){
    var content="",
    name = document.getElementById(id+"_name").innerText,
    phone = document.getElementById(id+"_phone").innerText,
    email = document.getElementById(id+"_email").innerText,
    course = document.getElementById(id+"_course").innerText;
    
    document.getElementById("exampleModalLabel").innerHTML = "編輯成員";
    
     content += '<form>';
    //填名字 id="user_name"
    content += '<div class="form-group"><label class="col-form-label">名字：<input type="text" class="form-control" id="user_name" value="'+name+'"></label></div>';
    //填電話 id="phone"
    content += '<div class="form-group"><label class="col-form-label">電話：<input type="tel" class="form-control" id="phone" value="'+phone+'" pattern="\d{10}"></label></div>';
    //填email id="email"
    content += '<div class="form-group"><label class="col-form-label">email：<input type="email" class="form-control" id="teacher" value="'+email+'"></label></div>';
    
    //判斷是選課｜專業科目
    if(role=="student"){
        //選課程 id="choose"
        content += '<div class="form-group" id="dynamite"><label class="col-form-label">課程：<select class="form-control" id="choose"></select></label></div>'; 
        
        //拿到course&teacher
        temp="";
        $.ajax({
            url:"https://0d71af81d7eb.ngrok.io/cs/cs_course_list",
            dataType: "json",
            contentType: 'application/json; charset=utf-8',
            success: function(response){
                console.log("success");
                for(var i=0; i<response.length; i++){
                    temp += "<option>"+ response[i].name +" - "+response[i].teacher+"</option>";
                }
                document.getElementById("choose").innerHTML = temp;
            },
            error: function(){
                console.log("error");
            }
        });
        
        //顯示有上的課程 的按鈕
        $.ajax({
            url:"https://0d71af81d7eb.ngrok.io/cs/user_detail_info?name="+name,
            dataType: "json",
            contentType: 'application/json; charset=utf-8',
            success: function(response){
                
                console.log("it is success");
                
                content += '123<input type="text" class="form-control" value="hello">';
                console.log("content: "+content);
            },
            error: function(){
                console.log("error");
            }
        });
    }
    else if(role=="teacher"){
        //填專業科目 id="choose"
        content += '<div class="form-group"><label class="col-form-label">專業科目：<input type="text" class="form-control" id="choose" value="專業科目"></label></div>'; 
    }
    content += "</form>";

    document.getElementById("myContent").innerHTML = content;
    
    
    document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>'
        +'<button type="button" class="btn btn-primary" onclick="editUser('+"'"+id+"'"+')" data-dismiss="modal">Submit</button>';
    
}

//未完成
function editUser(id){
    //不給 password, personal_plan, role
    
}

//傳新增｜編輯的資料
function sendData(id, password, name, course_list, phone, email, major, personal_plan, role, choice){
    if(role=="學生")
        role = "student";
    else if(role=="老師")
        role = "teacher";
    var send;
    var myURL=ngrok;
    //新增
    if(choice=="add"){
        myURL = myURL + "insert_user_detail_info";
        send={
            "name" : name,
            "password": password,
            "course_list": course_list,
            "phone": phone,
            "email": email,
            "major": major,
            "personal_plan": personal_plan,
            "role": role
        };
    }
    //未完成
    else if(choice=="edit"){
        myURL = myURL + "edit_cs_course_info";
        
        send={
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
        success: function(){
            init("student");
        }
    });
}

//刪除成員
function del(){
    document.getElementById("myContent").innerHTML = "";
    //跳出表單
    var content="";
    content += '<form>';
    content += '<div class="form-group"><label class="col-form-label">成員ID：<input type="text" class="form-control" id="user_id" value="成員ID"></label></div></form>';
    
    document.getElementById("myContent").innerHTML = content;
    document.getElementById("exampleModalLabel").innerHTML = "刪除成員";
    document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>'
        +'<button id="submit" type="button" class="btn btn-primary" onclick="delUser()" data-dismiss="modal">Submit</button>';
}

//傳刪除成員的資料到後端
function delUser(){
    var myURL=ngrok+"delete_user_detail_info?user_id="+$("#user_id").val();
    console.log("URL: "+myURL);
    
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(){
            init("student");
        }
    });
}

function start(){
    init("student");
    setSideBar();
}

window.addEventListener("load", start, false);
