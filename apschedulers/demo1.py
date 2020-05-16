# BackgroundScheduler 是非阻塞的，代码执行完程序退出，主要用于集成到其他（web）程序，因为其他程序本身应该就是无限循环的，不能让程序阻塞
# BackingScheduler 阻塞的定时器（内部无限循环），主要用于独立的程序
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor

import logging
logging.basicConfig(filename='scheduler.log')
logging.getLogger('apscheduler').setLevel(logging.WARNING)

# 1, 创建执行器，用于控制任务的并发能力
executor = ThreadPoolExecutor(max_workers=100)

# 2, 创建调度器
scheduler = BackgroundScheduler(exector={'default':executor})


def func1(name,age):    #任务
    print(1/0)
    print(name,age)



# 添加任务
""" 三种触发器
date        只执行一次的定时任务
interval    周期执行， 参数是时间间隔
cron        周期执行，参数是时间
"""
scheduler.add_job(func1,'date',run_date='2020-05-15 16:26:30',args=('zs,','34'))
scheduler.add_job(func1,'interval',minutes=1,args=('lisi','23'))   #days,seconds,       #每隔1分钟执行一次
scheduler.add_job(func1,trigger='cron',minute='*/2',second='1',args=['wangwu','23'])   #second='*/5' 每隔5秒执行一次

def my_listener(event):
    if event.exception:
        print('任务出错了，可以写入日志文件，或发送邮件，短信通知')
        print(event.exception)   #定时任务出错时执行，可以根据需求再add_listener 时添加不同的错误EVENT_JOB_EXECUTED | EVENT_JOB_ERROR
    else:
        print('任务正常执行 ')  # 定时任务正常执行调用时


from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
scheduler.add_listener(my_listener,EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
scheduler.start()



while True:  # 加无线循环是为了让线程一直运行，看到效果，
    import time
    time.sleep(2)