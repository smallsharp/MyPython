import time
import threading


class CodingThread(threading.Thread):
    def run(self):
        for i in range(3):
            print('coding:{},线程:{}'.format(i, threading.current_thread()))
            time.sleep(0.5)


class ReadingThread(threading.Thread):
    def run(self):
        for i in range(3):
            print('reading:{},线程:{}'.format(i, threading.current_thread()))
            time.sleep(0.5)


def main():
    t1 = CodingThread()
    t2 = ReadingThread()
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
