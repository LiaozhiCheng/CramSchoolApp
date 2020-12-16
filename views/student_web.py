from flask import render_template
from flask import Blueprint

student_web = Blueprint('student_web', __name__)

#####################################################################
@student_web.route('/student', methods=["GET", "POST"])
def student():
	return render_template('student.html')

#####################################################################
@student_web.route('/student_attendence', methods=["GET", "POST"])
def attendence():
	return render_template('student_attendence.html')

#####################################################################
@student_web.route('/student_course_process', methods=["GET", "POST"])
def course_process():
	return render_template('student_course_process.html')

#####################################################################
@student_web.route('/student_grade', methods=["GET", "POST"])
def grade():
	return render_template('student_grade.html')

#####################################################################
@student_web.route('/student_homework', methods=["GET", "POST"])
def student_homework():
	return render_template('student_homework.html')

#####################################################################
@student_web.route('/student_learning_plan', methods=["GET", "POST"])
def learning_plan():
	return render_template('student_learning_plan.html')

#####################################################################
@student_web.route('/student_lesson_makeup', methods=["GET", "POST"])
def lesson_makeup():
	return render_template('student_lesson_make-up.html')