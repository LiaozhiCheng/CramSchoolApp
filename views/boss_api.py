
from flask import Blueprint

boss_api = Blueprint('boss_api', __name__)

@boss_api.route('/boss_test')
def my_boss():
        return "Hello Boss"