
from . import SettingBase
from flask import url_for
import json
 
#測試cs_api
#Todo
class CheckCramSchoolShowAPI(SettingBase):
    def test_cs_schedule(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_schedule.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
            #print("data: ")
            #print(data)
        response = self.client.get(url_for('cs_api.cs_schedule'))
        #print(response.json)
        self.assertEquals(response.json, data)
    
    def test_stu_member_list(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/stu_member_list.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.stu_member_list'))
        self.assertEquals(response.json, data)
    def test_tea_member_list(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/tea_member_list.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.tea_member_list'))
        self.assertEquals(response.json, data)
    def test_user_detail_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/user_detail_info_1.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.user_detail_info') + '?name=瑪克辛‧米蘭達')
        self.assertEquals(response.json, data)
    def test_user_detail_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/user_detail_info_2.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.user_detail_info') + '?name=慈')
        self.assertEquals(response.json, data)
    def test_user_detail_info_3(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/user_deatil_info_3.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.user_detail_info') + '?name=')
        self.assertEquals(response.json, data)
    #!
    
    
    
    def test_cs_course_list(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_course_list.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_course_list'))
        self.assertEquals(response.json, data)
    def test_cs_course_info_by_name_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_course_info_by_name_1.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_course_info_by_name') + '?name=')
        self.assertEquals(response.json, data)
    def test_cs_course_info_by_name_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_course_info_by_name_2.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_course_info_by_name') + '?name=1101數學')
        self.assertEquals(response.json, data)
    def test_cs_course_student_list_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_course_student_list_1.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_course_student_list') + '?course_id=')
        self.assertEquals(response.json, data)
    def test_cs_course_student_list_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_course_student_list_2.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_course_student_list') + '?course_id=C-005')
        self.assertEquals(response.json, data)
    #!
    
    def test_cs_course_attendence_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_course_attendence_1.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_course_attendence') + '?lesson_id=')
        self.assertEquals(response.json, data)
    def test_cs_course_attendence_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_course_attendence_2.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_course_attendence') + '?lesson_id=L-003-005')
        self.assertEquals(response.json, data)
    def test_cs_student_attendence_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_student_attendence_1.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_student_attendence') + '?user_id=&course_id=C-001')
        self.assertEquals(response.json, data)
    def test_cs_student_attendence_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_student_attendence_2.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_student_attendence') + '?user_id=110-S-012&course_id=C-001')
        self.assertEquals(response.json, data)
    
    def test_cs_classroom_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_classroom_info_1.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_classroom_info') + '?classroom_id=')
        self.assertEquals(response.json, data)
    def test_cs_classroom_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_classroom_info_2.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_classroom_info') + '?classroom_id=R-004')
        self.assertEquals(response.json, data)
    def test_cs_classroom_list(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_classroom_list.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_classroom_list'))
        self.assertEquals(response.json, data)
    def test_cs_classroom_info_by_name_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_classroom_info_by_name_1.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_classroom_info_by_name')+'?name=')
        self.assertEquals(response.json, data)
    def test_cs_classroom_info_by_name_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_classroom_info_by_name_2.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_classroom_info_by_name')+'?name=PE037')
        self.assertEquals(response.json, data)
    
    def test_cs_reschedule_list(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_reschedule_list.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_reschedule_list'))
        self.assertEquals(response.json, data)
    #!
    def test_cs_reschedule_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_reschedule_info_1.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_reschedule_info')+'?weekday=&time=21:00')
        self.assertEquals(response.json, data)
    def test_cs_reschedule_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_reschedule_info_2.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_reschedule_info')+'?weekday=Mon&time=19:00')
        self.assertEquals(response.json, data)
    def test_cs_reschedule_info_3(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_reschedule_info_3.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_reschedule_info')+'?weekday=Tue&time=19:00')
        self.assertEquals(response.json, data)
    #!
    
    def test_cs_lesson_id_and_time_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_lesson_id_and_time_1.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_lesson_id_and_time')+'?course_id=')
        self.assertEquals(response.json, data)
    def test_cs_lesson_id_and_time_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/cs_lesson_id_and_time_2.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_lesson_id_and_time')+'?course_id=C-001')
        self.assertEquals(response.json, data)


        

