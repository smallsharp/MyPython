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
        self.init_params()
        self.init_debug_params()
        # 开始
        self.btn_start.clicked.connect(self.run)
        # 结束
        self.btn_stop.clicked.connect(self.stop)

    def refresh_device(self):
        self.btn_refresh.clicked.connect(self.set_device)

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

    def set_device(self):
        """
        将获取到的设备，填充到下拉框中
        :return:
        """
        print("click")
        self.comb_devices.clear()
        # self.cb_devices.addItem(service.devices)
        self.comb_devices.addItem("meizu")
        print("currentText:", self.comb_devices.currentText())

    def init_params(self):
        for tx in self.tx_events:
            tx.textChanged.connect(self.sum)

    def sum(self):
        tx_list = []
        for tx in self.tx_events:
            tx_list.append(int(tx.text()))
        if sum(tx_list) > 100:
            tx_list = []
        else:
            print(tx_list)
            return tx_list


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MonkeyController()
    ex.show()
    sys.exit(app.exec_())
