from flask_security import UserMixin, RoleMixin
from flask_security import (
    MongoEngineUserDatastore,
    hash_password,
    verify_password,
)
from . import _db
from flask_security.forms import LoginForm
from wtforms import StringField
from wtforms.validators import InputRequired

USER_DATASTORE = None

"""
    setup
"""
class ExtendedLoginForm(LoginForm):
        email = StringField('Username', [InputRequired()])
        
def setup():
    # 不同種權限身份
    class Role(_db.DB.Document, RoleMixin):
        name = _db.DB.StringField(max_length=80, unique=True)
        description = _db.DB.StringField(max_length=255)

    # 使用者資訊
    class User(_db.DB.Document, UserMixin):
        username = _db.DB.StringField(max_length=255)
        email = _db.DB.StringField(max_length=255)
        password = _db.DB.StringField(max_length=255)
        phone = _db.DB.StringField(max_length=255)
        major = _db.DB.ListField()
        course_list = _db.DB.ListField()
        personal_plan = _db.DB.ListField()
        active = _db.DB.BooleanField(default=True)
        confirmed_at = _db.DB.DateTimeField()
        roles = _db.DB.ListField(_db.DB.ReferenceField(Role), default=[])
        # meta = {'strict': False}

    # Setup Flask-Security
    global USER_DATASTORE
    USER_DATASTORE = MongoEngineUserDatastore(_db.DB, User, Role)




"""
    others
"""


def create_user():
    student_role = USER_DATASTORE.find_or_create_role("student")
    if USER_DATASTORE.get_user("Liao") is None:
        USER_DATASTORE.create_user(
            username="Liao",
            phone = "0919925648",
            email='Liao@gmail.com',
            major = ['國文'],
            password=hash_password("871029"),
            roles=[student_role],
        )


def validate_user(username: str, password: str):
    cur_user = USER_DATASTORE.find_user(username=username)
    if cur_user is None:
        return
    if verify_password(password, cur_user.password):
        return cur_user
    return None
