from . import SettingBase
from flask import url_for
class CheckUserAndLogin(SettingBase):
    def test_signin_teacher(self):
        self.user_id = '110-T-001'
        self.password = '001'
        response = self.signin()
        print(response.data)
        self.assertEqual(response.status_code, 200)
        
    def test_signin_student(self):
        self.user_id = '110-S-026'
        self.password = '026'
        response = self.signin()
        print(response.data)
        self.assertEqual(response.status_code, 200) 
        
    def test_signin_boss(self):
        self.user_id = 'handsomeboy'
        self.password = 'beautifulgirl'
        response = self.signin()
        print(response.data)
        self.assertEqual(response.status_code, 200) 
    

    def test_signin_error(self):
        self.user_id = '110-S-026'
        self.password = '12'
        response = self.signin()
        print(response.data)
        self.assertEqual(response.status_code, 200) 
    
    def test_logout(self):
        response = self.client.get(url_for('login_web.logout'))
        self.assertEqual(response.status_code, 302) 
        
        
        
    def test_my_user(self):
        self.user_id = '110-T-001'
        self.password = '001'
        response = self.signin()
        response = self.client.get('/my_user')
        self.assertEqual(response.data, b'110-T-001')