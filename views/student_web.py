from flask import render_template
from flask import Blueprint
from flask_security import login_required,roles_required

student_web = Blueprint('student_web', __name__)

#####################################################################
@student_web.route('/student', methods=["GET", "POST"])
@login_required
@roles_required('student')
def student():
	return render_template('student.html')

#####################################################################
@student_web.route('/student_attendence', methods=["GET", "POST"])
@login_required
@roles_required('student')
def attendence():
	return render_template('student_attendence.html')

#####################################################################
@student_web.route('/student_course_process', methods=["GET", "POST"])
@login_required
@roles_required('student')
def course_process():
	return render_template('student_course_process.html')

#####################################################################
@student_web.route('/student_grade', methods=["GET", "POST"])
@login_required
@roles_required('student')
def grade():
	return render_template('student_grade.html')

#####################################################################
@student_web.route('/student_homework', methods=["GET", "POST"])
@login_required
@roles_required('student')
def student_homework():
	return render_template('student_homework.html')

#####################################################################
@student_web.route('/student_learning_plan', methods=["GET", "POST"])
@login_required
@roles_required('student')
def learning_plan():
	return render_template('student_learning_plan.html')

#####################################################################
@student_web.route('/student_lesson_makeup', methods=["GET", "POST"])
@login_required
@roles_required('student')
def lesson_makeup():
	return render_template('student_lesson_make-up.html')