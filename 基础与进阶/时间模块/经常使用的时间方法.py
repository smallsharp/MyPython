import time
import datetime

# 一 获取当前时间
print(time.time())

# 格式化时间1   2018-08-03 17:09:29
print(time.strftime('%Y-%m-%d %H:%M:%S'))

# 格式化时间2  2018-08-03 17:09:29
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 格式化时间3  2018-08-03 17:09:29
print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

# 格式化时间4  2018-08-03 17:09:29
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))


# ----------------------------------------------------------------------------------------------------#

# 2.获取时间差，计算程序的执行时间等：

# 使用time.time()
def t1():
    start = time.time()
    # time.sleep(1)  # 休眠1秒
    end = time.time()
    print(end - start)  # 1.0005199909210205


t1()


# datetime.datetime.now()
def t2():
    start = datetime.datetime.now()
    # time.sleep(1)
    end = datetime.datetime.now()
    print(end - start)  # 0:00:01.000297


t2()

# 3.计算昨天的日期（发散思维，计算其他日期相加、相减等）
d1 = datetime.datetime.now()
d2 = d1 - datetime.timedelta(days=1)
print(d1, d2)

# 4.时间元组 struct_time转化为时间戳

print('datetime.datetime.now():', datetime.datetime.now()) # 2018-08-03 17:05:57.887568
print('datetime.datetime.now().timetuple():', datetime.datetime.now().timetuple())
print('time.mktime(datetime.datetime.now().timetuple()):', time.mktime(datetime.datetime.now().timetuple()))