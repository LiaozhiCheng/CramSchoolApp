
from . import SettingBase
from flask import url_for
import json
 
#測試cs_api
#Todo
class CheckCramSchoolAPI(SettingBase):
    def test_cs_schedule(self):
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_schedule.json', 'r') as file:
            data = json.load(file)
            print("data: ")
            print(data)
        response = self.client.get(url_for('cs_api.cs_schedule'))
        print(response.json)
        self.assertEquals(response.json, data)
    """
    def test_stu_member_list(self):
        response = self.client.get(url_for('cs_api.stu_member_list'))
        self.assertEquals(response.json, list())
    def test_tea_member_list(self):
        response = self.client.get(url_for('cs_api.tea_member_list'))
        self.assertEquals(response.json, list())
    def test_user_detail_info(self):
        response = self.client.get(url_for('cs_api.user_detail_info'))
        self.assertEquals(response.json, list())
    def test_insert_user_detail_info(self):
        response = self.client.get(url_for('cs_api.insert_user_detail_info'))
        self.assertEquals(response.json, list())
    def test_delete_user_detail_info(self):
        response = self.client.get(url_for('cs_api.delete_user_detail_info'))
        self.assertEquals(response.json, list())
    def test_edit_user_detail_info(self):
        response = self.client.get(url_for('cs_api.edit_user_detail_info'))
        self.assertEquals(response.json, list())
    def test_cs_course_list(self):
        response = self.client.get(url_for('cs_api.cs_course_list'))
        self.assertEquals(response.json, list())
    def test_cs_course_info_by_name(self):
        response = self.client.get(url_for('cs_api.cs_course_info_by_name'))
        self.assertEquals(response.json, list())
    def test_cs_course_student_list(self):
        response = self.client.get(url_for('cs_api.cs_course_student_list'))
        self.assertEquals(response.json, list())
    def test_insert_cs_course_info(self):
        response = self.client.get(url_for('cs_api.insert_cs_course_info'))
        self.assertEquals(response.json, list())
    def test_delete_cs_course_info(self):
        response = self.client.get(url_for('cs_api.delete_cs_course_info'))
        self.assertEquals(response.json, list())
    def test_edit_cs_course_info(self):
        response = self.client.get(url_for('cs_api.edit_cs_course_info'))
        self.assertEquals(response.json, list())
    def test_cs_course_attendence(self):
        response = self.client.get(url_for('cs_api.cs_course_attendence'))
        self.assertEquals(response.json, list())
    def test_cs_student_attendence(self):
        response = self.client.get(url_for('cs_api.cs_student_attendence'))
        self.assertEquals(response.json, list())
    def test_edit_cs_course_attendence(self):
        response = self.client.get(url_for('cs_api.edit_cs_course_attendence'))
        self.assertEquals(response.json, list())
    def test_cs_classroom_info(self):
        response = self.client.get(url_for('cs_api.cs_classroom_info'))
        self.assertEquals(response.json, list())
    def test_cs_classroom_list(self):
        response = self.client.get(url_for('cs_api.cs_classroom_list'))
        self.assertEquals(response.json, list())
    def test_cs_classroom_info_by_name(self):
        response = self.client.get(url_for('cs_api.cs_classroom_info_by_name'))
        self.assertEquals(response.json, list())
    def test_insert_cs_classroom_info(self):
        response = self.client.get(url_for('cs_api.insert_cs_classroom_info'))
        self.assertEquals(response.json, list())
    def test_delete_cs_classroom_info(self):
        response = self.client.get(url_for('cs_api.delete_cs_classroom_info'))
        self.assertEquals(response.json, list())
    def test_edit_cs_classroom_info(self):
        response = self.client.get(url_for('cs_api.edit_cs_classroom_info'))
        self.assertEquals(response.json, list())
    def test_cs_reschedule_list(self):
        response = self.client.get(url_for('cs_api.cs_reschedule_list'))
        self.assertEquals(response.json, list())
    def test_cs_reschedule_info(self):
        response = self.client.get(url_for('cs_api.cs_reschedule_info'))
        self.assertEquals(response.json, list())
    def test_edit_cs_reschedule_list(self):
        response = self.client.get(url_for('cs_api.edit_cs_reschedule_list'))
        self.assertEquals(response.json, list())
    def test_cs_lesson_id_and_time(self):
        response = self.client.get(url_for('cs_api.cs_lesson_id_and_time'))
        self.assertEquals(response.json, list())
"""

        