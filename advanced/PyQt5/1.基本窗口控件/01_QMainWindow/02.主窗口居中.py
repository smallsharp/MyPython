#coding=utf-8
"""
@Time:2018-03-1913:18
@Author:lfl5207
"""
from PyQt5.QtWidgets import QDesktopWidget,QApplication,QMainWindow
import sys


class Winform(QMainWindow): # 继承自 QMainWindow的所有属性和方法

    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("主窗口放在屏幕中间的例子")

        self.resize(370, 250) # 设置窗口的大小
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry() # 获得屏幕的大小
        size = self.geometry() # 获得窗口的大小

        # print(screen,size) # PyQt5.QtCore.QRect(0, 0, 1366, 768) PyQt5.QtCore.QRect(0, 0, 370, 250)

        # 将窗口移动到屏幕中间
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())