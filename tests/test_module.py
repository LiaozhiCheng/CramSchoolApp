import unittest
from flask_testing import TestCase

class SettingBase(TestCase):
    def create_app(self):
        return create_app()
    def signup(self):
        response = self.client.post(url_for('login_user'),
                                     follow_redirects=True,
                                    json={
                                        "username": '110-T-001',
                                        "password": '001',
                                        "role": 'teacher'
                                    })
        return response


class CheckUserAndLogin(SettingBase):
    def test_signup(self):
        response = self.signup
        self.assertEqual(response.status_code, 200)
        
        


if __name__ == '__main__':
    unittest.main()
        
    