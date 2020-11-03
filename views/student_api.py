
from flask import Blueprint

student_api = Blueprint('student_api', __name__)

@student_api.route('/student_test')
def my_student():
        return "Hello Student"