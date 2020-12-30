from flask import Blueprint,jsonify
from flask import request
from datetime import datetime

# ---------- import models -----------------------------------------
from models import user
from models import course
from models import lesson
# ------------------------------------------------------------------

teacher_api = Blueprint('teacher_api', __name__)

# ------------------------------------------------------------------

#####################################################################
# teacher communication book
@teacher_api.route('/teacher_course_communication_book', methods=['GET','POST'])
def course_communication_book():
    course_id = request.values.get('course_id')
    items = lesson.get_by_courseid(course_id)
    com_book_list = []
    for i in items:
        each_com_book = {
                            "lesson_id" : i['lesson_id'],
                            "lesson_time" : datetime.strftime(i['lesson_time'],"%Y-%m-%d"),
                            "progress" : i['progress'],
                            "deadline" : datetime.strftime(i['homework']['deadline'],"%Y-%m-%d"),
                            "context" : i['homework']['context']
        }
        com_book_list.append(each_com_book)
    return jsonify(com_book_list)

#####################################################################
# teacher edit communication book
@teacher_api.route('/teacher_edit_course_communication_book', methods=['POST'])
def edit_course_communication_book():
    data = request.get_json()
    try:
        homework = {
                        "deadline" : datetime.strptime(data['deadline'],"%Y-%m-%d"),
                        "context": data['context']
        }
    except ValueError:
        homework = {
                        "deadline" : None,
                        "context": data['context']
        }
    new_info = {
                    "progress" : data['progress'],
                    "homework" : homework
    }
    lesson.update_lesson_communication_book(data['lesson_id'],new_info)
    return jsonify(new_info)

#####################################################################
# teacher communication book
@teacher_api.route('/teacher_course_personal_plan', methods=['GET','POST'])
def course_personal_plan():
    course_id = request.values.get('course_id')
    student_id = request.values.get('student_id')
    target_student = user.get_by_userid(student_id)
    plan_list = []
    for p in target_student['personal_plan']:
        if p != None:
            if p['lesson_id'][2:4]==course_id[2:4]:
                # 要取得該 plan 所屬 lesson 的lesson_time
                le = lesson.get_by_lessonid(p['lesson_id'])
                if p['deadline'] != None:
                    deadline = datetime.strftime(p['deadline'],"%Y-%m-%d") 
                else :
                    deadline = None
                each_plan = {
                    "lesson_id" : p['lesson_id'],
                    "lesson_time" : datetime.strftime(le['lesson_time'],"%Y-%m-%d"),
                    "deadline" : deadline,
                    "context": p['context']
                }
                print(each_plan)
                plan_list.append(each_plan)    
    return jsonify(plan_list)
#####################################################################
# teacher get no plan lesson time
@teacher_api.route('/teacher_no_plan_lesson_time', methods=['GET','POST'])
def teacher_no_plan_lesson_time():
    course_id = request.values.get('course_id')
    student_id = request.values.get('student_id')
    items = lesson.get_by_courseid(course_id)
    target_student = user.get_by_userid(student_id)
    lesson_list = []
    for i in items:
        exist = False
        for p in target_student['personal_plan']:
            le = lesson.get_by_lessonid(p['lesson_id'])
            if datetime.strftime(le['lesson_time'],"%Y-%m-%d") == datetime.strftime(i['lesson_time'],"%Y-%m-%d") :
              exist = True
              break
        if not exist:
            each_data = {
            "lesson_id" : i['lesson_id'],
            "lesson_time" : datetime.strftime(i['lesson_time'],"%Y-%m-%d")
            }
            lesson_list.append(each_data)
    return jsonify(lesson_list)


#####################################################################
# teacher edit course personal plan
@teacher_api.route('/teacher_edit_course_personal_plan', methods=['GET','POST'])
def edit_course_personal_plan():
    data = request.get_json()
    try:
        new_info = {
                        "lesson_id" : data['lesson_id'],
                        "deadline" : datetime.strptime(data['deadline'],"%Y-%m-%d"),
                        "context" : data['context']
        }
    except ValueError:
        new_info = {
                        "lesson_id" : data['lesson_id'],
                        "deadline" : None,
                        "context" : data['context']
        }
    s = user.get_by_userid(data['student_id'])
    plan = s['personal_plan']
    exist = False
    for p in plan:
        if p['lesson_id'] == data['lesson_id']:
            user.delete_personal_plan(data['student_id'],p)
            user.update_personal_plan(data['student_id'],new_info)
            exist = True
            break
    if not exist:
        user.update_personal_plan(data['student_id'],new_info)
    return jsonify(new_info)
   
#####################################################################
# teacher course student list
@teacher_api.route('/teacher_course_student_list', methods=['GET','POST'])
def course_student_list():
    course_id = request.values.get('course_id')
    target_course = course.get_by_courseid(course_id)
    student_list = []
    for student_id in target_course['student_list']:
        s = user.get_by_userid(student_id)
        each_student = {
                            "student_name" : s['name'],
                            "student_id" : s['user_id'],
                            "email" : s['email'],
                            "phone" : s['phone']
        }
        student_list.append(each_student)
    return jsonify(student_list)
#####################################################################
# teacher course student info
@teacher_api.route('/teacher_student_personal_info', methods=['GET'])
def user_personal_info():
    student_id = request.values.get('student_id')
    target_student = user.get_by_userid(student_id)
    output = {
                "user_id" : target_student['user_id'],
                "name" : target_student['name'],
                "phone" : target_student['phone'],
                "email" : target_student['email'],
                "role" : target_student['role']
    }
        
    return jsonify(output)

#####################################################################
# teacher course attendence
@teacher_api.route('/teacher_course_attendence', methods=['GET','POST'])
def course_attendence():
    course_id = request.values.get('course_id')
    target_course = course.get_by_courseid(course_id)
    items = lesson.get_by_courseid(course_id)
    whole_list = []
    for i in items:
        attendence_list = []
        for student_id in target_course['student_list']:
            s = user.get_by_userid(student_id)
            each_student = {
                                "student_name" : s['name'],
                                "student_id" : s['user_id'],
                                "email" : s['email'],
                                "phone" : s['phone'],
                                "state" : s['user_id'] in i['attendence']
            }
            attendence_list.append(each_student)
        each_day = {
                        "lesson_time" : datetime.strftime(i['lesson_time'],"%Y-%m-%d"),
                        "attendence_list" : attendence_list
        }
        whole_list.append(each_day)
        whole_list = sorted(whole_list,key=lambda k: k['lesson_time'])
    return jsonify(whole_list)
        
#####################################################################
# teacher course grade
@teacher_api.route('/teacher_course_grade', methods=['GET','POST'])
def course_grade():
    course_id = request.values.get('course_id')
    target_course = course.get_by_courseid(course_id)
    all_lessons = lesson.get_by_courseid(course_id)
    whole_list = []
    for l in all_lessons:
        if len(l['quiz']['grade_list'])==0:
            student_list = []
            for student_id in target_course['student_list']:
                s = user.get_by_userid(student_id)
                each_student = {
                                    "student_name" : s['name'],
                                    "student_grade" : None
                }
                
                student_list.append(jsonify(each_student))
            each_quiz = {
                            "lesson_id" : l['lesson_id'],
                            "lesson_time" : datetime.strftime(l['lesson_time'],"%Y-%m-%d"),
                            "quiz_name" : l['quiz']['quiz_name'],
                            "grade_list": student_list
            }
        else:
            each_quiz = {
                            "lesson_id" : l['lesson_id'],
                            "lesson_time" : datetime.strftime(l['lesson_time'],"%Y-%m-%d"),
                            "quiz_name" : l['quiz']['quiz_name'],
                            "grade_list": l['quiz']['grade_list']
            }
            whole_list.append(each_quiz)
            whole_list = sorted(whole_list,key=lambda k: k['lesson_time'])
    return jsonify(whole_list)
#####################################################################
# teacher edit course grade
@teacher_api.route('/teacher_edit_course_grade', methods=['POST'])
def edit_course_grade():
    data = request.get_json()
    new_info = {
                    "quiz_name": data['quiz_name'],
                    "grade_list" : data['grade_list']    
    }
    lesson.update_lesson_grade(data['lesson_id'],new_info)
    return jsonify(new_info)
#####################################################################
# teacher delete course grade    
@teacher_api.route('/teacher_delete_course_grade', methods=['GET'])
def delete_course_grade():
    lesson_id = request.values.get('lesson_id')
    item = lesson.get_by_lessonid(lesson_id)
    new_list = []
    for s in item['quiz']['grade_list']:
        new_each = {
                        "student_name": s['student_name'],
                        "student_grade": None
                        
        }
        new_list.append(new_each)
    new_quiz = {
        "quiz_name" : item['quiz']['quiz_name'],
        "grade_list" : new_list
    }
    lesson.update_lesson_grade(lesson_id,new_quiz)
    return jsonify(new_quiz)