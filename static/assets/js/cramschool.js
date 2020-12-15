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
        url:"https://af55163ad559.ngrok.io/cs/cs_schedule",
        //url: "coursetest.json",
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            console.log("success");
            createTable(response);
            for(var i=0; i<response.length; i++){
                console.log("time: "+response[i].course_time[3]);
                console.log("name: "+response[i].name);
                console.log("id: "+response[i].course_id);
                console.log("teacher: "+response[i].teacher);
                console.log("classroom: "+(response[i].classroom).name);
            }
        },
        error: function(){
            console.log("error");
        }
    });

