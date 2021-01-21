//測試 done

//用名字查的-> sessionStorage的有：user_id, course_id
//用course_id查的-> 

function init(){    
    //拿到course&teacher
    var temp="";
    var myURL = ngrok + "cs_course_list";
    $.ajax({
        url: myURL,
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            if(response[0].message == undefined){
                for(var i=0; i<response.length; i++){
                    temp += '<option id="'+response[i].course_id+'">'+ response[i].name +" - "+response[i].teacher+"</option>";
                }
                document.getElementById("course").innerHTML = temp;
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

//選擇課程後，拿到lesson
function getLesson(data){
     
    var course_id = $(data).find("option:checked").attr("id");
    
    var temp="", myURL = ngrok + "cs_lesson_id_and_time?course_id="+course_id;
    $.ajax({
        url: myURL,
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            
            if(response[0].message == undefined){
                for(var i=0; i<response.length; i++){
                    temp += '<option id="'+ response[i].lesson_id +'">'+ response[i].lesson_time.slice(8, 11)+" "+response[i].lesson_time.slice(5, 7)+"</option>";
                }
                document.getElementById("lesson").innerHTML = temp;
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

//sessionStorage: lesson_id
function searchByLesson(){
    //拿到course_id
    var option = document.getElementById("lesson");
    var index = option.selectedIndex;
    var lesson_id = option.options[index].getAttribute("id");
    
    sessionStorage.setItem("lesson_id", lesson_id);
    getByLesson();
    
}

function getByLesson(){
    var lesson_id = sessionStorage.getItem("lesson_id");
    var temp="", myURL=ngrok+"cs_course_attendence?lesson_id="+lesson_id;
    console.log("myURL: "+myURL);
    $.ajax({
        url: myURL,
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            
            if(response[0].message == undefined){
                var content="";
                document.getElementById("date").innerHTML="<th>姓名</th><th>出席</th><th>編輯</th>";
                for(var i=0; i<response.length; i++){
                   name = Object.keys(response[i])[1];

                    attend = Object.values(response[i])[1];

                    user_id = Object.values(response[i])[0];

                    content+="<tr>";
                    //姓名
                    content+="<td>"+name+"</td>";
                    //出席
                    content+='<td id="'+user_id+'">'+attend+"</td>";

                    //編輯
                    content +='<td><button class="btn btn-secondary" type="button" data-toggle="modal" data-target="#example" onclick="edit('+"'"+user_id+"', 'lesson'"+')">編輯</button></td>';
                    content += "</tr>";
                }
                document.getElementById("tbody").innerHTML = content;
                document.getElementById("remind").innerHTML="";
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

//輸入姓名後，拿到他上的所有course
//sessionStorage: user_id
function getCourseByName(){
    
    var temp="", myURL=ngrok+"user_detail_info?name="+$("#searchName").val();
    console.log("myURL: "+myURL);
    $.ajax({
        url: myURL,
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            if(response[0].message == undefined){
                for(var i=0; i<response[0].course_list.length; i++){
                    temp += '<option id="'+(response[0].course_list)[i]+'">'+(response[0].course_name_list)[i]+"</option>";
                }
                document.getElementById("courseByName").innerHTML = temp;

               //把user_id記下來
               sessionStorage.setItem("user_id", response[0].user_id);
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

//用姓名搜尋，顯示表格
//sessionStorage: course_id
function searchByName(){
    
    //拿到course_id
    var option = document.getElementById("courseByName");
    var index = option.selectedIndex;
    var course_id = option.options[index].getAttribute("id");
    
    //把course_id記下來，等編輯完成重新顯示表格時需要
    sessionStorage.setItem("course_id", course_id);
    
    getByName();
}

//拿到出缺席紀錄(byName)
function getByName(){
    //先拿到所選擇的course_id
    var course_id = sessionStorage.getItem("course_id")
    
    //編輯表格所需的變數
    var time, attend, lesson_id, content="";
    
    var temp="", myURL = ngrok + "cs_student_attendence?user_id="+sessionStorage.getItem("user_id")+"&course_id="+course_id;
    
    console.log("myURL: "+myURL);
    $.ajax({
        url: myURL,
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            
            if(response[0].message == undefined){
                document.getElementById("date").innerHTML="<th>日期</th><th>出席</th><th>編輯</th>";
                for(var i=0; i<response.length; i++){
                   time = Object.keys(response[i])[0].slice(5, 10);

                    attend = Object.values(response[i])[0];

                    lesson_id = Object.values(response[i])[1];

                    content+="<tr>";
                    //日期
                    content+="<td>"+time+"</td>";
                    //出席
                    content+='<td id="'+lesson_id+'">'+attend+"</td>";

                    //編輯
                    content +='<td><button class="btn btn-secondary" type="button" data-toggle="modal" data-target="#example" onclick="edit('+"'"+lesson_id+"','name'"+')">編輯</button></td>';
                    content += "</tr>";
                }
            document.getElementById("tbody").innerHTML = content;
            document.getElementById("remind").innerHTML="";
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

//按下編輯按鈕後，跳出表單提供編輯
//choice = name/lesson
function edit(myID, choice){
    document.getElementById("exampleModalLabel").innerHTML = "編輯出缺席";
    document.getElementById("myContent").innerHTML = "";
    
    var attend;
    if(choice=="name"){
        sessionStorage.setItem("method", "name");
        
        attend = document.getElementById(myID).innerText;
    }
    else{
        sessionStorage.setItem("method", "lesson");
        
        
    }
    //name->找course的每堂lesson_id //course->找lesson的每個user_id
    attend = document.getElementById(myID).innerText;
    
    //跳出表單
    var content="";
    content += '<form>';
    content += '<div class="form-group">出缺席：<br><input type="radio" id="att" name="attend" value="出席"';
    
    if(attend=="出席"){
        content += ' checked>出席<br><input type="radio" id="att" name="attend" value="缺席">缺席<br></div></form>';
    }
    else{
        content += '>出席<br><input type="radio" id="att" name="attend" value="缺席" checked>缺席<br></div></form>';
    }
    
    
    document.getElementById("myContent").innerHTML = content;
    
    document.getElementById("cancleSubmit").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>'
        +'<button id="submit" type="button" class="btn btn-primary" onclick="editAtt('+"'"+myID+"'"+')" data-dismiss="modal">Submit</button>';
}

//把資料傳到後端，並且重整表格
function editAtt(myID){
    //myID 有可能是user_id or lesson_id
    var method = sessionStorage.getItem("method");
    var user_id, lesson_id;
    var isAttendence;
    if(method=="name"){
        user_id = sessionStorage.getItem("user_id");
        lesson_id = myID;
    }
    else{
        user_id = myID;
        lesson_id = sessionStorage.getItem("lesson_id");
    }

    var form = document.getElementsByName("attend");
    
    if(form[0].checked == true){
        isAttendence = 1;
    }
    else{
        isAttendence = 0;
    }
    
    var myURL = ngrok + "edit_cs_course_attendence?user_id="+user_id+"&lesson_id="+lesson_id+"&isAttendence="+isAttendence;
    console.log("myURL: "+myURL);
    $.ajax({
        url: myURL,
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            
            if(response[0].message == undefined){
                if(method=="name"){
                    getByName();
                }
                else{
                    searchByLesson();
                }
            }
            else{
                window.alert("您的資料輸入有誤，請再試一次！");
            }
            
            
        }
    });
    
    
}
            
function start(){
    init();
    setSideBar();
}

window.addEventListener("load", start, false);
