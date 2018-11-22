from datetime import datetime

now = datetime.today()

# 当前时间==>年 月 日 时 分 秒
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

from datetime import timedelta

date1 = datetime(2018, 12, 10)
later1 = date1 + timedelta(10)  # 10天后的日期 == > 2018-12-20 00:00:00
later2 = date1 + timedelta(hours=10)  # 10小时后的日期 == > 2018-12-10 10:00:00
later3 = date1 + timedelta(minutes=10)  # 10分钟后的日期 == > 2018-12-10 00:10:00

# 计算时间差
date2 = datetime(2019, 2, 22)

dif = date2 - date1
print(dif.days)  # 74
print(dif.seconds)
