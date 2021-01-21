from models import _db, user



def add_users():
    for the_user in _db.USER_DATA_COLLECTION.find():
        print(the_user)
        try:
            user.create_user(the_user['name'], the_user['password'], the_user['phone'], the_user['user_id'], the_user['email'], the_user['role'], the_user['major'], the_user['course_list'], [])
        except:
            the_user['major'] = list()
            user.create_user(the_user['name'], the_user['password'], the_user['phone'], the_user['user_id'], the_user['email'], the_user['role'], the_user['major'], the_user['course_list'], [])
            