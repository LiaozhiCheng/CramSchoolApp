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