import time
import threading


# 多线程

def music(song, loop):
    for i in range(loop):
        print("listen music:{},time:{}".format(song, i))
        time.sleep(1)

def watch(movie, loop):
    for i in range(loop):
        print("listen music:{},time:{}".format(movie, i))
        time.sleep(2)

if __name__ == "__main__":
    musicThread = threading.Thread(target=music, args=("悟空", 4))
    # movieThread = threading.Thread(target=watch, args=("金刚", 4))
    musicThread.start()
    # movieThread.start()

    print(musicThread.ident)
    print(threading.Thread.getName(musicThread))

    musicThread.join()
    # movieThread.join()

    print("所有线程执行完毕")
