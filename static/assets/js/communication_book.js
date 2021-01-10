                var ss=0;
                var date= new Array();
                var lessonid= new Array();
                window.onload = function(){
                    getSavedData();
                    setSideBar();
                }
                    function getSavedData(){
                        
                    try{
                        temp=sessionStorage.getItem('course');
                        //console.log("sss");
                        //settemp();
                        //console.log("qqq");
                        //var temp = sessionStorage.getItem('course');
                        console.log(temp);
                        if(temp==null){
                            alert("未知課程，請回課表選擇課程");
                            window.location.replace(url_teacher);
                        }

                        $.ajax({
                        url: api_communication_book + temp,
                        //url: "cb.json", //放你的url，這裡先放本地端檔案
                        type: "GET",
                        dataType: "json",
                        contentType: 'application/json; charset=utf-8',

                        success: function(data){//這裡拿到的data是一個Object陣列
                            console.log("success");
                            setSchedule(data);
                            for(var i=0; i<data.length; i++){
                                //利用key去找value
                                //console.log("time: "+data[i].lesson_time);
                                //console.log("time: "+data[i].lesson_id);
                                //console.log("deadline: "+data[i].deadline);
                                //console.log("progress: "+data[i].progress);
                                //console.log("context: "+data[i].context);
                            }//看到時候有沒有成功
                        },

                        error: function(){
                            console.log('getSavedData error');
                        }
                    });
                        
                    }
                    catch(e){
                        alert("未知課程，請回課表選擇課程");
                        window.location.replace("teacher.html");
                    }
                    
                }
                /*function settemp(){
                    console.log("qqq");
                    var temp = sessionStorage.getItem('course');}*/
                        function setSchedule(data){
                            var t = document.getElementById("cbtable").getElementsByTagName("tbody");
                            var rows = "";
                            for(var i=0; i<data.length; i++){
                                //利用key去找value
                                lessonid[i]=data[i].lesson_id;
                                date[i]=data[i].lesson_time;
                                console.log("deadline: "+data[i].deadline);
                                //console.log("progress: "+data[i].progress);
                                //console.log("context: "+data[i].context);
                            }
                           for(var i=0; i<date.length; i++){
                                    rows += "<tr><td>" + date[i] + "</td>";
                                    //for(var j=0; j<4; j++){if(j==3){
                                            rows += "<td id='" + i + "-0'>"+data[i].deadline+"</td>";
                                            rows += "<td id='" + i + "-1'>"+data[i].progress+"</td>";
                                            rows += "<td id='" + i + "-2'>"+data[i].context+"</td>";
                                            rows += "<td id='" + i + "-3'><button id='e"+ i +"' type='button' class='btn btn-primary' data-toggle='modal' data-target='#exampleModal' onclick='testedit(this.id)' >Edit</button><button id='d"+ i +"' type='button' class='btn btn-outline-danger' onclick='testdelete(this.id)'>Delete</button></td>";
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

                       function returndata(submitdeadline,submitprogress,submitcontext) {
                            console.log(ss);
                            var cb = { "lesson_id" : lessonid[ss] , "lesson_time" : date[ss]  , "deadline" : submitdeadline , "progress" : submitprogress, "context" : submitcontext };
                            console.log(cb);
                            $.ajax({
                        url: api_edit_communication_book,
                        type: "POST",
                        data: JSON.stringify(cb),
                        dataType: "json",
                        contentType: "application/json; charset=utf-8",
                        
                        success: function(data){
                            
                            
                                //利用key去找value
                                if(data.message == "資料不得為空")
                                {
                                    window.alert("資料不得為空喔~~");
                                }
                                else
                                {
                                    alert("send success!");
                                }

                            getSavedData();
                            
                        },
                        
                        error: function(){
                            alert("send error!!!");
                        }
                    });
                } 
                        function submit() {
                            //console.log(ss);
                            var submitdeadline = document.getElementById("deadline").value;
                            var submitprogress = document.getElementById("progress").value;
                            var submitcontext = document.getElementById("context").value;
                            returndata(submitdeadline,submitprogress,submitcontext);
                            //document.getElementById(ss+"-0").innerHTML=submitdeadline;
                           //document.getElementById(ss+"-1").innerHTML=submitprogress;
                            //document.getElementById(ss+"-2").innerHTML=submitcontext;
                }
                $('#submit').click(function() {
                        $('#exampleModal').modal('hide');
                });
                        function testedit(clickedid) {
                     
                    ss=clickedid.slice(1,2);
                }

                function testdelete(clickedid) {
                     //var NewStringValue=document.getElementById("message-text").value;
                    ss=clickedid.slice(1,2);
                    console.log(lessonid[ss]);
                    //returndata("","","");
                     $.ajax({
                        url: api_delete_communication_book + lessonid[ss],
                        //url: "cb.json", //放你的url，這裡先放本地端檔案
                        type: "GET",
                        dataType: "json",
                        contentType: 'application/json; charset=utf-8',

                        success: function(data){//這裡拿到的data是一個Object陣列
                            console.log("success");
                            getSavedData();
                            //看到時候有沒有成功
                        },

                        error: function(){
                            console.log('getSavedData error');
                        }
                    });
                    //document.getElementById(ss+"-0").innerHTML="";
                    //document.getElementById(ss+"-1").innerHTML="";
                    //document.getElementById(ss+"-2").innerHTML="";
                }
                      /*  $('#0').click(function() {"d"+
                            $('#0-0').text("sstt");
                        });*/
                   /* $.ajax({
                        
                        url: "cb.json", //放你的url，這裡先放本地端檔案
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
                                console.log("time: "+data[i].lesson_id);
                                console.log("deadline: "+data[i].deadline);
                                console.log("progress: "+data[i].progress);
                                console.log("context: "+data[i].context);
                            }//看到時候有沒有成功
                        },
                        
                        //如果失敗的話
                        error: function(){
                            console.log("error");
                        }
                    });*/
