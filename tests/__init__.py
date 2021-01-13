from flask_testing import TestCase
from flask import url_for
from main import create_app
import json

#這邊是測試的基礎設置，先不要動
class SettingBase(TestCase):
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    def create_app(self):

        return create_app()
        
    def signin(self):
        #response = self.client.get(url_for('login_api.validate'),user_id = '110-T-001',password = '001')
        response = self.client.post(url_for('login_api.validate'),
                                     follow_redirects=True,
                                    data=json.dumps({
                                        'user_id': self.user_id,
                                        'password': self.password

                                    }),content_type="application/json")

        return response
        
    def logout(self):
        response = self.client.post(url_for('login_web.logout'))
        return response