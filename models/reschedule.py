#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:47:03 2020

@author: linxiangling
"""


from models import _db
import sys
from datetime import datetime,timedelta


sys.path.insert(0, './models')


#當週補課
def get_week_reschedule():
    now=datetime.now()
    this_week_start = (now - timedelta(days=now.weekday()))#!!!!!!!!!!!
    this_week_start=datetime(year=this_week_start.year, month=this_week_start.month, day=this_week_start.day)
    this_week_end = (now + timedelta(days = 6 - now.weekday()))
    this_week_end=datetime(year=this_week_end.year, month=this_week_end.month, day=this_week_end.day, hour=23, minute=59, second=59)
    return [{'datetime':i['datetime'], 'state':i['state'], 'reservation_list':i['reservation_list'], 'classroom_id':i['classroom_id']} for i in _db.RESCHEDULE_COLLECTION.find({'datetime':{'$gte':this_week_start, '$lte':this_week_end}})]
    
#某天（星期）補課資訊
def get_day_reservation(weekday, time):
    weeks=['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
    Myweekday=-1
    for i in range(len(weeks)):
        if weeks[i]==weekday:
            Myweekday=i
    #print(time)
    
    Mytime=time.split(':')
    
    #print("----------------------------------------")
    #for i in Mytime:
    #    print(i)
        
    hour=Mytime[0]
    minute=Mytime[1]
    now=datetime.now()
    this_week_start_day=(now - timedelta(days=now.weekday()))
    this_week_start = datetime(year=this_week_start_day.year, month=this_week_start_day.month, day=this_week_start_day.day, hour=0, minute=0)
    reservation_time=this_week_start+ timedelta(days=Myweekday, hours=int(hour), minutes=int(minute))
    #print("----------------------------------------")
    #print(reservation_time)
    return _db.RESCHEDULE_COLLECTION.find_one({'datetime':reservation_time})

#開放補課時段
def update_reschedule_state(weekday, time, new_state):
    weeks=['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
    Myweekday=-1
    for i in range(len(weeks)):
        if weeks[i]==weekday:
            Myweekday=i
    Mytime=time.split(':')
    hour=Mytime[0]
    minute=Mytime[1]
    
    now=datetime.now()
    this_week_start = (now - timedelta(days=now.weekday()))   
    
    reservation_time=datetime(year=this_week_start.year, month=this_week_start.month, day=this_week_start.day)+ timedelta(days=Myweekday, hours=int(hour), minutes=int(minute))
    _db.RESCHEDULE_COLLECTION.update({'datetime':reservation_time}, {'$set':{'state':new_state}})


def get_all():
    return _db.RESCHEDULE_COLLECTION.find()

    
    
    
    