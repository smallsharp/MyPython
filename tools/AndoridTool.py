#coding=utf-8
"""
@Time:2018-03-1216:54
@Author:lfl5207
"""
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from tools.AndroidService import *
import sys

class MyWindow(QtWidgets.QWidget):

    _signal = QtCore.pyqtSignal("")

    def __init__(self):
        super(MyWindow,self).__init__()
        self.resize(500,300)
        self.init_child()
        self.init_ui()

    def init_ui(self):
        # 全局布局：垂直布局
        mainLayout = QtWidgets.QVBoxLayout()

        h1 = QtWidgets.QHBoxLayout()
        h1.addWidget(QtWidgets.QPushButton("xxxx"))
        h1.addWidget(QtWidgets.QPushButton("yyyy"))

        mainLayout.addLayout(h1)
        mainLayout.addWidget(self.form)

        # 设置 全局布局
        self.setLayout(mainLayout)

    def set_text(self):
        # LineEdit.setText("设备为是是是")
        self.text1.setText(check_state())

    def init_child(self):

        # self.form = QtWidgets.QGroupBox("Form layout")
        self.form = QtWidgets.QGroupBox() # 将控件包在一起
        layout = QtWidgets.QFormLayout()

        label1 = QtWidgets.QPushButton("检查设备")

        self.text1 = QtWidgets.QLineEdit()
        self.text1.setText(check_state())
        label1.clicked.connect(self.set_text)

        label2 = QtWidgets.QPushButton("当前应用")
        text2 = QtWidgets.QLineEdit()
        text2.setText(current_package())

        label3 = QtWidgets.QPushButton("Activiy")
        text3 = QtWidgets.QLineEdit()
        text3.setText(current_activity())

        label4 = QtWidgets.QPushButton("设备序列号")
        text4 = QtWidgets.QLineEdit()
        text4.setText(serial_no())

        layout.addRow(label1, self.text1)
        layout.addRow(label2, text2)
        layout.addRow(label3, text3)
        layout.addRow(label4, text4)

        self.form.setLayout(layout)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
