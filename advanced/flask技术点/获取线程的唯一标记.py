'''
 - 如何获取一个线程的唯一标记？ threading.get_ident()
 - 根据字典自定义一个类似于threading.local功能？
'''

import time
import threading

DIC = {}

def task(i):
    ident = threading.get_ident()
    if ident in DIC:
        DIC[ident]['stack'] = i
    else:
        DIC[ident] = {'stack': i}
    time.sleep(1)

    print('threadId:{} , data:{}'.format(ident, DIC[ident]))
    # print(DIC[ident]['stack'], i)


for i in range(10):
    t = threading.Thread(target=task, args=(i,))
    t.start()

# print(DIC)
