window.onload = function(){
    getStudentInfo();
    getAllCourse();
}

//所有課程列表
var allCourse = new Array();
//某學生所有之課程
var studentCourse = {"id" : new Array(), "name" : new Array()};


function edit(){
    var content="";
    //name = document.getElementById(id+"_name").innerText,
    //phone = document.getElementById(id+"_phone").innerText,
    //email = document.getElementById(id+"_email").innerText,
    //course = document.getElementById(id+"_course").innerText;
    var name = "麗賈娜‧信斯", phone = "0980534988", 
        email = "S085@gmail.com.tw";
    
    document.getElementById("exampleModalLabel").innerHTML = "編輯成員";
    
     content += '<form>';
    //填名字 id="user_name"
    content += '<div class="form-group"><label class="col-form-label">名字：<input type="text" class="form-control" id="user_name" value="'+name+'"></label></div>';
    //填電話 id="phone"
    content += '<div class="form-group"><label class="col-form-label">電話：<input type="tel" class="form-control" id="phone" value="'+phone+'" pattern="\d{10}"></label></div>';
    //填email id="email"
    content += '<div class="form-group"><label class="col-form-label">email：<input type="email" class="form-control" id="teacher" value="'+email+'"></label></div>';
    
    //courses
    content += '<div class="form-group"><label class="col-form-label">課程：</label>'

	//條列所有課程
	for(i=0; i<allCourse.length; i++){
		content += "<div class='d-flex justify-content-center row w-100'>"
				//設置label
				+ "<label for='" + allCourse[i].id + "' class='col-9'>" 
				+ allCourse[i].name + "-" + allCourse[i].teacher + "</label>"
				+ "<div class='col-3'>"
				//設置input: id = courseID
				+ "<input type='checkbox' id='" + allCourse[i].id + "'";
		
		//若學生已有該課程，則設置為checked
		if(studentCourse.id.includes(allCourse[i].id)){
			console.log(allCourse[i].id);
			content += " checked";
		}
		content += " onclick='editCourse(this)'></div></div>";
	}
    content += "</div></form>";
    document.getElementById("myContent").innerHTML = content;
}



//更動課程之後的判斷（未完成）：是否新增課程?是否刪除課程?
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


function getAllCourse(){
    $.ajax({
        url: "testContent/course_list.json",
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            for(var i in data){
                var one_course = {
                    "id" : data[i].course_id,
                    "name" : data[i].name,
                    "teacher" : data[i].teacher
                };
                allCourse.push(one_course);
            }
        },
        
        error: function(){
            console.log("cannot get course_list.json");
        }
    });
}

function getStudentInfo(){
    
    $.ajax({
        url: "testContent/user_detail_info.json",
        type: "GET",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        
        success: function(data){
            for(var i in data[0].course_name_list){
				studentCourse.id.push(data[0].course_list[i]);
				studentCourse.name.push(data[0].course_name_list[i]);
            }
        },
        
        error: function(){
            console.log("cannot get user_detail_info.json");
        }
    });
    
}













