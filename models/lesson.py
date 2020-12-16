#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:45:27 2020

@author: linxiangling
"""

from bson.objectid import ObjectId
from models import db

from flask_bcrypt import Bcrypt
import sys

from datetime import datetime,timezone,timedelta


sys.path.insert(0, './models')

    
#課程資訊(出缺席紀錄)
def get_lesson_info(lesson_id):
    return db.LESSON_COLLECTION.find_one({'lesson_id':lesson_id})
      

#lesson列表(出缺席紀錄，依student) 
def get_lesson_list(course_id):
    return db.COURSE_COLLECTION.find_one({'course_id':course_id})['lesson_list']

#編輯lesson資訊(編輯出缺席)
def update_lesson_attendence_info(lessonid, attendence_list):
    db.LESSON_COLLECTION.update_one(lessonid, {'$set':{'attendence':attendence_list}})


# 依據 lesson_id 找特定課程
def get_by_lessonid(lesson_id):
    item = db.LESSON_COLLECTION.find_one({'lesson_id' : lesson_id})
    return item

def get_by_courseid(course_id):
    items = db.LESSON_COLLECTION.find({'course_id' : course_id})
    return items

def update_lesson_communication_book(lesson_id,data):
    homework = data['homework']
    progress = data['progress']
    db.LESSON_COLLECTION.update_one({'lesson_id': lesson_id },{'$set':{'homework' : homework}})
    db.LESSON_COLLECTION.update_one({'lesson_id': lesson_id },{'$set':{'progress' : progress}})


def update_lesson_grade(lesson_id,data):
    db.LESSON_COLLECTION.update_one({'lesson_id':lesson_id},{'$set':{'quiz':data}})


