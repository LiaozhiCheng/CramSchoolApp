from . import SettingBase
from flask import url_for
from datetime import datetime
import json
#from flask_login import current_user, login_required, login_user


class CheckStudentAPI(SettingBase):

   

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


