#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:46:25 2020

@author: linxiangling
"""

from models import _db
import sys



sys.path.insert(0, './models')


#教室資訊(classroom_id)
def get_classroom_info(classroom_id):
    data = _db.CLASSROOM_COLLECTION.find_one({'classroom_id':classroom_id})     #不能直接return會有bson問題
    return {'classroom_id':data['classroom_id'], 'name':data['name'], 'capacity':data['capacity']}

#教室列表
def get_classroom_list():
    return [{'classroom_id':i['classroom_id'], 'name':i['name'], 'capacity':i['capacity']} for i in _db.CLASSROOM_COLLECTION.find()]

#教室資訊(name)
def get_classroom_info_by_name(name):
    data = _db.CLASSROOM_COLLECTION.find_one({'name':name})     #不能直接return會有bson問題
    return {'classroom_id':data['classroom_id'], 'name':data['name'], 'capacity':data['capacity']}


#新增教室資訊
def insert_classroom(name, capacity):
    #用資料庫筆數當id後綴，會有問題，之後改用static變數一直往上累計
    classroom_id = "R-"+str(_db.CLASSROOM_COLLECTION.count_documents({})+1).zfill(3)
    classroomdict = {'classroom_id':classroom_id, 'name':name, 'capacity':capacity}
    _db.CLASSROOM_COLLECTION.insert_one(classroomdict)
    
#刪除教室資訊
def delete_classroom(classroomid):
    _db.CLASSROOM_COLLECTION.delete_one(classroomid)
    
#編輯教室資訊
def update_classroom(classroomid, classroomdict):
    _db.CLASSROOM_COLLECTION.update_one(classroomid, {'$set':classroomdict})