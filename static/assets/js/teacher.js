            var courseid=0;
            var courseidArray= new Array();
            window.onload = function init(){
                        setSchedule();
                        setSideBar();
                        $.ajax({
                    
                    url: api_schedule, //放你的url，這裡先放本地端檔案
                    //url: "teacher.json",
                    type: "GET",
                    dataType: "json",
                    contentType: 'application/json; charset=utf-8',
                    
                    //如果成功的話
                    success: function(data){//這裡拿到的data是一個Object陣列
                        console.log("success");
                        test(data);
                        for(var i=0; i<data.length; i++){
                            //利用key去找value
                            
                            console.log("time: "+data[i].time.slice(0,2));
                            console.log("name: "+data[i].course);
                        }//看到時候有沒有成功
                    },
                    
                    //如果失敗的話
                    error: function(){
                        console.log("error");
                    }
                });
                        //localStorage.clear();
                        //setInfo();
                        //test();
                        $.ajax({
                    
                   url: api_personal_info, //放你的url，這裡先放本地端檔案
                     //url: "info.json",
                    type: "GET",
                    dataType: "json",
                    contentType: 'application/json; charset=utf-8',
                    
                    //如果成功的話
                    success: function(data){//這裡拿到的data是一個Object陣列
                        console.log("success");
                        setInfo(data);
                            console.log("time: "+data.user_id);
                            console.log("name: "+data.name);
                            console.log("phone: "+data.phone);
                            console.log("email: "+data.email);
                            console.log("email: "+data.major);
                    },
                    
                    //如果失敗的話
                    error: function(){
                        console.log("error");
                    }
                });
                    }
                    function setInfo(data){
                            document.getElementById("teacherinfo").innerHTML= "<h2>帳號: " + data.user_id + "</h2><h2>姓名: " + data.name + "</h2><h2>電話: " + data.phone + "</h2><h2>信箱: " + data.email + "</h2><h2>專業: " + data.major + "</h2>";
                    }
                    function setCourseID(id){
                        sessionStorage.setItem("course",id);
            }

                    function setSchedule(){
                        var t = document.getElementById("teacherschedule").getElementsByTagName("tbody");
                        var rows = "";
                        var time = [ "上午" , "下午" , "晚上" ];
                        var week = ["Mon" , "Tue" , "Wed" , "Thr" , "Fri" , "Sat" , "Sun"];
                        for(var i=0; i<3; i++){
                                rows += "<tr><td>" + time[i] + "</td>";
                                for(var j=0; j<7; j++){
                                        rows += "<td id='" + i + "-" + week[j] + "'></td>";
                                }
                                rows += "</tr>"
                        }
                        t[0].innerHTML = rows;
                    }

                    function test(data){
                        
                        for(var k=0; k<data.length; k++){
                           courseidArray[k]=data[k].course_id;
                           console.log(courseidArray[k]);
                       }
                        
                        for(var i=0; i<data.length; i++){
                        if(data[i].time.slice(0,2) < 12){
                            var tempID = courseidArray[i];
                            document.getElementById("0-"+ data[i].time.slice(-3)).innerHTML += '<a href="'+url_teacher_courseinfo+'" id="' + courseidArray[i] + '" onclick="setCourseID('+"'"+tempID+"'"+')" >'+data[i].time.slice(0,11)+"<br>"+data[i].course+"</a>";
                            
                            
                        }
                        else if(data[i].time.slice(0,2) > 12 && data[i].time.slice(0,2) < 18){
                            var tempID = courseidArray[i];
                            console.log(tempID);
                            document.getElementById("1-"+ data[i].time.slice(-3)).innerHTML += '<a href="'+url_teacher_courseinfo+'" id="' + courseidArray[i] + '" onclick="setCourseID('+"'"+tempID+"'"+')" >'+data[i].time.slice(0,11)+"<br>"+data[i].course+"</a>";
                        }
                        else {
                           
                            var tempID = courseidArray[i];
                            document.getElementById("2-"+ data[i].time.slice(-3)).innerHTML += '<a href="'+url_teacher_courseinfo+'" id="' + courseidArray[i] + '" onclick="setCourseID('+"'"+tempID+"'"+')" >'+data[i].time.slice(0,11)+"<br>"+data[i].course+"</a>";
                        }
                        }
                    }

                    

                    
