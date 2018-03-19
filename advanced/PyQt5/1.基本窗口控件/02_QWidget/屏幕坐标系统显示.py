# coding=utf-8
"""
@Time:2018-03-1914:18
@Author:lfl5207
"""
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget
import sys

app = QApplication(sys.argv)
widget = QWidget()

# 1.设置窗体的宽度和高度 （width,height）,不同的操作系统对窗口的最小宽度有规定
widget.resize(300, 200)
# print(widget.size()) # PyQt5.QtCore.QSize(300, 200)
# print(widget.width()) # 300
# print(widget.height()) # 200

# 2.设置窗口的位置，以屏幕的左上角为（0，0）点
widget.move(100, 120)
widget.setWindowTitle("PyQt坐标系统例子")

btn = QPushButton(widget)
btn.setText("Button")

# 3.设置子控件的大小
# btn.resize(200,30)

# 4.设置子控件的位置，以QWidget左上角为（0，0）点
btn.move(30, 40)
widget.show()

print("QWidget:")
print("w.x():", widget.x()) # 获取窗口的x坐标
print("w.y():", widget.y()) # 获取窗口的y坐标
print("w.width():", widget.width()) # 获取窗口的宽度
print("w.height():", widget.height()) # 获取窗口的高度

print("QWidget.geometry:")
print("QWidget.geometry().x():", widget.geometry().x()) # 获取客户区的x坐标
print("QWidget.geometry().y():", widget.geometry().y()) # 获取客户区的y坐标
print("QWidget.geometry().width():", widget.geometry().width()) # 获取客户区的宽度
print("QWidget.geometry().height():", widget.geometry().height()) # 获取客户区的高度

sys.exit(app.exec_())
