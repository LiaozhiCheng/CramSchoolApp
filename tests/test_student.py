from . import SettingBase
from flask import url_for
from datetime import datetime
import json
#from flask_login import current_user, login_required, login_user


class CheckStudentAPI(SettingBase):

    def test_schedule(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        response = self.client.get(
        url_for('user_api.user_schedule'), follow_redirects=True)
        expected_output = [{ "course_id" : "C-003" , "course" :  "1101歷史" , "time" : "17:00~19:00-Fri" },
                { "course_id" : "C-010" , "course" :  "1101國文" , "time" : "15:00~17:00-Mon" },
                { "course_id" : "C-011" , "course" :  "1101地理" , "time" : "17:00~19:00-Sat" },
                { "course_id" : "C-013" , "course" :  "1101軟體工程" , "time" : "17:00~19:00-Fri" },
                { "course_id" : "C-017" , "course" :  "1100數學" , "time" : "17:00~19:00-Sun" }]
        self.assertEquals(list(response.json), expected_output)
        self.logout()

    def test_personal_info(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        response = self.client.get(
            url_for('user_api.user_personal_info'), follow_redirects=True)
        expected_output = {"user_id": "110-S-011",
                           "name": "安東‧施密特",
                           "phone": "0991682462",
                           "email": "S011@gmail.com.tw",
                           "role": "student"}
        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.json, expected_output)
        self.logout()
        
    def test_personal_info_2(self):
        self.user_id = '110-T-005'
        self.password = '005'
        self.signin()
        response = self.client.get(
            url_for('user_api.user_personal_info'), follow_redirects=True)
        expected_output = {"user_id" : "110-T-005",
                          "name" : "安東尼‧蓋茨",
                          "phone" : "0956085980",
                          "email" : "T005@gmail.com.tw",
                          "major" : [ "歷史" , "數學" , "物理" , "地科" , "英文" , "軟體工程" , "地理" ],
                          "role" : "teacher"}
        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.json, expected_output)
        self.logout()

    def test_course_info(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        response = self.client.get(
            url_for('user_api.course_info') + "?course_id=C-003")
        expected_output = {"course" : "1101歷史",
                           "teacher" : "安東尼‧蓋茨",
                           "summary" : "",
                           "classroom" : "ANTH213"}

        self.assertEquals(response.json, expected_output)
        self.logout()

    def test_student_course_progress(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        response = self.client.get(
            url_for('student_api.stu_course_progress') + "?course_id=C-003")
        expected_output = [{ "lesson_time" : "Tue, 01 Sep 2020 00:00:00 GMT" , "progress" : "歷史第一課" },
                { "lesson_time" : "Tue, 08 Sep 2020 00:00:00 GMT" , "progress" : "歷史第二課" },
                { "lesson_time" : "Tue, 15 Sep 2020 00:00:00 GMT" , "progress" : "歷史第三課" },
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
        self.logout()

    def test_student_course_homework(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        response = self.client.get(
            url_for('student_api.stu_course_homework') + "?course_id=C-003")
        expected_output = [{ "lesson_time" : "Tue, 01 Sep 2020 00:00:00 GMT" , "homework" : "習作p1~p5" , "deadline" : "Wed, 27 Jan 2021 00:00:00 GMT" , "progress" : "歷史第一課" },
                { "lesson_time" : "Tue, 08 Sep 2020 00:00:00 GMT" , "homework" : "習作p6~p10" , "deadline" : "Mon, 01 Feb 2021 00:00:00 GMT" , "progress" : "歷史第二課" },
                { "lesson_time" : "Tue, 15 Sep 2020 00:00:00 GMT" , "homework" : "習作p11~p15" , "deadline" : "Thu, 07 Jan 2021 00:00:00 GMT" , "progress" : "歷史第三課" },
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
        self.logout()

    def test_student_course_grade(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        response = self.client.get(
            url_for('student_api.stu_course_grade') + "?course_id=C-003")
        expected_output = [{ "quiz_date" : "Tue, 08 Sep 2020 00:00:00 GMT" , "quiz_name" : "test1" , "grade" : 68 },
             { "quiz_date" : "Tue, 15 Sep 2020 00:00:00 GMT" , "quiz_name" : "test2" , "grade" : 75 },
             { "quiz_date" : "Tue, 22 Sep 2020 00:00:00 GMT" , "quiz_name" : "test3" , "grade" : 95 },
             { "quiz_date" : "Tue, 29 Sep 2020 00:00:00 GMT" , "quiz_name" : "test4" , "grade" : 92 },
             { "quiz_date" : "Tue, 06 Oct 2020 00:00:00 GMT" , "quiz_name" : "test5" , "grade" : 78 },
             { "quiz_date" : "Tue, 13 Oct 2020 00:00:00 GMT" , "quiz_name" : "test6" , "grade" : 71 },
             { "quiz_date" : "Tue, 20 Oct 2020 00:00:00 GMT" , "quiz_name" : "test7" , "grade" : 97 },
             { "quiz_date" : "Tue, 27 Oct 2020 00:00:00 GMT" , "quiz_name" : "test8" , "grade" : 81 },
             { "quiz_date" : "Tue, 03 Nov 2020 00:00:00 GMT" , "quiz_name" : "test9" , "grade" : 92 },
             { "quiz_date" : "Tue, 10 Nov 2020 00:00:00 GMT" , "quiz_name" : "test10" , "grade" : 92 },
             { "quiz_date" : "Tue, 17 Nov 2020 00:00:00 GMT" , "quiz_name" : "test11" , "grade" : 91 },
             { "quiz_date" : "Tue, 24 Nov 2020 00:00:00 GMT" , "quiz_name" : "test12" , "grade" : 61 },
             { "quiz_date" : "Tue, 01 Dec 2020 00:00:00 GMT" , "quiz_name" : "test13" , "grade" : 70 },
             { "quiz_date" : "Tue, 08 Dec 2020 00:00:00 GMT" , "quiz_name" : "test14" , "grade" : 88 }]
        self.assertEquals(response.json, expected_output)
        self.logout()

    def test_student_course_attendence(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        response = self.client.get(
            url_for('student_api.stu_course_attendence') + "?course_id=C-003")
        expected_output = [{ "lesson_time" : "Tue, 01 Sep 2020 00:00:00 GMT" , "progress" : "歷史第一課" , "state" : False },
                  { "lesson_time" : "Tue, 08 Sep 2020 00:00:00 GMT" , "progress" : "歷史第二課" , "state" : True },
                  { "lesson_time" : "Tue, 15 Sep 2020 00:00:00 GMT" , "progress" : "歷史第三課" , "state" : True },
                  { "lesson_time" : "Tue, 22 Sep 2020 00:00:00 GMT" , "progress" : "" , "state" : True },
                  { "lesson_time" : "Tue, 29 Sep 2020 00:00:00 GMT" , "progress" : "" , "state" : True },
                  { "lesson_time" : "Tue, 06 Oct 2020 00:00:00 GMT" , "progress" : "" , "state" : True },
                  { "lesson_time" : "Tue, 13 Oct 2020 00:00:00 GMT" , "progress" : "" , "state" : True },
                  { "lesson_time" : "Tue, 20 Oct 2020 00:00:00 GMT" , "progress" : "" , "state" : True },
                  { "lesson_time" : "Tue, 27 Oct 2020 00:00:00 GMT" , "progress" : "" , "state" : True },
                  { "lesson_time" : "Tue, 03 Nov 2020 00:00:00 GMT" , "progress" : "" , "state" : True },
                  { "lesson_time" : "Tue, 10 Nov 2020 00:00:00 GMT" , "progress" : "" , "state" : True },
                  { "lesson_time" : "Tue, 17 Nov 2020 00:00:00 GMT" , "progress" : "" , "state" : True },
                  { "lesson_time" : "Tue, 24 Nov 2020 00:00:00 GMT" , "progress" : "" , "state" : True },
                  { "lesson_time" : "Tue, 01 Dec 2020 00:00:00 GMT" , "progress" : "" , "state" : True },
                  { "lesson_time" : "Tue, 08 Dec 2020 00:00:00 GMT" , "progress" : "" , "state" : True }]
        self.assertEquals(response.json, expected_output)
        self.logout()

    def test_course_personal_plan(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        response = self.client.get(url_for('student_api.stu_course_personal_plan') + "?course_id=C-003")
        expected_output = [{ "context" : "考卷未訂正完成，下次交" , "deadline" : "Sat, 05 Sep 2020 00:00:00 GMT" , "lesson_time" : "Tue, 01 Sep 2020 00:00:00 GMT" , "progress" : "歷史第一課" },
            { "context" : "上課不認真，抄課本p1~5兩遍" , "deadline" : "Fri, 18 Sep 2020 00:00:00 GMT" , "lesson_time" : "Tue, 15 Sep 2020 00:00:00 GMT" , "progress" : "歷史第三課" },
            { "context" : "上次作業未完成，下次補交" , "deadline" : "Sun, 25 Oct 2020 00:00:00 GMT" , "lesson_time" : "Tue, 20 Oct 2020 00:00:00 GMT" , "progress" : "" }]
        self.assertEqual(response.json, expected_output)
        self.logout()

    def test_miss_lesson(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        response = self.client.get(url_for('student_api.stu_miss_lesson') + "?course_id=C-003")
        expected_output = [{ "course_name" : "1101歷史" ,'miss_lessons': [{'lesson_id': 'L-003-000', 'progress': '歷史第一課'}]}]
        self.assertEqual(response.json, expected_output)
        self.logout()


    def test_reschedule_list(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        response = self.client.get(url_for('student_api.stu_reschedule_list') + "?course_id=C-003")
        expected_output = [
              {"course_name": "", "datetime": "2021-01-11+1-19", "lesson_id": "", "progress": "", "state": "available"}, 
              {"course_name": "", "datetime": "2021-01-13+3-19", "lesson_id": "", "progress": "", "state": "available"}, 
              {"course_name": "", "datetime": "2021-01-14+4-17", "lesson_id": "", "progress": "", "state": "available"}, 
              {"course_name": "", "datetime": "2021-01-14+4-19", "lesson_id": "", "progress": "", "state": "available"}, 
              {"course_name": "", "datetime": "2021-01-15+5-19", "lesson_id": "", "progress": "", "state": "available"}, 
              {"course_name": "", "datetime": "2021-01-17+0-17", "lesson_id": "", "progress": "", "state": "available"}]
        self.assertEqual(response.json, expected_output)
        self.logout()

    def test_add_reservation(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        input_data = {
                "course_name" : "1101歷史",
                "lesson_id" : "L-003-000",
                "datetime" : "2021-01-11+1-19"}
        
        response = self.client.post(url_for('student_api.add_reservation'),data = json.dumps(input_data), content_type="application/json")
        expected_output ={
                            "user_id" : "110-S-011",
                            "datetime" : "Mon, 11 Jan 2021 19:00:00 GMT",
                            "course_name" : "1101歷史",
                            "lesson_id" : "L-003-000"
                            }
        self.assertEqual(response.json, expected_output)
        self.logout()

    def test_add_reservation_2(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        input_data = {
                "course_name" : "1101歷史",
                "lesson_id" : "",
                "datetime" : "2021-01-11+1-19"}
        
        response = self.client.post(url_for('student_api.add_reservation'),data = json.dumps(input_data), content_type="application/json")
        expected_output = {"message" : "資料不得為空"}
        self.assertEqual(response.json, expected_output)
        self.logout()
        
    def test_cancel_reservation(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        input_data = {
                    "user_id" : '110-S-011',
                    "datetime" : "2021-01-11+1-19",
                    "course_name" : "1101歷史",
                    "lesson_id" : "L-003-000"
        }
        response = self.client.post(url_for('student_api.cancel_reservation'),
                                    data = json.dumps(input_data), content_type="application/json")
        expected_output = {
                    "user_id" : '110-S-011',
                    "datetime" : "Mon, 11 Jan 2021 19:00:00 GMT",
                    "course_name" : "1101歷史",
                    "lesson_id" : "L-003-000"
        }
        self.assertEqual(response.json, expected_output)
        self.logout()
        
    def test_cancel_reservation_2(self):
        self.user_id = '110-S-011'
        self.password = '011'
        self.signin()
        input_data = {
                    "user_id" : '110-S-011',
                    "datetime" : "2021-01-11+1-19",
                    "course_name" : "1101歷史",
                    "lesson_id" : ""
        }
        response = self.client.post(url_for('student_api.cancel_reservation'),
                                    data = json.dumps(input_data), content_type="application/json")
        expected_output = {"message" : "資料不得為空"}
        self.assertEqual(response.json, expected_output)
        self.logout()

