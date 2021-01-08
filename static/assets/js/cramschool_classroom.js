//測試 done

//有ajax
function init(){
    console.log("init");
    var myURL = ngrok + "cs_classroom_list";
    //初始
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            if(response[i].message == undefined){
                createTable(response);
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
function createTable(data){
    var content = "";
    //一筆資料
    if(data.length==null){
        content += '<tr><td id="'+data.classroom_id+'_name">'+data.name+'</td>'
        +'<td id="'+data.classroom_id+'_id">'+data.classroom_id+'</td>'
        +'<td id="'+data.classroom_id+'_capacity">'+data.capacity+'</td>'
        +'<td id="'+data.course_id+'"><button class="btn btn-secondary" type="button" data-toggle="modal" data-target="#example" onclick="edit('+"'"+data.classroom_id+"'"+')">edit</button></td></tr>';
    }
    //多筆資料
    else{
        for(var i=0; i<data.length; i++){
            
            content += '<tr><td id="'+data[i].classroom_id+'_name">'+data[i].name+'</td>'
            +'<td id="'+data[i].classroom_id+'_id">'+data[i].classroom_id+'</td>'
            +'<td id="'+data[i].classroom_id+'_capacity">'+data[i].capacity+'</td>'
            +'<td id="'+data[i].course_id+'"><button class="btn btn-secondary" type="button" data-toggle="modal" data-target="#example" onclick="edit('+"'"+data[i].classroom_id+"'"+')">edit</button></td></tr>';
        }
    }
   document.getElementById("tbody").innerHTML = content;
}

//搜尋教室名稱＆顯示 有ajax
function search(){
    var myURL=ngrok + "cs_classroom_info_by_name?name="+$("#myval").val();
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            if(response[i].message == undefined){
                if(response[0]==0){
                    document.getElementById("table").innerHTML = "<h5>查無此教室</h5>";
                }
                else{
                    createTable(response);
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

//新增教室
function add(){
    var temp = "";
    
    //跳出表單
    var content="";
    content += '<form>';
    //新增教室名稱
    content += '<div class="form-group"><label class="col-form-label">教室名稱：<input type="text" class="form-control" id="classroom_name" value="MAF412"></label></div>';
    
    //新增容量
    content += '<div class="form-group"><label class="col-form-label">容納人數：<input type="text" class="form-control" id="capacity" value="15"></label></div>';

    content += '</form>'
    document.getElementById("myContent").innerHTML = content;
    document.getElementById("exampleModalLabel").innerHTML = "新增課程";
    
     document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancle</button>'
        +'<button type="button" class="btn btn-primary" data-dismiss="modal" id="addButton">Submit</button>';
    document.getElementById("addButton").addEventListener("click", function(){
        sendData(null, $("#classroom_name").val(), $("#capacity").val(), "add");
    })
}

//編輯教室
function edit(id){
    
    var name = document.getElementById(id+"_name").innerText;
    capacity = document.getElementById(id+"_capacity").innerText;
    
    //跳出表單
    var content="";
    content += '<form>';
    
    //新增教室名稱
    content += '<div class="form-group"><label class="col-form-label">教室名稱：<input type="text" class="form-control" id="classroom_name" value="'+name+'"></label></div>';
    
    //新增容量
    content += '<div class="form-group"><label class="col-form-label">容納人數：<input type="text" class="form-control" id="capacity" value="'+capacity+'"></label></div>';

    content += '</form>'
    document.getElementById("myContent").innerHTML = content;
    document.getElementById("exampleModalLabel").innerHTML = "編輯教室";
    
    document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancle</button>'
        +'<button type="button" class="btn btn-primary" id="editButton" data-dismiss="modal" onclick="init()">Submit</button>';
    
    document.getElementById("editButton").addEventListener("click", function(){
        sendData(id, $("#classroom_name").val(), $("#capacity").val(), "edit");
    })
    
}

//傳新增｜編輯資料到後端 有ajax
function sendData(id, name, capacity, choice){
    
    var myURL=ngrok;
    if(choice=="add"){
        myURL += "insert_cs_classroom_info?name="+name+"&capacity="+capacity+"&classroom_id="+id;
    }
    else if(choice=="edit"){
        myURL += "edit_cs_classroom_info?classroom_id="+id+"&name="+name+"&capacity="+capacity;
    }
    
    console.log("myURL: "+myURL);
    
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            if(response[i].message == undefined){
                init();
            }
            else{
                window.alert("出了點錯，請稍後再試！");
            }
        }
    });
}

//刪除課程
function del(){
    //跳出表單
    var content="";
    content += '<form>';
    content += '<div class="form-group"><label class="col-form-label">教室ID：<input type="text" class="form-control" id="classroom_id" value="教室ID ex.R-001"></label></div></form>';
    
    document.getElementById("myContent").innerHTML = content;
    document.getElementById("exampleModalLabel").innerHTML = "刪除教室";
    document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancle</button>'
        +'<button id="submit" type="button" class="btn btn-primary" onclick="delRoom()" data-dismiss="modal">Submit</button>';
}

//把刪除的教室ID傳到後端 有ajax
function delRoom(){
    console.log("id: "+$("#classroom_id").val());
    var myURL = ngrok + "delete_cs_classroom_info?classroom_id="+$("#classroom_id").val();
    console.log("myURL: "+myURL);
    $.ajax({
        url: myURL,
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            if(response[i].message == undefined){
                init();
            }
            else{
                window.alert("出了點錯，請稍後再試！");
            }
        }
    });
}

function start(){
    init();
    setSideBar();
}

window.addEventListener("load", start, false);
