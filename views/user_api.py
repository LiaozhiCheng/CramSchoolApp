from flask import Blueprint, jsonify
from flask import request
from flask_security import current_user,login_required

# ---------- import models -----------------------------------------
from models import course
# ------------------------------------------------------------------

user_api = Blueprint('user_api', __name__)

# ------------------------------------------------------------------

# user schedule
@user_api.route('/schedule', methods=['GET'])
@login_required
def user_schedule():
    course_list = []
    for course_id in current_user.course_list:
        each_course = course.get_by_courseid(course_id)
        course_dict = {
                        "course" : each_course['name'],
                        "course_id" : each_course['course_id'],
                        "time" : each_course['course_time']
        }
        course_list.append(course_dict)
        
    return jsonify(course_list)

#####################################################################
# user personal info
@user_api.route('/personal_info', methods=['GET'])
@login_required
def user_personal_info():
    if current_user.role == "teacher":
        output = {
                    "user_id" : current_user.user_id,
                    "name" : current_user.name,
                    "phone" : current_user.phone,
                    "email" : current_user.email,
                    "major" : current_user.major,
                    "role" : current_user.role
        }
    else:
        output = {
                    "user_id" : current_user.user_id,
                    "name" : current_user.name,
                    "phone" : current_user.phone,
                    "email" : current_user.email,
                    "role" : current_user.role
        }
        
    return jsonify(output)


#####################################################################
# course info
@user_api.route('/course_info', methods=['GET'])
@login_required
def course_info():
    course_id = request.values.get('course_id')
    item = course.get_by_courseid(course_id)
    output = {
                "course" : item['name'],
                "teacher" : item['teacher'],
                "summary" : item['summary'],
                "classroom" : item['classroom']['name']
            }
    return jsonify(output)