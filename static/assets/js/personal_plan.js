                    var ss=0;
                    var lessonid= new Array();
                    var addlessonid= new Array();
                    var date= new Array()
                    var studentid;
                    window.onload = function(){
                            getSavedData();
                            setSideBar();
                        }
                        function getSavedData(){
                                console.log("sss");
                            try{
                                temp = sessionStorage.getItem('course');
                                console.log(temp);
                                studentid = sessionStorage.getItem('studentId');
                                console.log(studentid);

                                $.ajax({
                                url: api_personal_plan+studentid+"&course_id="+temp,
                                //url: "personalplan.json", //放你的url，這裡先放本地端檔案
                                type: "GET",
                                dataType: "json",
                                contentType: 'application/json; charset=utf-8',

                                success: function(data){//這裡拿到的data是一個Object陣列
                                    console.log("success");
                                    setSchedule(data);
                                for(var i=0; i<data.length; i++){
                                    //利用key去找value
                                    console.log("time: "+data[i].lesson_id);
                                    console.log("time: "+data[i].lesson_time);
                                    console.log("deadline: "+data[i].deadline);
                                    console.log("context: "+data[i].context);
                                }//看到時候有沒有成功
                                },

                                error: function(){
                                    console.log('getSavedData error');
                                }
                            });
                                $.ajax({
                            //url: "studentinfo.json",
                            url: api_student_personal_info+studentid, //放你的url，這裡先放本地端檔案
                            type: "GET",
                            dataType: "json",
                            contentType: 'application/json; charset=utf-8',
                            
                            //如果成功的話
                            success: function(data){//這裡拿到的data是一個Object陣列
                                console.log("success");
                                setInfo(data);
                                //for(var i=0; i<data.length; i++){
                                    //利用key去找value
                                    console.log("time: "+data.name);
                                    console.log("name: "+data.user_id);
                                    console.log("phone: "+data.phone);
                                    console.log("email: "+data.email);
                               // }//看到時候有沒有成功
                            },
                            
                            //如果失敗的話
                            error: function(){
                                console.log("error");
                            }
                        });
                            }
                            catch(e){
                                alert("未知課程，請回課表選擇課程");
                                window.location.replace("teacher.html");
                            }
                            
                        }
                            function setInfo(data){
                                //for(var i=0; i<data.length; i++){
                                    //利用key去找value
                                    document.getElementById("studentinfo").innerHTML= "<h2>" + data.name + "</h2><h2>" + data.user_id + "</h2><h2>" + data.phone + "</h2><h2>" + data.email + "</h2>";}
                                    //console.log("time: "+data[i].user_id);
                                    //console.log("name: "+data[i].name);
                                    //console.log("phone: "+data[i].phone);
                                    //console.log("email: "+data[i].email);
                                //}
                            function returndata(submitdeadline,submitcontext) {
                                    console.log(ss);
                                    console.log(studentid);
                                    var pp = { "lesson_id" : lessonid[ss], "student_id" : studentid , "deadline" : submitdeadline , "context" : submitcontext };
                                    console.log(pp);
                                    $.ajax({
                                url: api_edit_personal_plan,
                                type: "POST",
                                data: JSON.stringify(pp),
                                dataType: "json",
                                contentType: "application/json; charset=utf-8",
                                
                                success: function(data){
                                    alert("send success!");
                                    //console.log(data);
                                    setSchedule(data);
                                },
                                
                                error: function(){
                                    alert("send error!!!");
                                }
                            });
                        } 
                            function setSchedule(data){
                                console.log("aaa");
                                var t = document.getElementById("pptable").getElementsByTagName("tbody");
                                var rows = "";
                                for(var i=0; i<data.length; i++){
                                    //利用key去找value
                                    lessonid[i]=data[i].lesson_id;
                                    date[i]=data[i].lesson_time;
                                    //console.log("deadline: "+data[i].deadline);
                                    //console.log("context: "+data[i].context);
                                }
                               for(var i=0; i<date.length; i++){
                                        rows += "<tr><td>" + date[i] + "</td>";
                                        //for(var j=0; j<4; j++){if(j==3){
                                                rows += "<td id='" + i + "-0'>"+data[i].deadline+"</td>";
                                                rows += "<td id='" + i + "-1'>"+data[i].context+"</td>";
                                                rows += "<td id='" + i + "-2'><button id='e"+ i +"' type='button' class='btn btn-primary' data-toggle='modal' data-target='#exampleModal' onclick='testedit(this.id)' >Edit</button><button id='d"+ i +"' type='button' class='btn btn-outline-danger' onclick='testdelete(this.id)'>Delete</button></td>";
                                                //}
                                                //else{
                                                //rows += "<td id='" + i + "-" + j + "'></td>";}
                                        //}
                                        rows += "</tr>"
                                }
                                t[0].innerHTML = rows;
                            }
                            //function test(){
                              //  document.getElementById("0-0").innerHTML = "國文";
                            //}
                            /*$('#exampleModal').click(function() {
                                //console.log($(this).attr('id'));
                                $('#1-2').text($('#context').val());
                                $('#1-1').text($('#progress').val());
                                $('#1-0').text($('#deadline').val());
                            });*/
                            function submit() {
                                //console.log(ss);
                        var submitdeadline = document.getElementById("deadline").value;
                        var submitcontext = document.getElementById("context").value;
                        returndata(submitdeadline,submitcontext);
                        document.getElementById(ss+"-0").innerHTML=submitdeadline;
                        document.getElementById(ss+"-1").innerHTML=submitcontext;
                        
                    }
                            function testedit(clickedid) {
                         
                        ss=clickedid.slice(1,2);
                    }
                        $('#submit').click(function() {
                        $('#exampleModal').modal('hide');
                    });
                    function testdelete(clickedid) {
                         //var NewStringValue=document.getElementById("message-text").value;
                        ss=clickedid.slice(1,2);
                        returndata("","");
                        document.getElementById(ss+"-0").innerHTML="";
                        document.getElementById(ss+"-1").innerHTML="";
                    }

                    function add(){
                        var temp="";
                        console.log("aaa");
                        $('#exampleModal2').modal('show')
                        $.ajax({
                                url: api_add_personal_plan+studentid+"&course_id="+temp,
                                //url: "time.json", //放你的url，這裡先放本地端檔案
                                type: "GET",
                                dataType: "json",
                                contentType: 'application/json; charset=utf-8',
                                
                                success: function(data){//這裡拿到的data是一個Object陣列
                                    console.log("success");
                                    //setSchedule(data);
                                    temp += "<select id='selecttime' onclick='clicktime()'>";
                                for(var i=0; i<data.length; i++){
                                    //利用key去找value
                                    addlessonid[i]=data[i].lesson_id;
                                    temp += "<option>"+data[i].lesson_time+"</option>";
                                    console.log("time: "+data[i].lesson_time);
                                }//看到時候有沒有成功
                                temp += "</select>";
                                document.getElementById("addlessontime").innerHTML = temp;
                                
                                },

                                error: function(){
                                    console.log('aaa error');
                                }
                                });
                    }

                    function addsubmit(){
                        var  addlessontime = document.getElementById("selecttime").selectedIndex;
                        var adddeadline = document.getElementById("adddeadline").value;
                        var addcontext = document.getElementById("addcontext").value;
                        var addpp = { "lesson_id" : addlessonid[addlessontime], "student_id" : studentid , "deadline" : adddeadline , "context" : addcontext };
                                    console.log(addpp);
                                    $.ajax({
                                url: api_edit_personal_plan,
                                type: "POST",
                                data: JSON.stringify(addpp),
                                dataType: "json",
                                contentType: "application/json; charset=utf-8",
                                
                                success: function(data){
                                    alert("send success!");
                                    //console.log(data);
                                    setSchedule(data);
                                },
                                
                                error: function(){
                                    alert("send error!!!");
                                }
                            });
                       // console.log(document.getElementById("addcontext").value);
                        //console.log(document.getElementById("selecttime").selectedIndex);
                    }

                    function clicktime(){
                        console.log(document.getElementById("selecttime").selectedIndex);

                    }
                          /*  $('#0').click(function() {"d"+
                                $('#0-0').text("sstt");
                            });*/
                       /* $.ajax({
                            
                            url: "personalplan.json", //放你的url，這裡先放本地端檔案
                            type: "GET",
                            dataType: "json",
                            contentType: 'application/json; charset=utf-8',
                            
                            //如果成功的話
                            success: function(data){//這裡拿到的data是一個Object陣列
                                console.log("success");
                                setSchedule(data);
                                for(var i=0; i<data.length; i++){
                                    //利用key去找value
                                    console.log("time: "+data[i].lesson_time);
                                    console.log("id: "+data[i].lesson_id);
                                    console.log("deadline: "+data[i].deadline);
                                    console.log("context: "+data[i].context);
                                }//看到時候有沒有成功
                            },
                            
                            //如果失敗的話
                            error: function(){
                                console.log("error");
                            }
                        });

                        /*$.ajax({
                            
                            url: "studentinfo.json", //放你的url，這裡先放本地端檔案
                            type: "GET",
                            dataType: "json",
                            contentType: 'application/json; charset=utf-8',
                            
                            //如果成功的話
                            success: function(data){//這裡拿到的data是一個Object陣列
                                console.log("success");
                                setInfo(data);
                                for(var i=0; i<data.length; i++){
                                    //利用key去找value
                                    console.log("time: "+data[i].student_name);
                                    console.log("name: "+data[i].student_id);
                                    console.log("phone: "+data[i].phone);
                                    console.log("email: "+data[i].email);
                                }//看到時候有沒有成功
                            },
                            
                            //如果失敗的話
                            error: function(){
                                console.log("error");
                            }
                        });*/
