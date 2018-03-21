#coding=utf-8
"""
@Time:2018-03-2012:24
@Author:lfl5207
"""
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox
import sys

app = QApplication(sys.argv)
widget = QWidget()
widget.resize(200,50)



def showMsg():
    QMessageBox.information(widget, "信息提示框", "ok，弹出测试信息")


btn = QPushButton("测试点击按钮", widget)
btn.clicked.connect(showMsg)
widget.show()
sys.exit(app.exec_())