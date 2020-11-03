from flask import Flask

from views import (
    student_api,
    teacher_api,
    boss_api,
    # login_api__class__
)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(student_api.student_api)
    app.register_blueprint(teacher_api.teacher_api)
    app.register_blueprint(boss_api.boss_api)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()