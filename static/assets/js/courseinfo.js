            window.onload = function(){
                getSavedData();
                setSideBar();
            }
            function setCourseinfo(data){
                            document.getElementById("courseinfo").innerHTML= "<h2 class='card-text'>課程:" + data.course + "</h2><h2 class='card-text'>老師:" + data.teacher + "</h2><h2 class='card-text'>教室:" + data.classroom + "</h2>";
                        }
            function getSavedData(){console.log("sss");
                try{
                    var temp = sessionStorage.getItem('course');
                    console.log(temp);
                    if(temp==null){
                                alert("未知課程，請回課表選擇課程");
                                window.location.replace(url_teacher);
                            }
                    $.ajax({
                    url: api_course_info + temp,
                    //url: "courseinfo.json", //放你的url，這裡先放本地端檔案
                    type: "GET",
                    dataType: "json",
                    contentType: 'application/json; charset=utf-8',

                    success: function(data){
                        console.log(data);
                        setCourseinfo(data);
                            console.log("time: "+data.course);
                            console.log("name: "+data.teacher);
                            console.log("phone: "+data.summary);
                            console.log("email: "+data.classroom);
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

