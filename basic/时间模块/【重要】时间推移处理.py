'''
pip install python-dateutil
'''

from dateutil.relativedelta import relativedelta
import datetime

now = datetime.datetime.today()
print(now)

threemonthago = now + relativedelta(months=-15)
print('三月前:', threemonthago)

twoyearago = now + relativedelta(years=-2, months=-3)
print('两年前：', twoyearago)

tendaylater = now + relativedelta(days=+10)
print('十天后：', tendaylater)  # <class 'datetime.datetime'>

######################### 时间差##########################################

dif = tendaylater - now
print(dif, dif.days, )

delta = relativedelta(now, twoyearago)

print(delta.years, delta.months, delta.days)
