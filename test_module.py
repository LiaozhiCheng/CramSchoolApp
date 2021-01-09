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



"""
#測試登入
class CheckUserAndLogin(SettingBase):
    def test_signup(self):
        response = self.signup
        self.assertEqual(response.status_code, 200)
        
        
        
#測試teacher api
#Todo
class CheckTeacherAPI(SettingBase):
    def test_course_communication_book(self):
        response = self.client.get(url_for('teacher_api.course_communication_book'))
        self.assertEquals(response.json, list())
        return response





if __name__ == '__main__':
    unittest.main()
        
    