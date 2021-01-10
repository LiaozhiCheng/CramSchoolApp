from flask import render_template
from flask import Blueprint
from flask_security import login_required,roles_required

teacher_web = Blueprint('teacher_web', __name__)

#####################################################################
@teacher_web.route('/teacher', methods=["GET", "POST"])
@login_required
@roles_required('teacher')
def teacher():
	return render_template('teacher.html', methods=["GET", "POST"])

#####################################################################
@teacher_web.route('/teacher_class_student', methods=["GET", "POST"])
@login_required
@roles_required('teacher')
def class_student():
	return render_template('teacher_class_student.html')

#####################################################################
@teacher_web.route('/teacher_communication_book', methods=["GET", "POST"])
@login_required
@roles_required('teacher')
def communication_book():
	return render_template('teacher_communication_book.html')

#####################################################################
@teacher_web.route('/teacher_courseinfo', methods=["GET", "POST"])
@login_required
@roles_required('teacher')
def courseinfo():
	return render_template('teacher_courseinfo.html')

#####################################################################
@teacher_web.route('/teacher_homework', methods=["GET", "POST"])
@login_required
@roles_required('teacher')
def teacher_homework():
	return render_template('teacher_homework.html')

#####################################################################
@teacher_web.route('/teacher_grade', methods=["GET", "POST"])
@login_required
@roles_required('teacher')
def teacher_grade():
	return render_template('teacher_grade.html')

#####################################################################
@teacher_web.route('/teacher_personal_plan', methods=["GET", "POST"])
@login_required
@roles_required('teacher')
def teacher_personal_plan():
	return render_template('teacher_personal_plan.html')

#####################################################################
@teacher_web.route('/teacher_student_attendence', methods=["GET", "POST"])
@login_required
@roles_required('teacher')
def teacher_attendence():
	return render_template('teacher_student_attendence.html')

#####################################################################
@teacher_web.route('/teacher_student_attendenceA', methods=["GET", "POST"])
@login_required
@roles_required('teacher')
def teacher_attendenceA():
    return render_template('teacher_student_attendenceA.html')

#####################################################################
@teacher_web.route('/teacher_student_attendenceB', methods=["GET", "POST"])
@login_required
@roles_required('teacher')
def teacher_attendenceB():
	return render_template('teacher_student_attendenceB.html')
#####################################################################