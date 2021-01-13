from flask_testing import TestCase
from flask import url_for
from main import create_app


#這邊是測試的基礎設置，先不要動
class SettingBase(TestCase):
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    def create_app(self):

        return create_app()
        
    def signin(self):

        response = self.client.post(url_for('login_api.validate'),
                                     follow_redirects=True,
                                    json={
                                        "user_id": self.user_id,
                                        "password": self.password,

                                    })

        return response