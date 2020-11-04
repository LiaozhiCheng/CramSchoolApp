from models import db


def get_all_student():
    temp = db.STUDENT_COLLECTION.find()
    
    return temp

