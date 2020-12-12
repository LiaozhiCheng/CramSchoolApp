from flask import Flask

from flask_security import Security

import models
from views import register_blueprint
from lib import config



def create_app():
    app = Flask(__name__)
    app.jinja_env.auto_reload = True
    app.config.from_object(config.Config())

    # models setup
    models.setup(app)

    # security setup

    Security(app, models.user.USER_DATASTORE,login_form=models.user.ExtendedLoginForm)

    # register app
    register_blueprint(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
