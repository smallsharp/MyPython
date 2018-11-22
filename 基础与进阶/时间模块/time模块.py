# coding=utf-8
import time

# 1. 当前时间的时间戳
# 接收时间戳的函数：localtime,ctime,gmtime
t = time.time()
local_time = time.localtime(t)  # 当地时间的时间元组
gm_time = time.gmtime(t)  # 格林威治时间
print('当前时间戳:%s' % t,type(t))
print('当地时间的时间元组:', local_time)
print('格林威治的时间元组:', gm_time)

# 2. 接收时间元组的函数asctime([tupletime]),返回格式：Mon Jul 23 17:59:47 2018
t1 = time.asctime(local_time)
t2 = time.asctime(gm_time)
print(t1, t2)  # Sat Feb 17 16:55:17 2018

# 3. 接收时间元组的函数strftime([tupletime]),返回指定格式：2018-02-17 16:55:17
t3 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
t4 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
t5 = time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
print(t3, t4)
print(t5)  # 18-02-17 16:55:17

# 4. 格式化时间 转成 时间元组
pt = time.strptime("2017-09-02 17:21:00", "%Y-%m-%d %H:%M:%S")
print(pt)

# 5. 时间元组转为时间戳
t = time.mktime(pt)
print(t)
