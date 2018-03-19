# coding=utf-8
"""
@Time:2018-03-1913:26
@Author:lfl5207
"""
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget
import sys


class Winform(QMainWindow):  # 继承自 QMainWindow的所有属性和方法

    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("关闭主窗口的例子")

        self.button1 = QPushButton("关闭主窗口")
        self.button1.clicked.connect(self.onButtonClick)

        laylout = QHBoxLayout()
        laylout.addWidget(self.button1)

        main_frame = QWidget()
        main_frame.setLayout(laylout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self):
        sender = self.sender()  # sender是发送信号的对象
        print(sender.text() + "被按下了！")
        qApp = QApplication.instance()
        qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())
