import time
import threading


def coding():
    for i in range(3):
        print('coding:{},线程:{}'.format(i, threading.current_thread()))
        time.sleep(0.5)


def reading():
    for i in range(3):
        print('reading:{},线程:{}'.format(i, threading.current_thread()))
        time.sleep(0.5)


# 总共有3个线程，1个主线程，2个子线程
def main():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=reading)
    t1.start()
    t2.start()

    # print(threading.enumerate()) # [<_MainThread(MainThread, started 23408)>, <Thread(Thread-1, started 3804)>, <Thread(Thread-2, started 8592)>]


if __name__ == '__main__':
    main()
