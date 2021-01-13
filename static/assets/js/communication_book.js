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
                                console.log("time: "+data[i].lesson_time);
                                console.log("id: "+data[i].lesson_id);
                                console.log("deadline: "+data[i].deadline);
                                console.log("progress: "+data[i].progress);
                                console.log("context: "+data[i].context);
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
                function setSchedule(data){
                    var t = document.getElementById("cbtable").getElementsByTagName("tbody");
                    var rows = "";
                    for(var i=0; i<data.length; i++){
                        lessonid[i]=data[i].lesson_id;
                        date[i]=data[i].lesson_time;
                        console.log("deadline: "+data[i].deadline);
                    }
                    for(var i=0; i<date.length; i++){
                        rows += "<tr><td>" + date[i] + "</td>";
                        rows += "<td id='" + i + "-0'>"+data[i].deadline+"</td>";
                        rows += "<td id='" + i + "-1'>"+data[i].progress+"</td>";
                        rows += "<td id='" + i + "-2'>"+data[i].context+"</td>";
                        rows += "<td id='" + i + "-3'><button id='e"+ i +"' type='button' class='btn btn-primary' data-toggle='modal' data-target='#exampleModal' onclick='testedit(this.id)' >Edit</button><button id='d"+ i +"' type='button' class='btn btn-outline-danger' onclick='testdelete(this.id)'>Delete</button></td>";
                        rows += "</tr>"
                    }
                    t[0].innerHTML = rows;
                }

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
                            
                            console.log(data);
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
                        }
                        $('#submit').click(function() {
                            $('#exampleModal').modal('hide');
                            $('#progress').val("");
                            $('#context').val("");
                            $('#deadline').val("");
                        });
                        function testedit(clickedid) {
                           
                            ss=clickedid.slice(1,2);
                        }

                        function testdelete(clickedid) {
                            ss=clickedid.slice(1,2);
                            console.log(lessonid[ss]);
                            $.ajax({
                                url: api_delete_communication_book + lessonid[ss],
                        //url: "cb.json", //放你的url，這裡先放本地端檔案
                        type: "GET",
                        dataType: "json",
                        contentType: 'application/json; charset=utf-8',

                        success: function(data){//這裡拿到的data是一個Object陣列
                            console.log("success");
                            console.log(data);
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
                