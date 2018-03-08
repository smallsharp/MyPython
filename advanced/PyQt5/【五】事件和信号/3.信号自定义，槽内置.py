# coding=utf-8
"""
@Time:2018-03-0811:11
@Author:lfl5207
"""
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
import sys


class Test(QDialog):

    # 自定义信号，不带参
    button_clicked_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        btn = QPushButton('关闭', self)

        # 第一步 信号/槽  当按钮被点击的时，绑定一个方法
        btn.clicked.connect(self.btn_clicked)

        # 第三步 接收信号，连接到槽
        self.button_clicked_signal.connect(self.close)

    # 第二步 调用该方法，发送自定义信号
    def btn_clicked(self):
        self.button_clicked_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Test()
    dlg.show()
    sys.exit(app.exec_())
