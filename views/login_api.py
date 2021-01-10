from flask import request, Blueprint, redirect
from flask_security import login_user, current_user
from models import user
from models import build_data

login_api = Blueprint("login_api", __name__)


# 設定未授權時轉跳畫面
# security._state.unauthorized_handler(unauthorized_callback)


@login_api.route("/login_user", methods=["POST"])
def validate():
    email = request.values.get("user_id")
    password = request.values.get("password")
    cur_user = user.validate_user(email, password)
    remember = True if request.values.get("rememberMe", "n") == "y" else False

    if cur_user is None:
        return "帳密錯誤"

    login_user(cur_user, remember=remember)
    if current_user.role == 'teacher':
        return redirect('teacher')
    elif current_user.role == 'student':
        return redirect('student')
    return "success"



@login_api.route("/register")
def register():
    build_data.add_users()
    return "regist success"
    
@login_api.route('/add_manager')
def add_manager():
    user.create_manager()
    return 'managerIsAdd'
@login_api.route("/my_user")
def my_user():
    return current_user.password
