import os


def checkADB():
    if os.environ["ANDROID_HOME"]:
        return os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb.exe")
    raise RuntimeError("当前没有配置Android开发环境！")


class AndroidPerformance:
    cmd_pss = "adb shell dumpsys meminfo "
    cmd_cpu = "adb shell top -n 5 -d 3 -s cpu | grep "

    def __init__(self, packageName):
        self.adb = checkADB()
        self.packageName = packageName

    @property
    def pss(self):
        res = os.popen("adb shell dumpsys meminfo {}".format(self.packageName)).read()
        # print(type(res)) # <class 'str'>
        if res.startswith("No process"):
            raise Exception("没有检测到{}的进程".format(self.packageName))
        part = res[res.find("TOTAL"): res.find("Objects")] # TOTAL   161474   148660     8540        0   175791   160807    14983
        return int(part.split()[1]) / 1024

    @property
    def heap(self):
        res = os.popen("adb shell dumpsys meminfo {}".format(self.packageName)).read()
        if res.startswith("No process"):
            raise Exception("没有检测到{}的进程".format(self.packageName))
        part = res[res.find("Dalvik Heap"): res.find("Dalvik Other")]
        # print(part) # Dalvik Heap    13508    12832        0        0    33126    29166     3960
        return int(part.split()[6]) / 1024

    def cpu(self):
        res = os.popen()
        pass


p = AndroidPerformance("com.tude.android")

import time
for i in range(1000):
    # print("pss:",p.pss)
    print("heap:",p.heap)
    time.sleep(0.5)

