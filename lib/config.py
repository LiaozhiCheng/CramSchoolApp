class Config(object):
    UPLOAD_FOLDER = "static/images"
    # Flask Security
    DEBUG = True
    SECRET_KEY = "super-secret"
    SECURITY_PASSWORD_SALT = "bcrypt"
    SECURITY_LOGIN_USER_TEMPLATE = "login.html"
    SECURITY_USER_IDENTITY_ATTRIBUTES = ('username','email')
    # MongoDB Config
    MONGODB_HOST = (
        "mongodb+srv://Liao:871029@cluster0-sk2jk.mongodb.net/CramSchool"
    )
    MONGODB_DB = True

    JSON_AS_ASCII = False
    TEMPLATES_AUTO_RELOAD = True
    UPLOAD_FOLDER = UPLOAD_FOLDER
