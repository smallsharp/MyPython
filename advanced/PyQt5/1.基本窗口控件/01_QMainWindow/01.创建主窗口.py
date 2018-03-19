# coding=utf-8
"""
@Time:2018-03-1913:10
@Author:lfl5207
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow): # 继承自 QMainWindow的所有属性和方法

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(400, 200)
        self.status = self.statusBar()
        self.status.showMessage("这是状态栏提示", 5000)
        self.setWindowTitle("PyQt MainWidow例子")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
