import threading

# 加锁
balance = 0


def change(n):
    global balance
    balance += n
    balance -= n

# 1. 未加锁
# def run_thread(n):
#     for i in range(1000000):
#         change(n)

lock = threading.Lock()  # 获取线程锁

# 2. 加锁
def run_thread(n):
    for i in range(1000000):
        # 获取锁
        lock.acquire()
        try:
            change(n)
        finally:
            # 释放锁
            lock.release()

if __name__=="__main__":
    t1 = threading.Thread(target=run_thread, args=(4,))
    t2 = threading.Thread(target=run_thread, args=(8,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
