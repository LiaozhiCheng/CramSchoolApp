from flask import render_template
from flask import Blueprint

student_web = Blueprint('student_web', __name__)

#####################################################################
@student_web.route('/student')
def student():
	return render_template('student.html')

#####################################################################
@student_web.route('/student_attendence')
def attendence():
	return render_template('student_attendence.html')

#####################################################################
@student_web.route('/student_course_process')
def course_process():
	return render_template('student_course_process.html')

#####################################################################
@student_web.route('/student_grade')
def grade():
	return render_template('student_grade.html')

#####################################################################
@student_web.route('/student_homework')
def student_homework():
	return render_template('student_homework.html')

#####################################################################
@student_web.route('/student_learning_plan')
def learning_plan():
	return render_template('student_learning_plan.html')

#####################################################################
@student_web.route('/student_lesson_make-up')
def lesson_makeup():
	return render_template('student_lesson_make-up.html')