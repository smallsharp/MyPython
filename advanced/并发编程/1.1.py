from threading import Thread


class CountdownTask:
    def __init__(self):
        self._running = True

    def stop(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('TTTT', n)
            n -= 1
            import time
            time.sleep(2)


c = CountdownTask()
t = Thread(target=c.run, args=(20,))
t.start()
# c.stop()
t.join()