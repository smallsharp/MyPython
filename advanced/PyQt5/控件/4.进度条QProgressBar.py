#coding=utf-8


import sys

from PyQt5.QtWidgets import (QWidget, QProgressBar, QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):
    """
    显示一个水平的进度条和一个按钮，用户通过点击按钮开始和停止进度条
    """
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 设置窗口的位置 和 大小
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')

        # QProgressBar的构造方法
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 30, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(30, 80)
        self.btn.clicked.connect(self.doAction)

        # 我们使用定时器timer来激活QProgressBar
        self.timer = QBasicTimer()
        self.step = 0


        self.show()


    # 我们调用start()方法启动一个计时器。这个方法有两个参数:超时和对象将接收的事件。
    # 每个QObject及其子类都有一个timerEvent()事件处理器。我们要重新实现这个事件处理器来响应定时器事件
    def timerEvent(self, e):

        if self.step == 10:
            self.timer.stop()
            self.btn.setText("Error Occured")
            # return

        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)



    # 我们在doAction()方法中启动/停止定时器。
    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())