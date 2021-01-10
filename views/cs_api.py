#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:21:14 2020

@author: linxiangling
"""

from flask import Blueprint, jsonify, request
from models import user, course, classroom, lesson, reschedule
import json
from datetime import datetime
from flask_security import roles_required, login_required


cs_api=Blueprint('cs_api', __name__)


@cs_api.route('cs_schedule')
#@roles_required('CSManager')
#補習班當日課表    ok
def cs_schedule():
    return jsonify(course.get_today_course())
  
@cs_api.route('stu_member_list')
#@roles_required('CSManager')
#學生成員名單與基本資料    ok
def stu_member_list():
    return jsonify(user.get_student_list())
    
@cs_api.route('tea_member_list')
#@roles_required('CSManager')
#教師成員名單與基本資料    ok
def tea_member_list():
    return jsonify(user.get_teacher_list())

@cs_api.route('user_detail_info', methods=['get'])
#@roles_required('CSManager')
#使用者個人資料    ok
def user_detail_info():
    name=request.values.get('name')
    #name不能為空
    if name == "":
        return jsonify({'message', '資料不得為空'})
    user_detail_info_list=[]
    for i in user.get_user_info_by_name(name):
        
        course_name_list=[]
        course_list=i['course_list']
        for j in course_list:
            course_name_list.append(course.get_course_info(j)['name'])  #course_list中的id應該不會有錯
            
        user_detail_info_list.append({'course_list':i['course_list'], 'email':i['email'], 'name':i['name'], 'phone':i['phone'], 'role':i['role'], 'user_id':i['user_id'], 'course_name_list':course_name_list})
    return jsonify(user_detail_info_list)
    

@cs_api.route('insert_user_detail_info', methods=['post'])
#@roles_required('CSManager')
#新增成員    ok
def insert_user_detail_info():
    user_json=request.get_json()
    
    password=user_json['password']
    name=user_json['name']
    course_id=user_json['course_list'][0]  #一開始只能新增一堂課
    phone=user_json['phone']
    email=user_json['email']
    major=[user_json['major']]  #前端只會給字串，為了資料庫型態一致(array)自己包成list
    personal_plan=""
    role=user_json['role']
    #password, name, role不得為空
    if password=="" or name=="" or role=="":
        return jsonify({'message', '資料不得為空'})
    if major=="null":
        major=[]
    user_id = user.insert_user(password, name, course_id, phone, email, major, personal_plan, role)
    print("user_id")
    print(user_id)
    print("course_id")
    print(course_id)
    #將該成員選的course加入該course的list
    course.update_course(course_id, course.get_course_info(course_id)['student_list'].append(user_id))
    return jsonify({'0':0})   #之後redirect
    
@cs_api.route('delete_user_detail_info')
#@roles_required('CSManager')
#刪除成員   ok
def delete_user_detail_info():
    user_id=request.values.get('user_id')
    #user_id不得為空
    if user_id=="":
        return jsonify({'message', '資料不得為空'})
    userid={'user_id':user_id}
    #先把該成員從所有course的list中刪掉
    for i in user.get_user_info(user_id)['course_list']:
        coursedict = {'student_list': course.get_course_info(i)['student_list'].remove(user_id)}
        course.update_course(i, coursedict)
    user.delete_user(userid)
    return jsonify({'0':0})   #之後redirect
    
@cs_api.route('edit_user_detail_info', methods=['post'])
#@roles_required('CSManager')
#編輯成員   要把學生加入course的student_list中    ok
def edit_user_detail_info():
    user_json=request.get_json()
    
    #password personal_plan role不會改
    user_id=user_json['user_id']
    name=user_json['name']
    delete_from_course_list=user_json['delete_from_course_list']    #要刪掉的course之id
    course_list=user_json['course_list']    #所有的course，含原本有的與要新增的
    phone=user_json['phone']
    email=user_json['email']
    major=[user_json['major']]
    #user_id, name不得為空
    if user_id=="" or name=="":
        return jsonify({'message', '資料不得為空'})
    userid={'user_id':user_id}
    userdict={'user_id': user_id, 'name':name, 'course_list':course_list, 'phone':phone, 'email':email, 'major':major}
    user.update_user(userid, userdict)
    
    #將學生加入course的student_list中，會很慢？？？？？
    for i in course_list:
        student_list=course.get_course_info(i)['student_list']  #從course_list刪除course，也要把student從course中的student_list刪除
        if user_id not in student_list:
            student_list.append(user_id)
            course.update_course({'course_id':i}, {'student_list':student_list})
            
    #從course_list刪除course，也要把student從course中的student_list刪除
    for i in delete_from_course_list:
        student_list=course.get_course_info(i)['student_list']
        student_list.remove(user_id)
        course.update_course({'course_id':i}, {'student_list':student_list})
        
    return jsonify({'0':0})   #之後redirect

@cs_api.route('cs_course_list')
#@roles_required('CSManager')
#所有課程列表   ok
def cs_course_list():
    return jsonify(course.get_course_list())

#@cs_api.route('cs_course_info', methods=['get'])
#課程詳細資訊(id)
#def cs_course_info():
#    course_id=request.values.get('course_id')
#    return jsonify(course.get_course_info(course_id))

@cs_api.route('cs_course_info_by_name', methods=['get'])
#@roles_required('CSManager')
#課程詳細資訊(name)    ok
def cs_course_info_by_name():
    name=request.values.get('name')
    #name不得為空
    if name=="":
        return jsonify({'message', '資料不得為空'})
    return jsonify(course.get_course_info_by_name(name))

@cs_api.route('cs_course_student_list', methods=['get'])
#@roles_required('CSManager')
#課程學生清單   ok
def cs_course_student_list():
    course_id=request.values.get('course_id')
    temp=[]
    #course_id不得為空
    if course_id=="":
        return jsonify({'message', '資料不得為空'})
    for i in course.get_course_info(course_id)['student_list']:
        temp.append(user.get_user_info(i)['name'])
    return jsonify(temp)

@cs_api.route('insert_cs_course_info', methods=['post'])
#@roles_required('CSManager')
#新增課程   ok
def insert_cs_course_info():
    course_json=request.get_json()
    
    name=course_json['name']
    start_time=course_json['start_time']
    course_time=course_json['course_time']
    teacher=course_json['teacher']
    summary=course_json['summary']
    #!!!!!!!!!!!!!!!!!先設null有用到再說，可設為course中lesson_list的最後一個
    current_lesson_id=""
    student_list=[]
    
    classroom=course_json['classroom']
    #name, start_time, course_time, teacher不得為空
    if name=="" or start_time=="" or course_time=="" or teacher=="":
        return jsonify({'message', '資料不得為空'})
    course.insert_course(name, start_time, course_time, teacher, summary, current_lesson_id, student_list, classroom)
    return jsonify({'0':0})   #之後redirect
    
@cs_api.route('delete_cs_course_info', methods=['get'])
#@roles_required('CSManager')
#刪除課程   ok
def delete_cs_course_info():
    course_id=request.values.get('course_id')
    #course_id不得為空
    if course_id=="":
        return jsonify({'message', '資料不得為空'})
    courseid={'course_id':course_id}
    course.delete_course(courseid)
    return jsonify({'0':0})   #之後redirect
    
@cs_api.route('edit_cs_course_info', methods=['post'])
#@roles_required('CSManager')
#編輯課程    ok
def edit_cs_course_info():
    course_json=request.get_json()
    
    course_id=course_json['course_id']
    name=course_json['name']
    start_time=course_json['start_time']
    course_time=course_json['course_time']
    teacher=course_json['teacher']
    summary=course_json['summary']
    #current_lesson_id=""        #!!!!!!!!!!!!!!!!!先設null有用到再說
    #student_list=course_json['student_list']
    classroom=course_json['classroom']
    
    #course_id, name, start_time, course_time, teacher不得為空
    if course_id=="" or name=="" or start_time=="" or course_time=="" or teacher=="":
        return jsonify({'message', '資料不得為空'})
    start_time=start_time.split("T")[0]     #拿到日期
    start_time=datetime. strptime(start_time, '%Y-%m-%d')
    courseid={'course_id':course_id}
    coursedict={'course_id':course_id, 'name':name, 'start_time':start_time, 'course_time':course_time, 'teacher':teacher, 'summary':summary, 'classroom':classroom}
    course.update_course(courseid, coursedict)
    return jsonify({'0':0})   #之後redirect

@cs_api.route('cs_course_attendence', methods=['get'])
#@roles_required('CSManager')
#出缺席紀錄(依lesson)    ok
def cs_course_attendence():
    lesson_id=request.values.get('lesson_id')
    #lesson_id不得為空
    if lesson_id=="":
        return jsonify({'message', '資料不得為空'})
    lesson_attendence=lesson.get_lesson_info(lesson_id)['attendence'] #該lesson有出席的學生
    
    all_student=course.get_course_info(lesson.get_lesson_info(lesson_id)['course_id'])['student_list']    #該course的所有學生
    
    temp=[]
    for i in all_student:
        user_info=user.get_user_info(i)
        if i in lesson_attendence:
            temp.append({user_info['name']:'出席', 'user_id':user_info['user_id']})
        else:
            temp.append({user_info['name']:'缺席', 'user_id':user_info['user_id']})
    return jsonify(temp)


@cs_api.route('cs_student_attendence', methods=['get'])
#@roles_required('CSManager')
#出缺席紀錄(依student)        ok
def cs_student_attendence():
    user_id=request.values.get('user_id')
    course_id=request.values.get('course_id')
    #user_id, course_id不得為空
    if user_id=="" or course_id=="":
        return jsonify({'message', '資料不得為空'})
    lesson_list=lesson.get_lesson_list(course_id)  #該course的lesson_list
    
    temp=[]
    for i in lesson_list:
        lesson_info=lesson.get_lesson_info(i)
        if user_id in lesson_info['attendence']:
            temp.append({str(lesson_info['lesson_time']):'出席', 'lesson_id':lesson_info['lesson_id']})
        else:
            temp.append({str(lesson_info['lesson_time']):'缺席', 'lesson_id':lesson_info['lesson_id']})
    return jsonify(temp)

@cs_api.route('edit_cs_course_attendence', methods=['get'])
#@roles_required('CSManager')
#編輯出缺席紀錄    ok
def edit_cs_course_attendence():    #isAttendence為bool，表示是否出席
    user_id=request.values.get('user_id')
    lesson_id=request.values.get('lesson_id')
    isAttendence=bool(int(request.values.get('isAttendence')))  #前端傳0或1
    #user_id, lesson_id, isAttendence不得為空
    if user_id=="" or lesson_id=="" or isAttendence=="":
        return jsonify({'message', '資料不得為空'})
    if isAttendence==True and user_id not in lesson.get_lesson_info(lesson_id)['attendence']:
        temp=lesson.get_lesson_info(lesson_id)['attendence']
        temp.append(user_id)
        lesson.update_lesson_attendence_info({'lesson_id':lesson_id}, temp)
    elif isAttendence==False and user_id in lesson.get_lesson_info(lesson_id)['attendence']:
        temp=lesson.get_lesson_info(lesson_id)['attendence']
        temp.remove(user_id)
        lesson.update_lesson_attendence_info({'lesson_id':lesson_id}, temp)
    return jsonify({'0':0})   #之後redirect
    
@cs_api.route('cs_classroom_info', methods=['get'])
#@roles_required('CSManager')
#教室資訊(classroom_id)      ok
def cs_classroom_info():
    classroom_id=request.values.get('classroom_id')
    #classroom_id不得為空
    if classroom_id=="":
        return jsonify({'message', '資料不得為空'})
    return jsonify(classroom.get_classroom_info(classroom_id))

@cs_api.route('cs_classroom_list', methods=['get'])
#@roles_required('CSManager')
#教室資訊列表    ok
def cs_classroom_list():
    return jsonify(classroom.get_classroom_list())

@cs_api.route('cs_classroom_info_by_name', methods=['get'])
#@roles_required('CSManager')
#教室資訊(name)    ok
def cs_classroom_info_by_name():
    name=request.values.get('name')
    #name不得為空
    if name=="":
        return jsonify({'message', '資料不得為空'})
    return jsonify(classroom.get_classroom_info_by_name(name))


@cs_api.route('insert_cs_classroom_info', methods=['get'])
#@roles_required('CSManager')
#新增教室資訊  ok
def insert_cs_classroom_info():
    name=request.values.get('name')
    capacity=int(request.values.get('capacity'))
    #name, capacity不得為空
    if name=="" or capacity=="":
        return jsonify({'message', '資料不得為空'})
    classroom.insert_classroom(name, capacity)
    return jsonify({'0':0})   #之後redirect

@cs_api.route('delete_cs_classroom_info', methods=['get'])
#@roles_required('CSManager')
#刪除教室資訊    ok
def delete_cs_classroom_info():
    classroom_id=request.values.get('classroom_id')
    #classroom_id不得為空
    if classroom_id=="":
        return jsonify({'message', '資料不得為空'})
    classroomid={'classroom_id':classroom_id}
    classroom.delete_classroom(classroomid)
    return jsonify({'0':0})   #之後redirect
 
@cs_api.route('edit_cs_classroom_info', methods=['get'])
#@roles_required('CSManager')
#編輯教室資訊    ok
def edit_cs_classroom_info():
    classroom_id=request.values.get('classroom_id')
    name=request.values.get('name')
    capacity=int(request.values.get('capacity'))
    #classroom_id, name, capacity不得為空
    if classroom_id=="" or name=="" or capacity=="":
        return jsonify({'message', '資料不得為空'})
    classroomid={'classroom_id':classroom_id}
    classroomdict={'classroom_id':classroom_id, 'name':name, 'capacity':capacity}
    classroom.update_classroom(classroomid, classroomdict)
    return jsonify({'0':0})   #之後redirect



@cs_api.route('cs_reschedule_list')
#@roles_required('CSManager')
#補課頁面資訊(當週每個時段是否開放補課、是否滿)     ok
def cs_reschedule_list():
    weeks=['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
    temp=[]
    for i in reschedule.get_week_reschedule():
        Myweekday=weeks[i['datetime'].weekday()]
        
        if len(i['reservation_list']) >= classroom.get_classroom_info(i['classroom_id'])['capacity']:
            temp.append({'weekday':Myweekday, 'full':True, 'datetime':i['datetime'], 'state':i['state'], 'reservation_list':i['reservation_list'], 'classroom_id':i['classroom_id']})
        else:
            temp.append({'weekday':Myweekday, 'full':False, 'datetime':i['datetime'], 'state':i['state'], 'reservation_list':i['reservation_list'], 'classroom_id':i['classroom_id']})
    return jsonify(temp)

@cs_api.route('cs_reschedule_info', methods=['get'])
#@roles_required('CSManager')
#補課詳細資訊(前端給星期幾與幾點幾分)    ok
#前端要該星期該時段有誰(name) 是補什麼lesson(lesson_time)
def cs_reschedule_info():
    weekday=request.values.get('weekday')
    time=request.values.get('time')
    #weekday, time不得為空
    if weekday=="" or time=="":
        return jsonify({'message', '資料不得為空'})
    data=reschedule.get_day_reservation(weekday, time)
    temp=[]
    if data:
        for i in data['reservation_list']:
            user_name=user.get_user_info(i['user_id'])['name']
            lesson_time=lesson.get_lesson_info(i['lesson_id'])['lesson_time']
            temp.append({'course_name':i['course_name'], 'lesson_time':lesson_time, 'name':user_name})
        return jsonify(temp)  #某星期該時段的reservation_list，reservation_list記該時段所有學生的補課資訊（dict）
    else:
        return jsonify({'0':0})  #要處理null問題

@cs_api.route('edit_cs_reschedule_list', methods=['get'])
#@roles_required('CSManager')
#編輯補課時段    ok
#補課時段每個禮拜日在動生成下週21個補課時段    補習班不可編輯補課時段
def edit_cs_reschedule_list():
    weekday=request.values.get('weekday')
    time=request.values.get('time')
    new_state=bool(int(request.values.get('new_state')))
    #weekday, time, new_state不得為空
    if weekday=="" or time=="" or new_state=="":
        return jsonify({'message', '資料不得為空'})
    reschedule.update_reschedule_state(weekday, time, new_state)
    return jsonify({'0':0})   #之後redirect

@cs_api.route('cs_lesson_id_and_time', methods=['get'])
#@roles_required('CSManager')
#某course所有lesson的id與lesson_time
def cs_lesson_id_and_time():
    course_id=request.values.get('course_id')
    #course_id不得為空
    if course_id=="":
        return jsonify({'message', '資料不得為空'})
    temp=[]
    for i in course.get_course_info(course_id)['lesson_list']:
        lesson_info=lesson.get_lesson_info(i)
        temp.append({'lesson_id':i, 'lesson_time':lesson_info['lesson_time']})
    return jsonify(temp)
    
    

    
    

    

    


    
    
    
    
    
    
    
    
    
    
