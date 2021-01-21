import datetime

from pymongo import MongoClient

print('0')
db = MongoClient('mongodb+srv://Liao:871029@cluster0-sk2jk.mongodb.net')['CramSchool']

print('1')
reschedule_collection = db['Reschedule']
print('2')


def add_resechedule():
    time_list = list()
    
    for i in range(7):
        time = datetime.datetime(year = 2021,month = 1,day = 18 ,hour = 17) + datetime.timedelta(days=i)
        for j in range(3):
            today_time = time
            today_time = today_time + datetime.timedelta(hours=j*2)
            time_list.append(today_time)
            
    for time in time_list:
        reschedule_dict = dict()
        reschedule_dict['datetime'] = time
        reschedule_dict['state'] = False
        reschedule_dict['reservation_list'] = list()
        reschedule_dict['classroom_id'] = 'R-001'
        reschedule_collection.insert_one(reschedule_dict)
        # reschedule_collection2.insert_one(reschedule_dict)
            
# def add_resechedule_timer():
#     datecount = 0
#     if datetime.datetime.utcnow().weekday() == 0 and datecount == 0:
#         datecount = 1
#         add_resechedule()
#     elif datetime.datetime.utcnow().weekday() == 1 and datecount == 1:
#         datecount = 0
if __name__ == '__main__':
    add_resechedule()

        
        
        
        