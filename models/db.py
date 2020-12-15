from pymongo import MongoClient

DB = MongoClient('mongodb+srv://Liao:871029@cluster0-sk2jk.mongodb.net')['testCram2']


USER_COLLECTION=DB['User']

COURSE_COLLECTION=DB['Course']

CLASSROOM_COLLECTION=DB['Classroom']

RESCHEDULE_COLLECTION=DB['Reschedule']

LESSON_COLLECTION=DB['Lesson']
