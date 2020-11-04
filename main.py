

from flask import Flask

from views import (
    student_api,
    teacher_api,
    boss_api,
    # login_api__class__
)

def create_app():
    app = Flask(__name__)
    app.jinja_env.auto_reload = True
    app.config.from_object('app.config')
    
    #register route from differemt role
    app.register_blueprint(student_api.student_api,url_prefix = '/student')
    app.register_blueprint(teacher_api.teacher_api,url_prefix = '/teacher')
    app.register_blueprint(boss_api.boss_api,url_prefix = '/boss')
    
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()