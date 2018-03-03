#coding=utf-8


import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        cb1 = QCheckBox('复选框的内容', self)
        cb2 = QCheckBox('测试选中状态', self)
        cb1.move(20, 20)
        cb2.move(20, 40)

        cb1.toggle()
        cb2.toggle()

        cb1.stateChanged.connect(self.changeTitle)

        cb2.stateChanged.connect(self.printOk)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')

    def printOk(self,state):
        if state == Qt.Checked:
            print("选中")
        else:
            print("未选中")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())