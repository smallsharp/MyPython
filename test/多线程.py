from threading import Thread
import time 
class race(Thread):
    
    def __init__(self,threadname, interval):
        Thread.__init__(self,name = threadname)
        self.interval = interval
        self.isrunning = True


    def run(self):
        while self.isrunning:
            print ('thread %s is running, time: %s' %(self.getName(), time.ctime()))
            time.sleep(self.interval)

    def stop(self):
        self.isrunning = False

def test():
    thead1 = race('A',1)
    thead2 = race('B',2)
    thead1.start()
    thead2.start()
    time.sleep(5)
    thead1.stop()
    thead2.stop()

if __name__ == '__main__':
    test()