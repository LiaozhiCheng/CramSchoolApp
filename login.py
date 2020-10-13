
from flask import Flask,render_template, request, jsonify, redirect, url_for, make_response, flash, session
from flask_bcrypt import Bcrypt
from flask_security import Security, MongoEngineUserDatastore ,login_user, logout_user, UserMixin, RoleMixin, login_required, current_user, roles_accepted
from flask_mongoengine import MongoEngine
from pymongo import MongoClient

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config.from_object('app.config')

client = MongoClient('mongodb+srv://Liao:871029@cluster0-sk2jk.mongodb.net')
db = client['CramSchool']

db = MongoEngine(app)
bcrypt = Bcrypt(app)

#密碼加密
def hashPassword(password):
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    return pw_hash

# 不同種權限身份
class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

# 使用者資訊
class User(db.Document, UserMixin):
    email = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])

user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)

#沒有權限導引畫面
def unauthorized_callback():
    flash("你沒有權限") 
    return redirect('/login')

# 設定未授權時轉跳畫面
security._state.unauthorized_handler(unauthorized_callback)

@app.before_first_request
def create_user():
    student_role = user_datastore.find_or_create_role('student')
    print(student_role)
    if user_datastore.get_user('Liao') == None:     
        print('345')
        user_datastore.create_user(
            email='Liao', password = hashPassword('871029'), roles=[student_role]
        )
#    admin_role = user_datastore.find_or_create_role('admin')
#    if user_datastore.get_user('root') == None:
#        user_datastore.create_user(
#            email='root', password = hashPassword('root'), roles=[admin_role]
#        )
#    guest_role = user_datastore.find_or_create_role('guest')
#    if user_datastore.get_user('guest') == None:
#        user_datastore.create_user(
#            email='guest', password = hashPassword('guest'), roles=[guest_role]
#        )  
        
@app.route('/')
@app.route('/login', methods=['GET', 'POST']) 
def login():
    return render_template('login.html')

@app.route('/login_user', methods=['GET', 'POST'])
def login_Use():
    print('here')
    try:
        nowUser = request.values.to_dict()
        print(nowUser)
        db = client['CramSchool']
        user_col=db['user']
        print(user_col.find_one({'email':nowUser['email']}))
        user_in_db =user_col.find_one({'email':nowUser['email']})
        if user_in_db is None or bcrypt.check_password_hash(user_in_db['password'], nowUser['password']) is False:
            print(user_in_db)
            print(bcrypt.check_password_hash(user_in_db['password'], nowUser['password']))
            return redirect('/login')
        
    #    設置session
        session['username'] = nowUser['email']
        session.permanent = True
        
        nowUser=user_datastore.get_user(nowUser['email'])
        login_user(nowUser)
        return redirect('/index')
    except:
        return redirect('/login')
    
   
@app.route('/index')
@login_required
def index():
    return render_template('index.html')



        
if __name__ == '__main__':
    app.run(host="140.121.199.231", port=27019)
#    app.run()