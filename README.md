# apscheduler
<h2>Apscheduler 简单使用</h2><br>
1, 如果是在其他的框架下使用定时任务，要使用BackgroundScheduler， 程序是无限循环的，就不用自己写无限循环了
2, 如果是独立运行的定时任务，就要使用demo2 的定时任务了 BlockingScheduler.
3，django 中可以直接在总的url中使用 BackgroundScheduler 定时任务，程序会自己运行，如demo1。
<h2>Apscheduler 组件</h2><br>
1，triggers(触发器)： 触发器中包含调度逻辑，每个作业都由自己的触发器来决定下次运行时间。除了他们自己初始配置意外，触发器完全是无状态的。<br>
2, job stores（作业存储器）：存储被调度的作业，默认的作业存储器只是简单地把作业保存在内存中，其他的作业存储器则是将作业保存在数据库中。当作业被保存到一个持久化的作业存储器中的时候，该作业的数据会被序列化，并在加载时被反序列化。作业存储器不能共享调度器。<br>
3, executors（执行器）：处理作业的运行，他们通常通过在作业中提交指定的可调用对象到一个线程或者进城池来进行。当作业完成时，执行器将会通知调度器。<br>
4, schedulers（调度器）：配置作业存储器和执行器可以在调度器中完成，例如添加、修改和移除作业。根据不同的应用场景可以选用不同的调度器，<br>
 可选的有BlockingScheduler,BackgroundScheduler,AsyncIOScheduler,GeventScheduler,TornadoScheduler,TwistedScheduler,QtScheduler 7种<br>
<h2>触发器类型</h2><br>
1, date 一次性定时任务，指定日期<br>
2, interval 在某个时间范围内隔多久执行一次<br>
3, cron 和Linux crontab格式兼容，最强大。<br>
<h2>date 参数</h2><br>
run_date(datetime|str) 作业的运行时间或日期<br>
timezone(datetime.tzinfo|str) 指定时区<br>
<h2>interval 参数</h2><br>
weeks(int)-间隔几周<br>
days(int)-间隔几天<br>
hours(int)-间隔几小时<br>
minutes(int)-间隔几分钟<br>
seconds(int)-间隔多少秒<br>
start_date(datetime|str)-开始日期<br>
end_date(datetime|str)-结束时间<br>
timezone(datetime.tzinfo|str)-时区<br>
<h2>cron参数</h2><br>
year (int|str) – 年，4位数字 <br>
month (int|str) – 月 (范围1-12) <br>
day (int|str) – 日 (范围1-31) <br>
week (int|str) – 周 (范围1-53) <br>
day_of_week (int|str) – 周内第几天或者星期几 (范围0-6 或者 mon,tue,wed,thu,fri,sat,sun) <br>
hour (int|str) – 时 (范围0-23) <br>
minute (int|str) – 分 (范围0-59) <br>
second (int|str) – 秒 (范围0-59) <br>
start_date (datetime|str) – 最早开始日期(包含) <br>
end_date (datetime|str) – 最晚结束时间(包含) <br>
timezone (datetime.tzinfo|str) – 指定时区 <br>
