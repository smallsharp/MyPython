#coding=utf-8


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):

    """
    状态栏用于显示状态信息
    """

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # 用QMainWindow创建状态栏的小窗口
        self.statusBar().showMessage('Ready') # showMessage()状态栏上显示一条消息
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())