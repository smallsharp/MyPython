#coding=utf-8
"""
@Time:2018-03-1916:24
@Author:lfl5207
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton


class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("水平布局管理例子")
        self.resize(500, 50)

        # 水平布局按照从左到右的顺序进行添加按钮部件。
        hlayout = QHBoxLayout()
        # 添加伸缩
        hlayout.addStretch(0)

        hlayout.addWidget(QPushButton(str(1)))
        hlayout.addWidget(QPushButton(str(2)))
        hlayout.addWidget(QPushButton(str(3)))
        hlayout.addWidget(QPushButton(str(4)))
        # hlayout.addWidget(QPushButton(str(5)))
        # hlayout.addWidget(QPushButton(str(6)))
        # hlayout.addWidget(QPushButton(str(7)))
        # hlayout.addWidget(QPushButton(str(8)))
        # hlayout.addWidget(QPushButton(str(9)))
        # 添加伸缩
        # hlayout.addStretch(1)
        self.setLayout(hlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())
