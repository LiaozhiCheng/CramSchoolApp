#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:45:27 2020

@author: linxiangling
"""


from models import _db
import sys


sys.path.insert(0, './models')

    
#課程資訊(出缺席紀錄)
def get_lesson_info(lesson_id):
    return _db.LESSON_COLLECTION.find_one({'lesson_id':lesson_id})
      

#lesson列表(出缺席紀錄，依student) 
def get_lesson_list(course_id):
    return _db.COURSE_COLLECTION.find_one({'course_id':course_id})['lesson_list']

#編輯lesson資訊(編輯出缺席)
def update_lesson_attendence_info(lessonid, attendence_list):
    _db.LESSON_COLLECTION.update_one(lessonid, {'$set':{'attendence':attendence_list}})