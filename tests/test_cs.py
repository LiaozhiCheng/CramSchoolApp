
from . import SettingBase
from flask import url_for
import json
 
#測試cs_api
#Todo
class CheckCramSchoolAPI(SettingBase):
    def test_cs_schedule(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_schedule.json', 'r') as file:
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
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/stu_member_list.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.stu_member_list'))
        self.assertEquals(response.json, data)
    def test_tea_member_list(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/tea_member_list.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.tea_member_list'))
        self.assertEquals(response.json, data)
    def test_user_detail_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/user_detail_info_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.user_detail_info') + '?name=瑪克辛‧米蘭達')
        self.assertEquals(response.json, data)
    def test_user_detail_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/user_detail_info_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.user_detail_info') + '?name=慈')
        self.assertEquals(response.json, data)
    def test_user_detail_info_3(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/user_detail_info_3.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.user_detail_info') + '?name=')
        self.assertEquals(response.json, data)
    #!
    def test_insert_user_detail_info_1(self):  
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/insert_user_detail_info_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.post(url_for('cs_api.insert_user_detail_info'),
                                     follow_redirects=True,
                                    data=json.dumps({
                                        'password': '',
                                        'name': '林阿湘',
                                        'course_list':["C-001"],
                                        'phone':'0912345678',
                                        'email':'Qpatty@gmail.com',
                                        'major':'',
                                        'role':'student'
                                    }),content_type="application/json")
        self.assertEquals(response.json, data)
    def test_insert_user_detail_info_2(self):  
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/insert_user_detail_info_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.post(url_for('cs_api.insert_user_detail_info'),
                                     follow_redirects=True,
                                    data=json.dumps({
                                        'password': '123',
                                        'name': '林阿湘',
                                        'course_list':["C-001"],
                                        'phone':'0912345678',
                                        'email':'Qpatty@gmail.com',
                                        'major':'',
                                        'role':'student'
                                    }),content_type="application/json")
        self.assertEquals(response.json, data)
    def test_insert_user_detail_info_3(self):  
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/insert_user_detail_info_3.json', 'r') as file:
            data = json.load(file)
        response = self.client.post(url_for('cs_api.insert_user_detail_info'),
                                     follow_redirects=True,
                                    data=json.dumps({
                                        'password': '456',
                                        'name': '梁小慈',
                                        'course_list':["C-010"],
                                        'phone':'0912345678',
                                        'email':'Qpatty@gmail.com',
                                        'major':'',
                                        'role':'teacher'
                                    }),content_type="application/json")
        self.assertEquals(response.json, data)
    def test_delete_user_detail_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/delete_user_detail_info_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.delete_user_detail_info') + '?user_id=')
        self.assertEquals(response.json, data)
    def test_delete_user_detail_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/user_detail_info_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.delete_user_detail_info') + '?user_id=110-S-103')
        self.assertEquals(response.json, data)
    #!
    def test_edit_user_detail_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/edit_user_detail_info_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.post(url_for('cs_api.edit_user_detail_info'),
                                     follow_redirects=True,
                                    data=json.dumps({
                                        'user_id': '110_S-099',
                                        'name': '',
                                        'delete_from_course_list':[],
                                        'course_list':["C-001"],
                                        'phone':'0912345678',
                                        'email':'test@gmail.com',
                                        'major':''
                                    }),content_type="application/json")
        self.assertEquals(response.json, data)
    def test_edit_user_detail_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/edit_user_detail_info_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.post(url_for('cs_api.edit_user_detail_info'),
                                     follow_redirects=True,
                                    data=json.dumps({
                                        'user_id': '110_S-099',
                                        'name': '少安祺',
                                        'delete_from_course_list':[],
                                        'course_list':["C-003"],
                                        'phone':'0999888777',
                                        'email':'test@gmail.com',
                                        'major':''
                                    }),content_type="application/json")
        self.assertEquals(response.json, data)
    def test_cs_course_list(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_course_list.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_course_list'))
        self.assertEquals(response.json, data)
    def test_cs_course_info_by_name_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_course_info_by_name_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_course_info_by_name') + '?name=')
        self.assertEquals(response.json, list())
    def test_cs_course_info_by_name_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_course_info_by_name_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_course_info_by_name') + '?name=1101數學')
        self.assertEquals(response.json, data)
    def test_cs_course_student_list_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/course_student_list_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_course_student_list') + '?course_id=')
        self.assertEquals(response.json, data)
    def test_cs_course_student_list_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_course_student_list_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_course_student_list') + '?course_id=C-001')
        self.assertEquals(response.json, data)
    #!
    def test_insert_cs_course_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/insert_cs_course_info_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.post(url_for('cs_api.insert_cs_course_info'),
                                     follow_redirects=True,
                                    data=json.dumps({
                                        'name': '',
                                        'start_time':'2021-01-06',
                                        'course_time':'22:09~23:09-Sun',
                                        'summary':'科拉‧阮',
                                        'classroom': {'capacity':45, 'classroom_id':'R-002', 'name':'CS023'}
                                    }),content_type="application/json")
        self.assertEquals(response.json, data)
    def test_insert_cs_course_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/insert_cs_course_info_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.post(url_for('cs_api.insert_cs_course_info'),
                                     follow_redirects=True,
                                    data=json.dumps({
                                        'name': '1101軟工',
                                        'start_time':'2021-01-06',
                                        'course_time':'22:09~23:09-Sun',
                                        'summary':'科拉‧阮',
                                        'classroom':{'capacity':45, 'classroom_id':'R-002', 'name':'CS023'}
                                    }),content_type="application/json")
        self.assertEquals(response.json, data)
    def test_delete_cs_course_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/delete_cs_course_info_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.delete_cs_course_info') + '?course_id=')
        self.assertEquals(response.json, data)
    def test_delete_cs_course_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/delete_cs_course_info_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.delete_cs_course_info') + '?course_id=C-022')
        self.assertEquals(response.json, data)
    #!
    def test_edit_cs_course_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/edit_cs_course_info_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.post(url_for('cs_api.edit_cs_course_info'),
                                     follow_redirects=True,
                                    data=json.dumps({
                                        'course_id': '',
                                        'name': '測試課程-軟工',
                                        'start_time':'2021-01-06',
                                        'course_time':'22:09~23:09-Sun',
                                        'old_teacher':'科拉‧阮',
                                        'new_teacher':'測試人員-湘',
                                        'summary':'',
                                        'classroom':{'capacity':45, 'classroom_id':'R-002', 'name':'CS023'}
                                    }),content_type="application/json")
        self.assertEquals(response.json, data)
    def test_edit_cs_course_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/edit_cs_course_info_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.post(url_for('cs_api.edit_cs_course_info'),
                                     follow_redirects=True,
                                    data=json.dumps({
                                        'course_id': 'C-022',
                                        'name': '測試課程-軟工',
                                        'start_time':'2021-01-06',
                                        'course_time':'22:09~23:09-Sun',
                                        'old_teacher':'科拉‧阮',
                                        'new_teacher':'測試人員-湘',
                                        'summary':'',
                                        'classroom':{'capacity':45, 'classroom_id':'R-002', 'name':'CS023'}
                                    }),content_type="application/json")
        self.assertEquals(response.json, data)
    def test_cs_course_attendence_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_course_attendence_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_course_attendence') + '?lesson_id=')
        self.assertEquals(response.json, data)
    def test_cs_course_attendence_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_course_attendence_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_course_attendence') + '?lesson_id=L-001-01')
        self.assertEquals(response.json, data)
    def test_cs_student_attendence_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_student_attendence_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_student_attendence') + '?user_id=&course_id=C-001')
        self.assertEquals(response.json, data)
    def test_cs_student_attendence_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_student_attendence_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_student_attendence') + '?user_id=110-S-012&course_id=C-001')
        self.assertEquals(response.json, data)
    def test_edit_cs_course_attendence_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/edit_cs_course_attendence_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.edit_cs_course_attendence')+'?user_id=&lesson_id=L-001-014&isAttendence=1')
        self.assertEquals(response.json, data)
    def test_edit_cs_course_attendence_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/edit_cs_course_attendence_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.edit_cs_course_attendence')+'?user_id=110-S-100&lesson_id=L-001-014&isAttendence=0')
        self.assertEquals(response.json, data)
    def test_edit_cs_course_attendence_3(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/edit_cs_course_attendence_3.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.edit_cs_course_attendence')+'?user_id=110-S-103&lesson_id=L-001-014&isAttendence=1')
        self.assertEquals(response.json, data)
    def test_cs_classroom_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_classroom_info_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_classroom_info') + '?classroom_id=')
        self.assertEquals(response.json, data)
    def test_cs_classroom_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_classroom_info_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_classroom_info') + '?classroom_id=R-004')
        self.assertEquals(response.json, data)
    def test_cs_classroom_list(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_classroom_list.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_classroom_list'))
        self.assertEquals(response.json, data)
    def test_cs_classroom_info_by_name_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_classroom_info_by_name_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_classroom_info_by_name')+'?name=')
        self.assertEquals(response.json, data)
    def test_cs_classroom_info_by_name_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_classroom_info_by_name_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_classroom_info_by_name')+'?name=CS104')
        self.assertEquals(response.json, data)
    def test_insert_cs_classroom_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/insert_cs_classroom_info_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.insert_cs_classroom_info')+'?name=&capacity=35')
        self.assertEquals(response.json, data)
    def test_insert_cs_classroom_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/insert_cs_classroom_info_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.insert_cs_classroom_info')+'?name=CS205&capacity=30')
        self.assertEquals(response.json, data)
    def test_delete_cs_classroom_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/delete_cs_classroom_info_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.delete_cs_classroom_info')+'?classroom_id=')
        self.assertEquals(response.json, data)
    def test_delete_cs_classroom_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/delete_cs_classroom_info_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.delete_cs_classroom_info')+'?classroom_id=R-009')
        self.assertEquals(response.json, data)
    def test_edit_cs_classroom_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/edit_cs_classroom_info_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.edit_cs_classroom_info')+'?classroom_id=&name=CS205&capacity=7')
        self.assertEquals(response.json, data)
    def test_edit_cs_classroom_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/edit_cs_classroom_info_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.edit_cs_classroom_info')+'?classroom_id=R-008&name=ANTH215&capacity=34')
        self.assertEquals(response.json, data)
    def test_cs_reschedule_list(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_reschedule_list.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_reschedule_list'))
        self.assertEquals(response.json, data)
    #!
    def test_cs_reschedule_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_reschedule_info_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_reschedule_info')+'?weekday=&time=21:00')
        self.assertEquals(response.json, data)
    def test_cs_reschedule_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_reschedule_info_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_reschedule_info')+'?weekday=Mon&time=19:00')
        self.assertEquals(response.json, data)
    def test_cs_reschedule_info_3(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_reschedule_info_3.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_reschedule_info')+'?weekday=Tue&time=19:00')
        self.assertEquals(response.json, data)
    #!
    def test_edit_cs_reschedule_list_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_reschedule_list_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.edit_cs_reschedule_list')+'?weekday=&time=19:00&new_state=1')
        self.assertEquals(response.json, data)
    def test_edit_cs_reschedule_list_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_reschedule_list_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.edit_cs_reschedule_list')+'?weekday=Fri&time=19:00&new_state=1')
        self.assertEquals(response.json, data)
    def test_edit_cs_reschedule_list_3(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_reschedule_list_3.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.edit_cs_reschedule_list')+'?weekday=Fri&time=19:00&new_state=0')
        self.assertEquals(response.json, data)
    def test_cs_lesson_id_and_time_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_lesson_id_and_time_1.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_lesson_id_and_time')+'?course_id=')
        self.assertEquals(response.json, data)
    def test_cs_lesson_id_and_time_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('/Users/linxiangling/Documents/GitHub/CramSchoolApp/tests/data/cs_lesson_id_and_time_2.json', 'r') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.cs_lesson_id_and_time')+'?course_id=C-001')
        self.assertEquals(response.json, data)


        