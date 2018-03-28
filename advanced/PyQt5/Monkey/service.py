import os
adb = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb.exe ")


def devices():
    """
    获取已连接的设备列表
    :return:
    """
    print("devices")
    cmd = adb + "devices"
    res = os.popen(cmd).readlines()
    # print(res)
    return [i.split()[0] for i in res if 'devices' not in i and len(i) > 5]

def packages():
    """
    获取设备中已安装的第三方包
    :return:
    """
    cmd = adb + "shell pm list packages -3"
    res = os.popen(cmd).readlines()
    return res

class MonkeyServer:

    def __init__(self):
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

    # event = ["触摸事件", "滑动事件", "轨迹球事件", "导航事件", "主导航事件", "系统按键事件", "页面切换事件"]
    #
    # for i, ev in enumerate(event):
    #     print(i, ev)
    print(devices())
