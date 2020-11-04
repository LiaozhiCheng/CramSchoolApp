from flask import Blueprint, jsonify
from models import testm

test_api = Blueprint('test_api', __name__)

@test_api.route('/get_all_student')
def my_student():
    tmp = []
    s = testm.get_all_student()
    for i in s:
        i.pop('_id')
        tmp.append(i)
    return jsonify(tmp)