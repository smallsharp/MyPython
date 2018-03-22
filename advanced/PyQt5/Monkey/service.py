class MonkeyServer:

    def __init__(self, param):
        self.param = param
        pass

    def run(self):
        import os
        # cmd = "adb -s " + self.param.get("device") + self.param["package"]
        "adb shell monkey -p 包名 -s 500 --ignore-crashes --ignore-timeouts --monitor-native-crashes -v -v -v 10000 > E:\monkey_log\test1.txt"
        cmd = "adb -s {0} shell monkey -p {1}".format(self.param["device"],self.param["package"])
        print(cmd)
        # os.popen(self.param)


if __name__ == '__main__':
    # param = {"device": "xiaomi", "package": "com.tude.android", "delay": 500, "times": 100}
    # m = MonkeyServer(param)
    # m.run()

    event = ["触摸事件", "滑动事件", "轨迹球事件", "导航事件", "主导航事件", "系统按键事件", "页面切换事件"]

    for i, ev in enumerate(event):
        print(i, ev)