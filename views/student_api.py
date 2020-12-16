from flask import Blueprint,jsonify
from flask import request
from flask_security import current_user

# ---------- import models ----------
from models import course
from models import lesson
from models import reschedule
from models import classroom
from datetime import datetime
# -----------------------------------

student_api = Blueprint('student_api', __name__)


#####################################################################
# student/teacher course progress
@student_api.route('/course_progress', methods=['GET','POST'])
def stu_course_progress():
    course_id = request.values.get('course_id')
    items = lesson.get_by_courseid(course_id)
    progress_list = []
    for i in items:
        each_progress = {
                            "lesson_time" : i['lesson_time'].date(),
                            "progress" : i['progress']
        }
        progress_list.append(each_progress)
        progress_list = sorted(progress_list,key=lambda k: k['lesson_time'])
    return jsonify(progress_list)

#####################################################################
# student course homework
@student_api.route('/course_homework', methods=['GET','POST'])
def stu_course_homework():
    course_id = request.values.get('course_id')
    items = lesson.get_by_courseid(course_id)
    homework_list = []
    for i in items:
        each_homework = {
                            "lesson_time" : i['lesson_time'].date(),
                            "homework" : i['homework']['context'],
                            "deadline" : i['homework']['deadline'],
                            "progress" : i['progress']
        }
        homework_list.append(each_homework)
        homework_list = sorted(homework_list,key=lambda k: k['lesson_time'])
    return jsonify(homework_list)


#####################################################################
# student course grade
@student_api.route('/course_grade', methods=['GET','POST'])
def stu_course_grade():
    course_id = request.values.get('course_id')
    items = lesson.get_by_courseid(course_id)
    quiz_list = []
    for i in items:
        if current_user.user_id in i['attendence']:
            grade_dict = next((g for g in i['quiz']['grade_list'] if g['student_name'] == current_user.user_id), None)
            each_quiz = {
                            "quiz_date" : i['lesson_time'].date(),
                            "quiz_name" : i['quiz']['quiz_name'],
                            "grade" : grade_dict['student_grade']
            }        
            quiz_list.append(each_quiz)
        quiz_list = sorted(quiz_list,key=lambda k: k['quiz_date'])
    return jsonify(quiz_list)

#####################################################################
# student course attendence
@student_api.route('/course_attendence', methods=['GET','POST'])
def stu_course_attendence():
    course_id = request.values.get('course_id')
    items = lesson.get_by_courseid(course_id)
    attendence_list = []
    for i in items:
        each_attendence = {
                            "lesson_time" : i['lesson_time'],
                            "progress" : i['progress'],
                            "state" : current_user.user_id in i['attendence']
        }    
        attendence_list.append(each_attendence)
        attendence_list = sorted(attendence_list,key=lambda k: k['lesson_time'])
    return jsonify(attendence_list)

#####################################################################
# student course_personal_plan
@student_api.route('/course_personal_plan', methods=['GET','POST'])
def stu_course_personal_plan():
    course_id = request.values.get('course_id')
    personal_plan = current_user.personal_plan
    plan_list = []
    for p in personal_plan:
        if p['lesson_id'][2:4] == course_id[2:4]:
            l = lesson.get_by_lessonid(p['lesson_id'])
            each_plan = {
                            "lesson_time" : l['lesson_time'].date(),
                            "deadline" : p['deadline'].date(),
                            "progress" : l['progress'],
                            "context" : p['context'] 
            }    
        plan_list.append(each_plan)
        plan_list = sorted(plan_list,key=lambda k: k['lesson_time'])
    return jsonify(plan_list)

#####################################################################
# student miss lesson
@student_api.route('/miss_lesson', methods=['GET','POST'])
def stu_miss_lesson():
    whole_list = []
    for course_id in current_user.course_list :
        c = course.get_by_courseid(course_id)
        ls = lesson.get_by_courseid(course_id)
        miss_lessons = []
        for l in ls:
            if current_user.user_id not in l['attendence']:
                each_lesson = {
                                "lesson_id" : l['lesson_id'],
                                "progress" : l['progress'],
                }
                miss_lessons.append(each_lesson)
        each_course = { 
                        "course_name" : c['name'],
                        "miss_lessons" : miss_lessons   
        }
        if len(each_course['miss_lessons']) > 0 :
            whole_list.append(each_course)
    return jsonify(whole_list)
#####################################################################
# student reschedule list
@student_api.route('/reschedule_list', methods=['GET','POST'])
def stu_reschedule_list():
    items = reschedule.get_all();
    reschedule_list = []
    for i in items:
        if i['state'] == True:
            re = next((r for r in i['reservation_list'] if r['user_id'] == current_user.user_id), None)
            if re != None:
                ls = lesson.get_by_lessonid(re['lesson_id'])
                each_block = {
                                "datetime" : datetime.strftime(re['datetime'],"%Y-%m-%d+%w-%H"),
                                "course_name" : re['course_name'],
                                "lesson_id" : re['lesson_id'],
                                "progress" : ls['progress'],
                                "state" : "reserved"
                }
                reschedule_list.append(each_block)
            else:
                room_id = i['classroom_id']
                r = classroom.get_by_classroomid(room_id)
                if len(i['reservation_list']) < int(r['capacity']):
                    sta = True
                else:
                    sta = False
                each_block = {
                                "datetime" : datetime.strftime(i['datetime'],"%Y-%m-%d+%w-%H"),
                                "course_name" : "",
                                "lesson_id" : "",
                                "progress" : "",
                                "state" : "available" if sta else "full"
                }
                reschedule_list.append(each_block)
    return jsonify(reschedule_list)

#####################################################################
# student add reservation
@student_api.route('/add_reservation', methods=['POST'])
def add_reservation():
    data = request.get_json()
    new_reservation = {
                            "user_id" : current_user.user_id,
                            "datetime" : datetime.strptime(data['datetime'],"%Y-%m-%d+%w-%H"),
                            "course_name" : data['course_name'],
                            "lesson_id" : data['lesson_id']
    }
    reschedule.add_reservation(new_reservation)
    return jsonify(new_reservation)
    
#####################################################################
# student cancel reservation
@student_api.route('/cancel_reservation', methods=['GET','POST'])
def cancel_reservation():
    data = request.get_json()
    new_info = {
                    "user_id" : current_user.user_id,
                    "datetime" : datetime.strptime(data['datetime'],"%Y-%m-%d+%w-%H"),
                    "course_name" : data['course_name'],
                    "lesson_id" : data['lesson_id']
    }
    reschedule.delete_reservation(new_info)
    return jsonify(new_info)