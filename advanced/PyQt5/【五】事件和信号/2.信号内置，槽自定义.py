#coding=utf-8
"""
@Time:2018-03-0811:07
@Author:lfl5207
"""

from PyQt5.QtWidgets import *
import sys


class Test(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        btn = QPushButton('关闭', self)

        # 信号(btn.clicked)是内置的、槽(self.my_func)是自定义的
        btn.clicked.connect(self.my_func)

    def my_func(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Test()
    dlg.show()
    sys.exit(app.exec_())