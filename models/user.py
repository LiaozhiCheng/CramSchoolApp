#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:42:06 2020

@author: linxiangling
"""

from bson.objectid import ObjectId
from models import db

from flask_bcrypt import Bcrypt
import sys

from datetime import datetime,timezone,timedelta


sys.path.insert(0, './models')

#學生成員名單  
def get_student_list():
    return [{'name':i['name'], 'user_id':i['user_id'], 'course_list':i['course_list'], 'email':i['email'], 'phone':i['phone']} for i in db.USER_COLLECTION.find({'role':'student'})]


#老師成員名單
def get_teacher_list():
    return [{'name':i['name'], 'user_id':i['user_id'], 'course_list':i['course_list'], 'email':i['email'], 'phone':i['phone'], 'major':i['major']} for i in db.USER_COLLECTION.find({'role':'teacher'})]

#使用者個人資料(name)   
def get_user_info_by_name(name):
    return [{'name':i['name'], 'user_id':i['user_id'], 'course_list':i['course_list'], 'email':i['email'], 'phone':i['phone'], 'role':i['role']} for i in db.USER_COLLECTION.find({'name':name})]
    


#使用者個人資料(id)   
def get_user_info(user_id):
    return db.USER_COLLECTION.find_one({'user_id':user_id})


#新增成員
def insert_user(password, name, course_list, phone, email, major, personal_plan, role):
    now=datetime.now()
    #用民國年份當id開頭
    register_year= now.year - 1911
    if role == 'teacher':
        #用資料庫筆數當id後綴，會有問題，之後改用static變數一直往上累計
        user_id= str(register_year) + str("-") + "T-"+ str(db.USER_COLLECTION.count_documents({})+1).zfill(3)
    else:
        #用資料庫筆數當id後綴，會有問題，之後改用static變數一直往上累計
        user_id= str(register_year) + str("-") + "S-"+ str(db.USER_COLLECTION.count_documents({})+1).zfill(3)
    
    userdict={'user_id': user_id, 'password': password,  'name':name, 'course_list':course_list, 'phone':phone, 'email':email, 'major':major, 'personal_plan':personal_plan, 'role':role}
    db.USER_COLLECTION.insert_one(userdict)
    

#刪除成員（教師）
def delete_user(userid):
    db.USER_COLLECTION.delete_one(userid)
    
    
#編輯成員 
def update_user(userid, userdict):
    db.USER_COLLECTION.update_one(userid, {'$set':userdict})