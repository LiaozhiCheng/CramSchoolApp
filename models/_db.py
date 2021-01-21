from flask_mongoengine import MongoEngine

DB = None


def setup(app):
    global DB
    DB = MongoEngine(app)
    
from pymongo import MongoClient

DB = MongoClient('mongodb+srv://Liao:871029@cluster0-sk2jk.mongodb.net')['CramSchool']


USER_DATA_COLLECTION = DB['User']

USER_COLLECTION=DB['user']

COURSE_COLLECTION=DB['Course']

CLASSROOM_COLLECTION=DB['Classroom']

RESCHEDULE_COLLECTION=DB['Reschedule']

LESSON_COLLECTION=DB['Lesson']

COLLECTION_ID_COLLECTION=DB['CollectionID']
