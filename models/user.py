from bson.objectid import ObjectId
from models import db

from flask_bcrypt import Bcrypt

def get_all_user():
    return db.STUDENT_COLLECTION.find() + db.TEACHER_COLLECTION.find() + db.BOSS_COLLECTION.find()

