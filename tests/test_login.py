from . import SettingBase

class CheckUserAndLogin(SettingBase):
    def test_signup(self):
        response = self.signup()
        self.assertEqual(response.status_code, 200)