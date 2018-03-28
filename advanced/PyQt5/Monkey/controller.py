# coding=utf-8
"""
@Time:2018-03-2216:51
@Author:lfl5207
@Description: 逻辑设计
"""

from PyQt5.QtWidgets import *
from advanced.PyQt5.Monkey.ui import MonkeyUi
from advanced.PyQt5.Monkey import service
import sys


class MonkeyController(MonkeyUi):

    def __init__(self):
        super(MonkeyController, self).__init__()
        # 连接设备
        self.refresh_device()
        # 获取所有参数
        self.init_event_params()
        self.init_debug_params()
        # 开始
        self.btn_start.clicked.connect(self.run)
        # 结束
        self.btn_stop.clicked.connect(self.stop)

    def refresh_device(self):
        """
        刷新设备，耗时操作
        :return:
        """
        self.btn_refresh.clicked.connect(self.dowork) # 刷新按钮被点击时，执行

    def init_event_params(self):
        print("init_evnet_params")
        for index,tx in enumerate(self.tx_events):
            print(index,tx.text())

    def run(self):
        cmd = "adb -s {0} shell monkey -p {1}".format(self.device, self.tx_pkg)

    def init_debug_params(self):
        for ckb in self.ckb_debugs:
            ckb.stateChanged.connect(self.test)

    def test(self):
        """
        没有写完
        :return:
        """
        print("changed")
        self.ischecked = [False, False, False, False, False]
        print(self.ischecked)

    def stop(self):
        pass


    def dowork(self):
        self.thread = Thread()
        # 信号绑定到槽函数
        self.thread.update_text_singal.connect(self.set_device)
        self.thread.start()

    def set_device(self,text):
        """
        将获取到的设备，填充到下拉框中
        :return:
        """
        self.comb_devices.addItem(text)



from PyQt5.QtCore import *

class Thread(QThread):

    def __init__(self):
        super(Thread,self).__init__()

    update_text_singal = pyqtSignal(str)

    def run(self):
        print("run")
        devices = service.devices()
        # 通过信号将 数据发送出去
        self.update_text_singal.emit(devices[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MonkeyController()
    ex.show()
    sys.exit(app.exec_())