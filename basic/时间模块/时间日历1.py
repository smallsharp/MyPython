# coding=utf-8
import time

print(time.time())  # 当前时间戳
print(time.localtime())  # 当前时间元组

# 格式化时间1，使用时间戳
t = time.time()
result = time.ctime(t)
print(result)  # Sat Feb 17 16:55:17 2018

# 格式化时间2，使用时间元组
tm_turple = time.localtime()
result2 = time.asctime(tm_turple)
print(result2)  # Sat Feb 17 16:55:17 2018

# 格式化时间3，使用时间元组
# time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
result3 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(result3)  # 2018-02-17 16:55:17

# 格式化时间4，使用时间元组
# time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
result4 = time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
print(result4)  # 18-02-17 16:55:17

# 格式化时间 转成 时间元组
pt = time.strptime("2017-09-02 17:21:00", "%Y-%m-%d %H:%M:%S")
print(pt)


# 时间元组转为时间戳
t = time.mktime(pt)
print(t)
