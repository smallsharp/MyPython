import time
from datetime import datetime

s = time.time() - 7 * 86400

print(s)
print(datetime.now())
d = datetime.fromtimestamp(time.time())
print(d.day)

# 计算天数差
d1 = datetime.fromtimestamp(1541051125)
d2 = datetime.fromtimestamp(1538372725)
print(d1, d2)
dif = d1 - d2

print(dif.days)
