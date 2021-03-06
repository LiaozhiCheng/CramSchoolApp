function sendLoginRequest(){
	var user_id = document.getElementById("user_id").value;
	var password = document.getElementById("password").value;
	var loginInfo = { "user_id" : user_id, "password" : password };
	
	$.ajax({
		url: "/login_user",
		type: "POST",
		data: JSON.stringify(loginInfo),
		dataType: "json",
		contentType: "application/json;charset=utf-8",
		
		success: function(data){
			var role = data.role;
			if(role == "student"){
				window.location.href = "student";
			}
			else if(role == "teacher"){
				window.location.href = "teacher";
			}
			else if(role == "boss"){
				window.location.href = "cramschool";
			}
		},
		error: function(){
			var target = document.getElementById("alert");
			target.className = "alert alert-danger ";
			target.setAttribute("role", "alert");
			target.innerHTML = "帳號密碼錯誤";
			console.log("login error!!");
		}
	});
	
}