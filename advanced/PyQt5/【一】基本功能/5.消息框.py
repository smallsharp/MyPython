#coding=utf-8

"""
ZetCode PyQt5 tutorial

This program shows a confirmation
message box when we click on the close
button of the application window.
默认情况下,如果我们单击x按钮窗口就关门了。有时我们想修改这个默认的行为。例如我们在编辑器中修改了一个文件,当关闭他的时候，我们显示一个消息框确认。

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()


    # 我们关闭窗口的时候,触发了QCloseEvent,重写closeEvent()事件处理程序
    def closeEvent(self, event):

        # 标题，文本，选项1|选项2
        reply = QMessageBox.question(self, 'Message',"Are you sure to quit?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Retry)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())