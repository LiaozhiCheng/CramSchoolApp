//偵測錯誤 done

var myURL = ngrok + "cs_schedule";
setSideBar();
function createTable(data){
    console.log("data: "+data);
    var content = "";
    for(var i=0; i<data.length; i++){
        content += "<tr><td>"+data[i].course_time.slice(0,11)+"</td>"
        +"<td>"+data[i].name+"</td>"
        +"<td>"+data[i].course_id+"</td>"
        +"<td>"+data[i].teacher+"</td>"
        +"<td>"+(data[i].classroom).name+"</td></tr>"; 
    }
    document.getElementById("tbody").innerHTML = content;
}

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
