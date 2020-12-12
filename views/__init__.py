from .login_api import login_api
from .login_web import login_web


blueprint_prefix = [(login_api, ""), (login_web, "")]


def register_blueprint(app):
    for blueprint, prefix in blueprint_prefix:
        app.register_blueprint(blueprint, url_prefix=prefix)
    return app
