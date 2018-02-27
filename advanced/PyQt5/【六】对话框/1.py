#coding=utf-8

"""
对话框窗口或对话框是现代GUI应用程序最不可或缺的一部分。
一个对话框被定义为两个或两个以上的人之间的谈话。
在计算机应用程序对话框窗口用于“交谈”应用程序。
一个对话框用于输入数据,修改数据,更改应用程序设置等。

QInputDialog
QInputDialog提供了一种简单方便的对话框从用户得到一个值。输入值可以是字符串,一个数字,或一个项目从一个列表
"""

"""
PyQt5 tutorial 

In this example, we determine the event sender
object.

author: py40.com
last edited: 2017年3月
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')

        if ok:
            self.le.setText(str(text))

"""
这个例子显示一个按钮和一个文本框，用户点击按钮显示一个输入框，用户输入信息会显示在文本框中。
第一个字符串是一个对话框标题,第二个是对话框中的消息。对话框返回输入的文本和一个布尔值。点击Ok按钮,布尔值是True。

"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())