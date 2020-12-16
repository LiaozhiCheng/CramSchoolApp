from flask import Blueprint, redirect, render_template, url_for

from flask_security import logout_user, login_required

login_web = Blueprint("login_web", __name__)


@login_web.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("index"))

@login_web.route("/", methods=["GET", "POST"])
@login_web.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")



@login_web.route("/testlogin", methods=["GET"])
@login_required
def test():
    return "only for login user"
