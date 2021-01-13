from . import SettingBase
from flask import url_for
class CheckStudentAPI(SettingBase):
    user_id = '110-S-011'
    password = '011'
    
    def test_schedule(self):
        self.user_id = '110-T-001'
        self.password = '001'
        self.signin()
        response = self.client.get(url_for('user_api.user_schedule'),follow_redirects=True)
        expected_output = [{ "course" :  "1101地理" , "time" : "17:00~19:00-Sat" }]
        self.assertEquals(response.json, expected_output)
    
    def test_personal_info_1(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        response = self.client.get(url_for('user_api.user_personal_info'),follow_redirects=True)
        expected_output = {"user_id" : "110-S-011",
                          "name" : "安東‧施密特",
                          "phone" : "0991682462",
                          "email" : "S011@gmail.com.tw",
                          "role" : "student" }
        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.data, expected_output)
        
    def test_course_info(self):
        response = self.client.get(url_for('user_api.course_info') + "/?course_id=C-019")
        expected_output = {"course" : "1101化學",
                  "teacher" : "佩姬‧莫斯利",
                  "summary" : "",
                  "classroom" : "CS087"}
        
        self.assertEquals(response.json, expected_output)
        
    def test_student_course_progress(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        response = self.client.get(url_for('student_api.stu_course_progress') + "/?course_id=C-019")
        expected_output = [{ "lesson_time" : "Tue, 01 Sep 2020 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 08 Sep 2020 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 15 Sep 2020 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 22 Sep 2020 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 29 Sep 2020 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 06 Oct 2020 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 13 Oct 2020 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 20 Oct 2020 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 27 Oct 2020 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 03 Nov 2020 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 10 Nov 2020 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 17 Nov 2020 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 24 Nov 2020 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 01 Dec 2020 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 08 Dec 2020 00:00:00 GMT" , "progress" : "" }]
        
        self.assertEquals(response.json, expected_output)
        
    
    def test_student_course_homework(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        response = self.client.get(url_for('student_api.stu_course_homework') + "/?course_id=C-019")
        expected_output = [{ "lesson_time" : "Tue, 01 Sep 2020 00:00:00 GMT" , "homework" : "" , "deadline" : "Mon, 01 Feb 2021 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 08 Sep 2020 00:00:00 GMT" , "homework" : "" , "deadline" : "Mon, 01 Feb 2021 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 15 Sep 2020 00:00:00 GMT" , "homework" : "" , "deadline" : "Mon, 01 Feb 2021 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 22 Sep 2020 00:00:00 GMT" , "homework" : "" , "deadline" : "Mon, 01 Feb 2021 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 29 Sep 2020 00:00:00 GMT" , "homework" : "" , "deadline" : "Mon, 01 Feb 2021 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 06 Oct 2020 00:00:00 GMT" , "homework" : "" , "deadline" : "Mon, 01 Feb 2021 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 13 Oct 2020 00:00:00 GMT" , "homework" : "" , "deadline" : "Mon, 01 Feb 2021 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 20 Oct 2020 00:00:00 GMT" , "homework" : "" , "deadline" : "Mon, 01 Feb 2021 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 27 Oct 2020 00:00:00 GMT" , "homework" : "" , "deadline" : "Mon, 01 Feb 2021 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 03 Nov 2020 00:00:00 GMT" , "homework" : "" , "deadline" : "Mon, 01 Feb 2021 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 10 Nov 2020 00:00:00 GMT" , "homework" : "" , "deadline" : "Mon, 01 Feb 2021 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 17 Nov 2020 00:00:00 GMT" , "homework" : "" , "deadline" : "Mon, 01 Feb 2021 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 24 Nov 2020 00:00:00 GMT" , "homework" : "" , "deadline" : "Mon, 01 Feb 2021 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 01 Dec 2020 00:00:00 GMT" , "homework" : "" , "deadline" : "Mon, 01 Feb 2021 00:00:00 GMT" , "progress" : "" },
                { "lesson_time" : "Tue, 08 Dec 2020 00:00:00 GMT" , "homework" : "" , "deadline" : "Mon, 01 Feb 2021 00:00:00 GMT" , "progress" : "" }]
        
        self.assertEquals(response.json, expected_output)


    # def test_student_course_grade(self):
    #     self.user_id = '110-S-011'
    #     self.password = '011'
    #     self.signin()
    #     response = self.client.get(url_for('student_api.stu_course_grade') + "/?course_id=C-019")
    #     expected_output = [{ "quiz_date" : "Tue, 01 Sep 2020 00:00:00 GMT" , "quiz_name" : "test0" , "grade" : "60" },
    #          { "quiz_date" : "Tue, 08 Sep 2020 00:00:00 GMT" , "quiz_name" : "test1" , "grade" : "82" },
    #          { "quiz_date" : "Tue, 15 Sep 2020 00:00:00 GMT" , "quiz_name" : "test2" , "grade" : "82" },
    #          { "quiz_date" : "Tue, 22 Sep 2020 00:00:00 GMT" , "quiz_name" : "test3" , "grade" : "77" },
    #          { "quiz_date" : "Tue, 29 Sep 2020 00:00:00 GMT" , "quiz_name" : "test4" , "grade" : "73" },
    #          { "quiz_date" : "Tue, 06 Oct 2020 00:00:00 GMT" , "quiz_name" : "test5" , "grade" : "81" },
    #          { "quiz_date" : "Tue, 13 Oct 2020 00:00:00 GMT" , "quiz_name" : "test6" , "grade" : "79" },
    #          { "quiz_date" : "Tue, 20 Oct 2020 00:00:00 GMT" , "quiz_name" : "test7" , "grade" : "61" },
    #          { "quiz_date" : "Tue, 27 Oct 2020 00:00:00 GMT" , "quiz_name" : "test8" , "grade" : "66" },
    #          { "quiz_date" : "Tue, 03 Nov 2020 00:00:00 GMT" , "quiz_name" : "test9" , "grade" : "89" },
    #          { "quiz_date" : "Tue, 10 Nov 2020 00:00:00 GMT" , "quiz_name" : "test10" , "grade" : "64" },
    #          { "quiz_date" : "Tue, 17 Nov 2020 00:00:00 GMT" , "quiz_name" : "test11" , "grade" : "76" },
    #          { "quiz_date" : "Tue, 24 Nov 2020 00:00:00 GMT" , "quiz_name" : "test12" , "grade" : "86" },
    #          { "quiz_date" : "Tue, 01 Dec 2020 00:00:00 GMT" , "quiz_name" : "test13" , "grade" : "100" },
    #          { "quiz_date" : "Tue, 08 Dec 2020 00:00:00 GMT" , "quiz_name" : "test14" , "grade" : "79" }] 
        
    #     self.assertEquals(response.json, expected_output)

    # def test_student_course_attendence(self):
    #     self.user_id = '110-S-011'
    #     self.password = '011'
    #     self.signin()
    #     response = self.client.get(url_for('student_api.stu_course_attendence') + "/?course_id=C-019")
    #     expected_output = [{"lesson_time" : "Tue, 01 Sep 2020 00:00:00 GMT" , "lesson_progress" : "" , "state" : "true" },
    #               {"lesson_time" : "Tue, 08 Sep 2020 00:00:00 GMT" , "lesson_progress" : "" , "state" : "true" },
    #               {"lesson_time" : "Tue, 15 Sep 2020 00:00:00 GMT" , "lesson_progress" : "" , "state" : "true" },
    #               {"lesson_time" : "Tue, 22 Sep 2020 00:00:00 GMT" , "lesson_progress" : "" , "state" : "true" },
    #               {"lesson_time" : "Tue, 29 Sep 2020 00:00:00 GMT" , "lesson_progress" : "" , "state" : "true" },
    #               {"lesson_time" : "Tue, 06 Oct 2020 00:00:00 GMT" , "lesson_progress" : "" , "state" : "true" },
    #               {"lesson_time" : "Tue, 13 Oct 2020 00:00:00 GMT" , "lesson_progress" : "" , "state" : "true" },
    #               {"lesson_time" : "Tue, 20 Oct 2020 00:00:00 GMT" , "lesson_progress" : "" , "state" : "true" },
    #               {"lesson_time" : "Tue, 27 Oct 2020 00:00:00 GMT" , "lesson_progress" : "" , "state" : "true" },
    #               {"lesson_time" : "Tue, 03 Nov 2020 00:00:00 GMT" , "lesson_progress" : "" , "state" : "true" },
    #               {"lesson_time" : "Tue, 10 Nov 2020 00:00:00 GMT" , "lesson_progress" : "" , "state" : "true" },
    #               {"lesson_time" : "Tue, 17 Nov 2020 00:00:00 GMT" , "lesson_progress" : "" , "state" : "true" },
    #               {"lesson_time" : "Tue, 24 Nov 2020 00:00:00 GMT" , "lesson_progress" : "" , "state" : "true" },
    #               {"lesson_time" : "Tue, 01 Dec 2020 00:00:00 GMT" , "lesson_progress" : "" , "state" : "true" },
    #               {"lesson_time" : "Tue, 08 Dec 2020 00:00:00 GMT" , "lesson_progress" : "" , "state" : "true" }]
        
    #     self.assertEquals(response.context['lesson_time'], expected_output)

    # def stu_course_personal_plan(self):
    #     response = self.client.get(url_for('user_api.course_info') ,course_id = "C-019")
    #     expected_output = 
        
    #     self.assertEqual(response.json, expected_output)


    # def stu_miss_lesson(self):
    #     response = self.client.get(url_for('user_api.course_info') ,course_id = "C-019")
    #     expected_output = 
        
    #     self.assertEqual(response.json, expected_output)
        
        
    # def stu_reschedule_list(self):
    #     response = self.client.get(url_for('user_api.course_info') ,course_id = "C-019")
    #     expected_output = 
        
    #     self.assertEqual(response.json, expected_output)
        
        

    # def add_reservation(self):
    #     response = self.client.get(url_for('user_api.course_info') ,course_id = "C-019")
    #     expected_output = 
        
    #     self.assertEqual(response.json, expected_output)
        
        
    
    # def cancel_reservation(self):
    #     response = self.client.get(url_for('user_api.course_info') ,course_id = "C-019")
    #     expected_output = 
        
    #     self.assertEqual(response.json, expected_output)
        
        