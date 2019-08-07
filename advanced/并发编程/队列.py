from queue import Queue
from time import sleep
import threading

# q = Queue(4)
#
# print(q.qsize())
# print(q.full())
# print(q.get())  # 阻塞的，如果队列为空，则一直等待
# print(q.put(1))  # 阻塞的，如果队列已满，则一直等待


def put_value(q):
    i = 0
    while True:
        q.put(i)
        i += 1
        sleep(2)


def get_value(q):
    while True:
        print('从队列中取出:{}'.format(q.get()))


def main():
    q = Queue(4)
    t1 = threading.Thread(target=put_value, args=[q])
    t2 = threading.Thread(target=get_value, args=[q])
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
