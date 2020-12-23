from flask_apscheduler import APScheduler
from flask import Flask


class Config(object):
    JOBS=[
        {
            'id':'job1',
            'func':'__main__:job_1',
            'args':(1,2),
            'trigger':'cron',
            'day_of_week':2,
            'hour':19,
            'minute':32
        },
        # {
        #     'id':'job2',
        #     'func':'__main__:job_1',
        #     'args':(3,4),
        #     'trigger':'interval',
        #     'seconds':5
        # }
    ]
def job_1(a,b):   # 一個函式，用來做定時任務的任務。
    print(str(a)+' '+str(b))

app=Flask(__name__) # 例項化flask

# app.config.from_object(Config())# 為例項化的flask引入配置

@app.route('/')  # 首頁路由
def hello_world():
    return 'hello'


if __name__=='__main__':
    scheduler=APScheduler()  # 例項化APSchedule
    # scheduler.add_job(id = '123', func = 'job1', trigger = CronTrigger.from_cron(day_of_week = 2, args = (1,2), hour = 19, minute = 41))
    scheduler.init_app(app)  # 把任務列表放進flask
    scheduler.start() # 啟動任務列表
    app.run()  # 啟動flask
    