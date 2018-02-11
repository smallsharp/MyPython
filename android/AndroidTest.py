# coding=utf-8
import os


class AndroidTool:

    def __init__(self):
        self.__adb_path = self.__get_adb_path()
        self.__device_id = self.default_device()

    def default_device(self):
        return self.get_devices()[0]

    def __get_adb_path(self):
        """
        获取系统中的adb.exe路径
        :return:
        """
        return os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb.exe")

    def __appoint_device(self, device_id):
        """
        使用-s 指定设备
        :param device_id:
        :return:
        """
        if device_id:
            self.__device_id = " -s {} ".format(device_id)
        else:
            self.__device_id = ""
        return self.__device_id

    def __start_server(self):
        print(self.adb("start-server").readlines())

    def adb(self, args, device_id=None):
        """
        执行adb命令
        :param args:参数
        :return:
        """
        if device_id:
            self.__device_id = device_id
        cmd = "{} {}".format(self.__adb_path, str(args))
        # print(cmd)
        return os.popen(cmd)

    def shell(self, args):
        """
        执行adb shell命令
        :param args:参数
        :return:
        """
        cmd = "{} {} shell {}".format(self.__adb_path, self.__device_id, str(args))
        print(cmd)
        return os.popen(cmd)

    def get_devices(self):
        """
        获取所有的连接设备
        :return:
        """
        res = self.adb('devices').readlines()
        return [i.split()[0] for i in res if 'devices' not in i and len(i) > 5]

    def clear_cache(self, package):
        """
        清理应用数据
        :return:
        """
        self.shell('pm clear {package}'.format(package=package))

    def install(self, device, path):
        """
        安装apk文件
        :return:
        """
        device = "-s " + device
        if device:
            lines = self.adb('{device} install -r {path}'.format(device=device, path=path)).read()
        if 'Success' in lines:
            print('install success')
        if 'Failure' in lines:
            print("install failed!")


if __name__ == '__main__':
    # tool = AndroidTool("LE67A06310143950")
    tool = AndroidTool()

    # print(tool.default_device())

    for device in tool.get_devices():
        # tool.install("app-debug.apk", device=device)
        tool.install(device=device,path="app-debug.apk")


