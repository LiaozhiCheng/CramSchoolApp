import unittest

from flask_testing import TestCase
from flask import url_for
from main import create_app

#這邊是測試的基礎設置，先不要動
class SettingBase(TestCase):
    def create_app(self):

        return create_app()
        
    def signup(self):

        response = self.client.post(url_for('login_api.validate'),
                                     follow_redirects=True,
                                    json={
                                        "user_id": '110-T-001',
                                        "password": '001',

                                    })

        return response
  
"""    
指令說明
cmd 輸入pip install Flask-Testing
cmd 執行python test_module.py即可測試
測試的class要繼承SettingBase
測試的func開頭要是test_
response相關指令可參考https://pythonhosted.org/Flask-Testing/
url_for是指哪個blueprint.哪個function(不是網址)


"""
#測試登入
class CheckUserAndLogin(SettingBase):
    def test_signup(self):

        response = self.signup()                           
        self.assert200(response)
        
        
        
#測試teacher_api
#Todo
class CheckTeacherAPI(SettingBase):
    def test_course_communication_book(self):
        response = self.client.get(url_for('teacher_api.course_communication_book'))
        self.assertEquals(response.json, list())


#測試student_api
#Todo
class CheckStudentAPI(SettingBase):
    pass



if __name__ == '__main__':
    unittest.main()
        
    