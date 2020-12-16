        window.onload = function(){
            getSavedData();
        }
        //window.addEventListener("load", getSavedData());
        function setCourseinfo(data){
                    //for(var i=0; i<data.length; i++){
                        //利用key去找value
                        document.getElementById("courseinfo").innerHTML= "<h2 class='card-text'>課程:" + data.course + "</h2><h2 class='card-text'>老師:" + data.teacher + "</h2><h2 class='card-text'>大綱:" + data.summary + "</h2><h2 class='card-text'>教室:" + data.classroom + "</h2>";
                        //console.log("time: "+data[i].user_id);
                        //console.log("name: "+data[i].name);
                        //console.log("phone: "+data[i].phone);
                        //console.log("email: "+data[i].email);
                    //}
                    }
        function getSavedData(){console.log("sss");
            try{
                var temp = sessionStorage.getItem('course');
                console.log(temp);
                $.ajax({
                url: "https://3aac3445b286.ngrok.io/user/course_info?course_id="+temp,
                //url: "courseinfo.json", //放你的url，這裡先放本地端檔案
                type: "GET",
                dataType: "json",
                contentType: 'application/json; charset=utf-8',

                success: function(data){
                    console.log(data);
                    setCourseinfo(data);
                    //for(var i=0; i<data.length; i++){
                        //利用key去找value
                        console.log("time: "+data.course);
                        console.log("name: "+data.teacher);
                        console.log("phone: "+data.summary);
                        console.log("email: "+data.classroom);
                    //}//看到時候有沒有成功
                },

                error: function(){
                    console.log('getSavedData error');
                }
            });
                //console.log(temp);*/
            }
            catch(e){
                alert("未知課程，請回課表選擇課程");
                window.location.replace("teacher.html");
            }
            
        }


               /* $.ajax({
                //url: "https://......info?course_id="+temp+"&";
                url: "courseinfo.json", //放你的url，這裡先放本地端檔案
                type: "GET",
                dataType: "json",
                contentType: 'application/json; charset=utf-8',
                
                //如果成功的話
                success: function(data){//這裡拿到的data是一個Object陣列
                    console.log("success");
                    setCourseinfo(data);
                    //for(var i=0; i<data.length; i++){
                        //利用key去找value
                        console.log("time: "+data.course);
                        console.log("name: "+data.teacher);
                        console.log("phone: "+data.summary);
                        console.log("email: "+data.classroom);
                   // }//看到時候有沒有成功
                },
                
                //如果失敗的話
                error: function(){
                    console.log("error");
                }
            });*/