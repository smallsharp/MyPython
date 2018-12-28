# 协程  greenlet.getcurrent()
import time
import threading
import greenlet

DIC = {}


def task(i):
    # ident = threading.get_ident()
    ident = greenlet.getcurrent()
    if ident in DIC:
        DIC[ident]['stack'] = i
    else:
        DIC[ident] = {'stack': i}
    time.sleep(1)

    print('threadId:{} , data:{}'.format(ident, DIC[ident]))


for i in range(10):
    t = threading.Thread(target=task, args=(i,))
    t.start()

# print(DIC)
