import datetime
import time

now = datetime.datetime.now()

# 当前时间戳
timestamp = datetime.datetime.now().timestamp()

# 时间戳转 日期
dt = datetime.datetime.fromtimestamp(timestamp)
print(type(timestamp), type(dt))  # <class 'float'> <class 'datetime.datetime'>

## --------------------------------------第一种方式------------------------------------------------------------------- ##

date_str = now.strftime('%Y-%m-%d')

# 转成datetime
dt = now.strptime(date_str, '%Y-%m-%d')
timestamp = time.mktime(dt.timetuple())
print(timestamp, date_str, dt)

## --------------------------------------第二种方式-------------------------------------------------------------------##

d2 = datetime.datetime(2018, 12, 24)

print(type(d2))
timestamp = time.mktime(d2.timetuple())
print(timestamp)
