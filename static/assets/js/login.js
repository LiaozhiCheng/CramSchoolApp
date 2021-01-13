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
		
		success: function(){
			console.log("login success");
		},
		error: function(){
			console.log("login error!!");
		}
	});
	
}