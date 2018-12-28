'''
	作用：为每个线程创建一个独立的空间，使得线程对自己的空间中的数据进行操作（数据隔离）。
'''

import threading
from threading import local
import time

obj = local()


def task(i):
    obj.value = 1000 + i
    time.sleep(1)
    print('value:{},index:{}'.format(obj.value, i))


for i in range(10):
    t = threading.Thread(target=task, args=(i,))
    t.start()
