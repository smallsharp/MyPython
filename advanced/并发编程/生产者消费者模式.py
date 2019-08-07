import threading
import time
import random

gTotalAmount = 1000  # 生产消费后，剩余总额
gTotalTimes = 10  # 控制生产消费次数
gTimes = 0

gLock = threading.Lock()


class Producer(threading.Thread):

    def run(self):
        global gTotalAmount
        global gTimes

        while True:
            gLock.acquire()
            if gTimes >= gTotalTimes:
                gLock.release()
                break
            amount = random.randint(100, 500)
            gTotalAmount += amount
            gTimes += 1
            gLock.release()
            print('{}生产了{},剩余{}'.format(threading.current_thread(), amount, gTotalAmount))
            time.sleep(0.5)


class Consumer(threading.Thread):

    def run(self):
        global gTotalAmount

        while True:
            gLock.acquire()
            amount = random.randint(100, 300)
            if gTotalAmount >= amount:
                gTotalAmount -= amount
                print('{}消费了{},剩余{}'.format(threading.current_thread(), amount, gTotalAmount))
            else:
                if gTimes >= gTotalTimes:
                    gLock.release()
                    print('{}准备消费{},剩余{},消费失败！'.format(threading.current_thread(), amount, gTotalAmount))
                    break
            gLock.release()
            time.sleep(0.5)


def main():
    for i in range(3):
        consumer = Consumer(name='消费者{}'.format(i))
        consumer.start()

    for i in range(3):
        producer = Producer(name='生产者{}'.format(i))
        producer.start()


if __name__ == '__main__':
    main()
