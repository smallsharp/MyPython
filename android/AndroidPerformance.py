import os


def adbPath():
    if os.environ["ANDROID_HOME"]:
        return os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb.exe")
    raise RuntimeError("当前没有配置Android开发环境！")


def get_devices():
    """
    获取所有的连接设备
    :return:
    """
    res = os.popen(adbPath() + " devices").readlines()
    return [i.split()[0] for i in res if 'devices' not in i and len(i) > 5]


class AndroidPerformance:

    def __init__(self, device, packageName):
        self.adb = adbPath()
        self.device = device
        self.packageName = packageName

    @property
    def pss(self):
        res = os.popen("adb -s {} shell dumpsys meminfo {}".format(self.device, self.packageName)).read()
        # print(type(res)) # <class 'str'>
        if res.startswith("No process"):
            raise Exception("没有检测到{}的进程".format(self.packageName))
        part = res[res.find("TOTAL"): res.find(
            "Objects")]  # TOTAL   161474   148660     8540        0   175791   160807    14983
        return int(part.split()[1]) / 1024

    @property
    def heap(self):
        res = os.popen("adb -s {} shell dumpsys meminfo {}".format(self.device, self.packageName)).read()
        if res.startswith("No process"):
            raise Exception("没有检测到{}的进程".format(self.packageName))
        part = res[res.find("Dalvik Heap"): res.find("Dalvik Other")]
        # print(part) # Dalvik Heap    13508    12832        0        0    33126    29166     3960
        return int(part.split()[6]) / 1024

    @property
    def cpu(self):
        res = os.popen("adb -s {} shell top -n 1 -s cpu|findstr {}".format(self.device, self.packageName)).read()
        # print("cpu:",res) # 14637  1   0% S    68 2893816K 103580K  fg u0_a582  com.tude.android
        if res.startswith("No process"):
            raise Exception("没有检测到{}的进程".format(self.packageName))
        return res[res.find("%") - 3: res.find("%")]

    def uid(self):
        res = os.popen("adb -s {} shell dumpsys package {} | grep userId".format(self.device, self.packageName))
        return res.split("=")[1]


p = AndroidPerformance("85GBBMA2353T", "com.tude.android")

import time

for i in range(1000):
    print("pss:{}; heap:{}; cpu:{}".format(p.pss, p.heap, p.cpu))
    time.sleep(0.1)
