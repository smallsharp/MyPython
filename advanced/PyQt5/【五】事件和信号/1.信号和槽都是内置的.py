# coding=utf-8
"""
@Time:2018-03-0811:00
@Author:lfl5207
"""

from PyQt5.QtWidgets import *
import sys


class Test(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        btn = QPushButton('关闭', self)

        # 信号(btn.clicked) ==> 槽(self.close)都是内置的
        # 按钮被点击，去关闭窗口
        btn.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Test()
    dlg.show()
    sys.exit(app.exec_())
