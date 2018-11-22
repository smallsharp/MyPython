#coding=utf-8
import datetime

# 获取当天当前日期
t = datetime.datetime.now()
s = datetime.datetime.today()

print('{}-{}-{}'.format(s.year,s.month,s.day))

print(t)
print(t.year)
print(t.month)
print(t.day)
print(t.hour)
print(t.second)

# 时间延后
new = t + datetime.timedelta(days=7)
print(t,new)

# 计算时间价间隔

first = datetime.datetime(2018,2,18,12,00,00)
second = datetime.datetime(2018,2,19,13,00,00)
delta = second-first

print(delta,type(delta))
print(delta.total_seconds() )# 总秒数