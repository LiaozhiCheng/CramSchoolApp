
from flask import Blueprint

teacher_api = Blueprint('teacher_api', __name__)

@teacher_api.route('/teacher_test')
def my_teacher():
        return "Hello Teacher"