#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:12:14 2021

@author: linxiangling
"""

from bson.objectid import ObjectId
from models import _db

from flask_bcrypt import Bcrypt
import sys

from datetime import datetime,timezone,timedelta


sys.path.insert(0, './models')


#拿到各collection id(計算ID用)
def get_collection_id():
    data=_db.COLLECTION_ID_COLLECTION.find_one({'_id':ObjectId("600508e60168ed5deab84a23")})
    return {'course_now':data['course_now'], 'user_now':data['user_now'], 'classroom_now':data['classroom_now']} 

#編輯各collection id（加一）
def update_collection_id(x, now):
    if x==1:    #course
        _db.COLLECTION_ID_COLLECTION.update_one({'_id':ObjectId("600508e60168ed5deab84a23")}, {'$set':{'course_now':now+1}})
    elif x==2:   #user
        _db.COLLECTION_ID_COLLECTION.update_one({'_id':ObjectId("600508e60168ed5deab84a23")}, {'$set':{'user_now':now+1}})
    else:   #classroom
        _db.COLLECTION_ID_COLLECTION.update_one({'_id':ObjectId("600508e60168ed5deab84a23")}, {'$set':{'classroom_now':now+1}})