# coding=utf-8

import time

start = time.clock()
for i in range(0, 1000):
    if i /  100 in range(0, 10):
        print(i)

end = time.clock()

print(end - start)


while 1:
    print(time.time() )
    time.sleep(1)
