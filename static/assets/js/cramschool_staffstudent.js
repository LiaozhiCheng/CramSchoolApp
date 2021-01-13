//偵測 done

//某學生所有之課程
var studentCourse = {"id" : new Array(), "name" : new Array()};
var allCourse = new Array();
var in_course = new Array();
var edit_course = new Array();
var del_course = new Array();

//拿到所有課程 By安祺
function getAllCourse(){
    var myURL = ngrok+"cs_course_list";
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        async: false,
        
        success: function(data){
            
            if(data[0].message == undefined){
                for(var i in data){
                    var one_course = {
                        "id" : data[i].course_id,
                        "name" : data[i].name,
                        "teacher" : data[i].teacher
                    };
                    allCourse.push(one_course);
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
            if(response[0].message == undefined){
                createTable(response, role);
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

//創建表格
function createTable(data, role){
    document.getElementById("tbody").innerHTML = "";
    
    //按鈕的顯示
    document.getElementById(role).setAttribute("class", "btn btn-dark");
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
        +'<td id="'+data.course_id+'"><button class="btn btn-secondary" type="button" data-toggle="modal" data-target="#example" onclick="edit('+"'"+data.user_id+"','"+role+"'"+')">edit</button></td></tr>';
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
            
            if(response[0].message == undefined){
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

//搜尋成員姓名＆顯示
function search(){
    
    var myURL = ngrok+"user_detail_info?name="+$("#myval").val();
    console.log("myURL: "+myURL);
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            if(response[0].message == undefined){
                createTable(response, response[0].role);
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

//新增成員
function add(){
    document.getElementById("myContent").innerHTML = "";
    var temp = "";
    
    //跳出表單
    var content="";
    content += '<form>';
    //填名字 id="user_name"
    content += '<div class="form-group"><label class="col-form-label">名字：<input type="text" class="form-control" id="user_name" placeholder="名字"></label></div>';
    
    //填密碼 id="password"
    content += '<div class="form-group"><label class="col-form-label">密碼：<input type="text" class="form-control" id="password" placeholder="密碼"></label></div>';
    
    //填電話 id="phone"
    content += '<div class="form-group"><label class="col-form-label">電話：<input type="tel" class="form-control" id="phone" placeholder="電話" pattern="\d{10}"></label></div>';
    
    //填email id="email"
    content += '<div class="form-group"><label class="col-form-label">email：<input type="email" class="form-control" id="email" placeholder="email"></label></div>';
    
    //選擇角色 id="role"
    content += '<div class="form-group"><label class="col-form-label">身份：<select class="form-control" id="role" onchange="setForm(this)"><option selected>學生</option><option>老師</option></select></label></div>';
    
    //(預設)選課程 id="choose"
    content += '<div class="form-group"><label class="col-form-label">課程：<select class="form-control" id="choose"></select></label></div>';
    
    //如果是老師要多出major id="add_major"
    content += '<div class="form-group" id="add_major"></div>';
    
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
            
            if(response[0].message == undefined){
                for(var i=0; i<response.length; i++){
                    temp += '<option id="'+response[i].course_id+'">'+ response[i].name +" - "+response[i].teacher+"</option>";
                }
                document.getElementById("choose").innerHTML = temp;
            }
            else{
                window.alert("出了點錯，請稍後再試！");
            }
            
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
    
    var change = "";
    
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
            if(response[0].message == undefined){
                for(var i=0; i<response.length; i++){
                    temp += '<option id="'+response[i].course_id+'">'+ response[i].name +" - "+response[i].teacher+"</option>";
                }
                document.getElementById("choose").innerHTML = temp;
            }
            else{
                window.alert("出了點錯，請稍後再試！");
            }
        },
        error: function(){
            console.log("error");
        }
    });
    
    //老師會比學生多出major
    if(index==0){
        document.getElementById("add_major").innerHTML = "";
    }
    else if(index==1){
       //填專業科目 id="choose"
        change = '<label class="col-form-label">專業科目：<input type="text" class="form-control" id="major" value="專業科目"></label>'; 
        document.getElementById("add_major").innerHTML =change; 
    }
    
}

//傳新增的成員資料到後端
function addUser(){
    
    var major="", course_list=[]; 
    var myselect, index, coures_id;
    
    myselect = document.getElementById("choose");
    index = myselect.selectedIndex;
    course_id = myselect.options[index].id;
    course_list[0] = course_id;
    
    if($("#role").val()=="老師"){
        major = $("#major").val();
        //console.log("add_major: "+major);
    }
    
    
    //送資料
    sendData(null, $("#password").val(), $("#user_name").val(), course_list, null, $("#phone").val(), $("#email").val(), major, null, $("#role").val(), "add");
}

//再次確認 By安祺
function editCourse(e){
	//若新增詢問是否確定
	if(e.checked){
		var result = confirm("確定新增課程？");
		if(result){
			alert("已新增課程！");
		}
		else{
			e.checked = false;
		}
	}
	else{
		var result = confirm("確定刪除課程？");
		if(result){
			alert("已刪除課程！");
		}
		else{
			e.checked = true;
		}
	}
}

function set_course(o){
    if(o.checked == true){//新增他
        var result = confirm("確定新增課程？");
		if(result){
			alert("已新增課程！");
            edit_course.push(o.id);
		}
        else{
            o.checked == false;
        }
    }
    else{
        //remove？？
        var result = confirm("確定刪除課程？");
		if(result){
            if(in_course.indexOf(o.id)!=-1){
                //如果在上課的陣列裡
                del_course.push(o.id);
                edit_course.remove(o.id);
            }
            else if(edit_course.indexOf(o.id)!=-1){
                //如果在編輯的陣列裡
                edit_course.remove(o.id);
            }
            
			alert("已刪除課程！");
            
		}
		else{
			o.checked = true;
		}
    }
}

function edit(id, role){
    del_course = [];
    console.log("edit");
    var content="",
    name = document.getElementById(id+"_name").innerText,
    phone = document.getElementById(id+"_phone").innerText,
    email = document.getElementById(id+"_email").innerText,
    course = document.getElementById(id+"_course").innerText;
    
    document.getElementById("exampleModalLabel").innerHTML = "編輯成員";
    
     content += '<form>';
    //填名字 id="user_name"
    content += '<div class="form-group"><label class="col-form-label">名字：<input type="text" class="form-control" id="user_name" placeholder="'+name+'", value="'+name+'"></label></div>';
    //填電話 id="phone"
    content += '<div class="form-group"><label class="col-form-label">電話：<input type="tel" class="form-control" id="phone" placeholder="'+phone+'", value="'+phone+'", pattern="\d{10}"></label></div>';
    //填email id="email"
    content += '<div class="form-group"><label class="col-form-label">email：<input type="email" class="form-control" id="email" placeholder="'+email+'", value="'+email+'"></label></div>';
    
    
    var myURL = ngrok+"user_detail_info?name="+name;
    //拿到那個學生的修課資料
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        async: false,
        
        success: function(data){
            
            if(data[0].message == undefined){
                in_course = [];
                edit_course = [];
                studentCourse = {"id" : [], "name" : []};
                for(var i in data[0].course_list){
                    edit_course.push(data[0].course_list[i]);
                    in_course.push(data[0].course_list[i]);
                }
                for(var i in data[0].course_name_list){
                    studentCourse.id.push(data[0].course_list[i]);
                    studentCourse.name.push(data[0].course_name_list[i]);
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
    
    //選課程 id="choose"
    content += '<div class="form-group" id="dynamite"><label class="col-form-label">課程：</label>'; 


    //所有課程列表
    for(i=0; i<allCourse.length; i++){
        content += "<div class='d-flex justify-content-center row w-100'>"
                //設置label
                + "<label for='" + allCourse[i].id + "' class='col-9'>" 
                + allCourse[i].name + "-" + allCourse[i].teacher + "</label>"
                + "<div class='col-3'>"
                //設置input: id = courseID
                + "<input type='checkbox' id='" + allCourse[i].id + "' onclick=set_course(this)";
        //若學生已有該課程，則設置為checked
        if(studentCourse.id.includes(allCourse[i].id)){
            content += " checked";
        }
        content += " onclick='editCourse(this)'></div></div></div>";
    }
    
    //老師會多出專業科目
    if(role=="teacher"){
        //填專業科目 id="choose"
        content += '<div class="form-group"><label class="col-form-label">專業科目：<input type="text" class="form-control" id="major" placeholder="專業科目"></label></div>'; 
    }
    content += "</form>";

   document.getElementById("myContent").innerHTML = content;
    
    document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>'+'<button type="button" class="btn btn-primary" data-dismiss="modal" onclick="editUser(\''+id+"', '"+role+'\')">Submit</button>';
    
}

function editUser(user_id, role){
    var name = $("#user_name").val();
    var phone = $("#phone").val();
    var email = $("#email").val();
    var major="";
    
    if(role=="student"){
        console.log("edit_sendData");
       sendData(user_id, null, name, edit_course, del_course, phone, email, major, null, role, "edit");
    }
    else if(role=="teacher"){
        major = $("#major").val();
        sendData(user_id, null, name, edit_course, del_course, phone, email, major, null, role, "edit");
    }
}

//傳新增｜編輯的資料
function sendData(id, password, name, course, del_course, phone, email, major, personal_plan, role, choice){
    if(role=="學生")
        role = "student";
    else if(role=="老師")
        role = "teacher";
    var send;
    var myURL=ngrok;
    
    console.log("send_major: "+major);
    //新增
    if(choice=="add"){
        myURL = myURL + "insert_user_detail_info";
        send={
            "name" : name,
            "password": password,
            "course_list": course,
            "phone": phone,
            "email": email,
            "major": major,
            "personal_plan": personal_plan,
            "role": role
        };
    }
    
    //編輯
    else if(choice=="edit"){
        myURL = myURL + "edit_user_detail_info";
        console.log("user_id: "+id);
        console.log("name: "+name);
        
        var i;
        
        if(edit_course==[]){
            course_list = null;
        }
        if(del_course==[]){
            course_list = null;
        }
        
        send={
            "user_id": id,
            "name" : name,
            "delete_from_course_list": del_course,
            "course_list": course,
            "phone": phone,
            "email": email,
            "major": null
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
                init("student");
            }
            else{
                window.alert("出了點錯，請稍後再試！");
            }
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
    console.log("delUser()");
    var myURL=ngrok+"delete_user_detail_info?user_id="+$("#user_id").val();
    
    console.log("URL: "+myURL);
    
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            
            if(response[0].message == undefined){
                init("student");
            }
            else{
                window.alert("出了點錯，請稍後再試！");
            }
        }
    });
}

function start(){
    getAllCourse();
    init("student");
    setSideBar();
}

window.addEventListener("load", start, false);
