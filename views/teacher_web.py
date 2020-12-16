from flask import render_template
from flask import Blueprint

teacher_web = Blueprint('teacher_web', __name__)

#####################################################################
@teacher_web.route('/teacher')
def teacher():
	return render_template('teacher.html')

#####################################################################
@teacher_web.route('/teacher_class_student')
def class_student():
	return render_template('teacher_class_student.html')

#####################################################################
@teacher_web.route('/teacher_communication_book')
def communication_book():
	return render_template('teacher_communication_book.html')

#####################################################################
@teacher_web.route('/teacher_courseinfo')
def courseinfo():
	return render_template('teacher_courseinfo.html')

#####################################################################
@teacher_web.route('/teacher_homework')
def teacher_homework():
	return render_template('teacher_homework.html')

#####################################################################
@teacher_web.route('/teacher_grade')
def teacher_grade():
	return render_template('teacher_grade.html')

#####################################################################
@teacher_web.route('/teacher_personal_plan')
def teacher_personal_plan():
	return render_template('teacher_personal_plan.html')

#####################################################################
@teacher_web.route('/teacher_student_attendence')
def teacher_attendence():
	return render_template('teacher_student_attendence.html')

#####################################################################
@teacher_web.route('/teacher_student_attendenceA')
def teacher_attendenceA():
    return render_template('teacher_student_attendenceA.html')

#####################################################################
@teacher_web.route('/teacher_student_attendenceB')
def teacher_attendenceB():
	return render_template('teacher_student_attendenceB.html')
#####################################################################