#coding=utf-8
"""
@Time:2018-03-2118:13
@Author:lfl5207
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys


class Winform(QWidget):

    # 第一步：自定义信号
    button_clicked_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('自定义信号和内置槽函数示例')
        self.resize(330, 50)
        btn = QPushButton('关闭', self)

        # 第二步：按钮被点击时，发送信号
        btn.clicked.connect(self.btn_clicked)

        # 第三步：信号链接到槽函数
        self.button_clicked_signal.connect(self.close)

    def btn_clicked(self):
        # 发送自定义信号，无参数
        self.button_clicked_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())
