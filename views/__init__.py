from .login_api import login_api
from .login_web import login_web
from .student_api import student_api
from .student_web import student_web
from .teacher_api import teacher_api
from .teacher_web import teacher_web
from .cs_api import cs_api
from .cramschool_web import cramschool_web
from .user_api import user_api



blueprint_prefix = [(login_api, ""), (login_web, ""), (user_api, ""), (student_api, ""), (student_web, "/student"), (teacher_api, ""), (teacher_web, "/teacher"), (cs_api, ""), (cramschool_web, "/cramschool")]


def register_blueprint(app):
    for blueprint, prefix in blueprint_prefix:
        app.register_blueprint(blueprint, url_prefix=prefix)
    return app
