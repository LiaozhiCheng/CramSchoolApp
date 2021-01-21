#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:43:44 2020

@author: linxiangling
"""

from bson.objectid import ObjectId
from models import _db, collectionid

from flask_bcrypt import Bcrypt
import sys

from datetime import datetime,timezone,timedelta


sys.path.insert(0, './models')


#補習班當日課表(回傳當日course)
def get_today_course():
    dt1 = datetime.utcnow().replace(tzinfo=timezone.utc) 
    dt2 = dt1.astimezone(timezone(timedelta(hours=8)))  # 轉換時區 -> 東八區
    weeks=['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
    weekday=weeks[dt2.weekday()]
    return [{'course_id':i['course_id'], 'name':i['name'], 'start_time':i['start_time'], 'course_time':i['course_time'], 'teacher':i['teacher'], 'summary':i['summary'], 'current_lesson_id':i['current_lesson_id'],'lesson_list':i['lesson_list'], 'student_list':i['student_list'], 'classroom':i['classroom']} for i in _db.COURSE_COLLECTION.find({'course_time':{'$regex':''+weekday+'$'}})]  #星期三是2??



#所有課程列表
def get_course_list():
    return [{'name':i['name'], 'course_time':i['course_time'], 'course_id':i['course_id'], 'teacher':i['teacher'], 'classroom':i['classroom'], 'start_time':i['start_time']} for i in _db.COURSE_COLLECTION.find()]

#課程詳細資訊(name)
def get_course_info_by_name(name):
    return [{'name':i['name'], 'course_time':i['course_time'], 'course_id':i['course_id'], 'teacher':i['teacher'], 'classroom':i['classroom'], 'start_time':i['start_time']} for i in _db.COURSE_COLLECTION.find({'name':name})]


#課程詳細資訊(id)
def get_course_info(course_id):
    return _db.COURSE_COLLECTION.find_one({'course_id':course_id})


#新增課程
def insert_course(name, start_time, course_time, teacher, summary, current_lesson_id, student_list, classroom):
    #取得目前course id值
    course_now=collectionid.get_collection_id()['course_now']
    course_id="C-"+str(course_now+1).zfill(3)
    collectionid.update_collection_id(1, course_now)

    start_time=datetime.strptime(start_time, '%Y-%m-%d')
    lesson_list=[]
    
    coursedict={'course_id':course_id, 'name':name, 'start_time':start_time, 'course_time':course_time, 'teacher':teacher, 'summary':summary, 'current_lesson_id':current_lesson_id, 'lesson_list':lesson_list, 'student_list':student_list, 'classroom':classroom}
    _db.COURSE_COLLECTION.insert_one(coursedict)

    start_course_time=course_time.split("~")[0]
    start_lesson_time=start_time + timedelta(hours = int(start_course_time.split(":")[0]), minutes=int(start_course_time.split(":")[1]))
    for i in range(10):      #預設新增10堂課(lesson)  
        insert_empty_lesson(course_id, start_lesson_time)
        start_lesson_time=start_lesson_time + timedelta(days = 7)
    return course_id
        
#新增空lesson（course新建時附帶預設新增十堂）
def insert_empty_lesson(course_id, lesson_time):
    #用資料庫筆數當id後綴，會有問題，之後改用static變數一直往上累計，用course_id當id中間
    lesson_id="L-"+course_id.split("-")[1]+str(_db.LESSON_COLLECTION.count_documents({})+1).zfill(3)
    course_id=course_id
    progress=""
    homework={}
    attendence=[]
    quiz={'quiz_name':'', 'grade_list':'[]'}
    lesson_time=lesson_time
    
    _db.COURSE_COLLECTION.update_one({'course_id':course_id}, {'$push':{'lesson_list':lesson_id}})

    lessondict={'lesson_id':lesson_id, 'course_id':course_id, 'progress':progress, 'homework':homework, 'attendence':attendence, 'quiz':quiz, 'lesson_time':lesson_time}
    _db.LESSON_COLLECTION.insert_one(lessondict)
     
#刪除課程
def delete_course(course_id):
    _db.COURSE_COLLECTION.delete_one(course_id)
    
#編輯課程
def update_course(courseid, coursedict):
    _db.COURSE_COLLECTION.update_one(courseid, {'$set':coursedict})
    
def get_course_student_list(course_id):
    return _db.COURSE_COLLECTION.find_one({'course_id':course_id})['student_list']

# 依據 course_id 找特定課程
def get_by_courseid(course_id):
    item = _db.COURSE_COLLECTION.find_one({'course_id' : course_id})
    return item  
#課程學生清單   
#def get_course_student_list(course_id):
#    return db.COURSE_COLLECTION.find_one({'course_id':course_id})['student_list']
    
