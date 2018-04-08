# coding=utf-8

import os
import re


def adbPath():
    """
    获取系统中的adb.exe路径
    :return:
    """
    return os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb.exe")


class ADBTools:
    """
    Android 命令行工具合集
    """

    def __init__(self, device=None):
        """
        初始化设备
        :param device:未传，使用默认连接的第一个设备，如果传，则使用传入的设备
        """
        self.adbPath = adbPath()
        self.device = None
        if not device:
            devices = self.get_devices()  # 查找当前已连接的设备
            if devices:
                self.device = devices[0]  # 如果有，取第一个做为默认设备
            else:
                raise Exception("没有发现可用设备，请检查设备连接！")
        else:
            self.device = device

    def adb(self, args):
        """
        执行adb命令
        :param args:参数
        :return:
        """
        cmd = "{adb} {args}".format(adb=self.adbPath, args=str(args))
        return os.popen(cmd)

    def shell(self, args):
        """
        执行adb shell命令
        :param args:参数
        :return:
        """
        cmd = "{} -s {} shell {}".format(self.adbPath, self.device, str(args))
        print(cmd)
        return os.popen(cmd)

    def get_devices(self):
        """
        获取所有的连接设备
        :return: ['85GBBMA2353T']
        """
        res = self.adb('devices').readlines()
        return [i.split()[0] for i in res if 'devices' not in i and len(i) > 5]

    def get_current_application(self):
        """
        获取当前运行的应用信息
        :return:
        """
        return self.shell('dumpsys window w | {} \/ | {} name='.format("findstr", "findstr")).read()

    def get_current_package(self):
        """
        获取当前运行app包名
        :return:
        """
        reg = re.compile(r'name=(.+?)/')
        return re.findall(reg, self.get_current_application())[0]

    def get_current_activity(self):
        """
        获取当前运行activity
        :return: package/activity
        """
        reg = re.compile(r'name=(.+?)\)')
        return re.findall(reg, self.get_current_application())[0]

    def get_device_sdk_version(self):
        """
        获取设备SDK版本
        :return:
        """
        return self.shell('getprop ro.build.version.sdk').read().strip()

    def get_screen_normal_size(self):
        """
        获取设备屏幕分辨率 >> 标配
        :return:
        """
        return self.shell('wm size').read().strip().split()[-1].split('x')

    def get_screen_reality_size(self):
        """
        获取设备屏幕分辨率 >> 实际分辨率
        :return:
        """
        x = 0
        y = 0
        l = self.shell(r'getevent -p | {} -e "0"'.format("findstr")).readlines()
        for n in l:
            if len(n.split()) > 0:
                if n.split()[0] == '0035':
                    x = int(n.split()[7].split(',')[0])
                elif n.split()[0] == '0036':
                    y = int(n.split()[7].split(',')[0])
        return x, y

    def call(self, number):
        """
        拨打电话
        :param number:
        :return:
        """
        self.shell('am start -a android.intent.action.CALL -d tel:%s' % number)

    def open_url(self, url):
        """
        打开网页
        :return:
        """
        self.shell('am start -a android.intent.action.VIEW -d %s' % url)

    def start_app(self, component):
        """
        启动一个应用
        e.g: com.android.settings/com.android.settings.Settings
        """
        self.shell("am start -n %s" % component)

    def input(self,text):
        """
        发送一个输入事件
        :param text:
        :return:
        """
        self.shell('input text {}'.format(text))

    def send_keyevent(self, keycode):
        """
        发送一个按键事件
        https://developer.android.com/reference/android/view/KeyEvent.html
        :return:
        """
        self.shell('input keyevent %s' % keycode)

    def click(self, x, y):
        """
        发送一个点击事件
        :return:
        """
        self.shell('input tap {} {}'.format(x, y))

    def swipe(self, fromx, fromy, tox, toy, time=500):
        """
        发送一个滑动 或  按压事件
        :param fromx: 起点的x坐标
        :param fromy: 起点的y坐标
        :param tox: 终点的x坐标
        :param toy: 重点的y坐标
        :param time:默认为500毫秒
        :return:None
        """
        self.shell('input swipe {} {} {} {} {}'.format(fromx, fromy, tox, toy, time))

    def clear_cache(self, package):
        """
        清理应用数据 adb -s 85GBBMA2353T shell pm clear com.tude.android
        :return:
        """
        return self.shell('pm clear {package}'.format(package=package))


if __name__ == '__main__':
    tool = ADBTools()
    # print(tool.get_devices())
    # print(tool.get_current_application())
    # print(tool.get_current_package())
    # print(tool.get_current_activity())
    # print(tool.get_device_sdk_version())
    # print(tool.get_screen_normal_size())
    # print(tool.get_screen_reality_size())

    # tool.call(18516213133)

    import time

    # tool.start_app("com.android.settings/com.android.settings.Settings")
    # time.sleep(0.5)
    # tool.open_url("http://www.baidu.com")

    # tool.start_app("com.tude.android/com.tude.android.MainActivity")
    # time.sleep(0.5)
    # tool.start_app("com.tude.android/com.tude.android.gallery.GalleryActivity")

    tool.swipe(900,500,100,500)
    time.sleep(1)
    tool.swipe(100,500,900,500)
