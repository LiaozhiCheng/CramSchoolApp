from . import SettingBase
from flask import url_for
import json
 
#測試cs_api
#Todo
class CheckCramSchoolEditAPI(SettingBase):
    def test_insert_user_detail_info_1(self):  
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/insert_user_detail_info_1.json', 'r', encoding = 'utf-8') as file:
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
        with open('data/insert_user_detail_info_2.json', 'r', encoding = 'utf-8') as file:
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
        with open('data/insert_user_detail_info_3.json', 'r', encoding = 'utf-8') as file:
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
        with open('data/delete_user_detail_info_1.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.delete_user_detail_info') + '?user_id=')
        self.assertEquals(response.json, data)
    def test_delete_user_detail_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/user_detail_info_2.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.delete_user_detail_info') + '?user_id=110-S-103')
        self.assertEquals(response.json, data)
    #!
    def test_edit_user_detail_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/edit_user_detail_info_1.json', 'r', encoding = 'utf-8') as file:
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
        with open('data/edit_user_detail_info_2.json', 'r', encoding = 'utf-8') as file:
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
    
    def test_insert_cs_course_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/insert_cs_course_info_1.json', 'r', encoding = 'utf-8') as file:
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
        with open('data/insert_cs_course_info_2.json', 'r', encoding = 'utf-8') as file:
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
        with open('data/delete_cs_course_info_1.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.delete_cs_course_info') + '?course_id=')
        self.assertEquals(response.json, data)
    def test_delete_cs_course_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/delete_cs_course_info_2.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.delete_cs_course_info') + '?course_id=C-022')
        self.assertEquals(response.json, data)
    #!
    def test_edit_cs_course_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/edit_cs_course_info_1.json', 'r', encoding = 'utf-8') as file:
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
        with open('data/edit_cs_course_info_2.json', 'r', encoding = 'utf-8') as file:
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
    
    def test_edit_cs_course_attendence_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/edit_cs_course_attendence_1.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.edit_cs_course_attendence')+'?user_id=&lesson_id=L-001-014&isAttendence=1')
        self.assertEquals(response.json, data)
    def test_edit_cs_course_attendence_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/edit_cs_course_attendence_2.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.edit_cs_course_attendence')+'?user_id=110-S-100&lesson_id=L-001-014&isAttendence=0')
        self.assertEquals(response.json, data)
    def test_edit_cs_course_attendence_3(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/edit_cs_course_attendence_3.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.edit_cs_course_attendence')+'?user_id=110-S-103&lesson_id=L-001-014&isAttendence=1')
        self.assertEquals(response.json, data)
    def test_insert_cs_classroom_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/insert_cs_classroom_info_1.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.insert_cs_classroom_info')+'?name=&capacity=35')
        self.assertEquals(response.json, data)
    def test_insert_cs_classroom_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/insert_cs_classroom_info_2.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.insert_cs_classroom_info')+'?name=CS205&capacity=30')
        self.assertEquals(response.json, data)
    def test_delete_cs_classroom_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/delete_cs_classroom_info_1.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.delete_cs_classroom_info')+'?classroom_id=')
        self.assertEquals(response.json, data)
    def test_delete_cs_classroom_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/delete_cs_classroom_info_2.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.delete_cs_classroom_info')+'?classroom_id=R-009')
        self.assertEquals(response.json, data)
    def test_edit_cs_classroom_info_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/edit_cs_classroom_info_1.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.edit_cs_classroom_info')+'?classroom_id=&name=CS205&capacity=7')
        self.assertEquals(response.json, data)
    def test_edit_cs_classroom_info_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/edit_cs_classroom_info_2.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.edit_cs_classroom_info')+'?classroom_id=R-008&name=ANTH215&capacity=34')
        self.assertEquals(response.json, data)
    def test_edit_cs_reschedule_list_1(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/edit_cs_reschedule_list_1.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.edit_cs_reschedule_list')+'?weekday=&time=19:00&new_state=1')
        self.assertEquals(response.json, data)
    def test_edit_cs_reschedule_list_2(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/edit_cs_reschedule_list_2.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.edit_cs_reschedule_list')+'?weekday=Fri&time=19:00&new_state=1')
        self.assertEquals(response.json, data)
    def test_edit_cs_reschedule_list_3(self):
        self.user_id = "handsomeboy"
        self.password = "beautifulgirl"
        self.signin()
        with open('data/edit_cs_reschedule_list_3.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        response = self.client.get(url_for('cs_api.edit_cs_reschedule_list')+'?weekday=Fri&time=19:00&new_state=0')
        self.assertEquals(response.json, data)