

# date 类型示例：

# 2016-12-12运行一次job_function
# sched.add_job(job_function, 'date', run_date=date(2016, 12, 12), args=['text'])
# 2016-12-12 12:00:00运行一次job_function
# sched.add_job(job_function, 'date', run_date=datetime(2016, 12, 12, 12, 0, 0), args=['text'])


#interval 类型

# 每两个小时调一下job_function
# sched.add_job(job_function, 'interval', hours=2)


# cron 类型

# job_function将会在6,7,8,11,12月的第3个周五的1,2,3点运行
# sched.add_job(job_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
# 截止到2016-12-30 00:00:00，每周一到周五早上五点半运行job_function
# sched.add_job(job_function, 'cron', day_of_week='mon-fri', hour=5, minute=30, end_date='2016-12-31')



import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from app.untils.log_builder import sys_logging

scheduler = BlockingScheduler()   # 后台运行

 # 设置为每日凌晨00:30:30时执行一次调度程序
@scheduler.scheduled_job("cron", day_of_week='*', hour='1', minute='30', second='30')
def rebate():
        print("schedule execute")
        sys_logging.debug("statistic scheduler execute success" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    try:
        scheduler.start()
        sys_logging.debug("statistic scheduler start success")
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        sys_logging.debug("statistic scheduler start-up fail")