# coding=utf-8
"""
@Time:2018-03-2216:51
@Author:lfl5207
"""
import sys
from PyQt5.QtWidgets import *


class Monkey(QWidget):
    def __init__(self):
        super(Monkey, self).__init__()
        self.initUi()

    def initUi(self):

        self.view_basic()
        # self.creatVboxGroupBox()
        self.view_event()
        self.view_buttons()

        mainLayout = QVBoxLayout()  # 第一步，定义全局布局（垂直布局）
        # mainLayout = QHBoxLayout()

        # 第二步，定义一个子布局
        hboxLayout = QHBoxLayout()
        # hboxLayout.addStretch()

        # 第三步，子布局中，添加控件集合
        hboxLayout.addWidget(self.gridGroupBox)
        hboxLayout.addWidget(self.btnGroupBox)
        # hboxLayout.addWidget(self.vboxGroupBox)

        # 第四步，将子布局，加入到全局布局
        mainLayout.addLayout(hboxLayout)  # 添加子布局，水平布局
        mainLayout.addWidget(self.formGroupBox)
        self.setLayout(mainLayout)

    def view_basic(self):
        self.gridGroupBox = QGroupBox("基础参数")
        formlayout = QFormLayout()
        formlayout.setSpacing(8)
        lb_devices = QLabel("选择设备")
        cb_devices = QComboBox()
        cb_devices.addItems(["xiaomi", "meizu", "huawei"])

        lb_pkg = QLabel("应用包名")
        tx_pkg = QComboBox()
        tx_pkg.addItems(["com.tude.android", "com.jd.mall"])

        lb_times = QLabel("执行次数")
        tx_times = QLineEdit()

        lb_interval = QLabel("事件间隔")
        tx_interval = QLineEdit()

        lb_seed = QLabel("种子数")
        tx_seed = QLineEdit()

        formlayout.addRow(lb_devices,cb_devices)
        formlayout.addRow(lb_pkg,tx_pkg)
        formlayout.addRow(lb_times,tx_times)
        formlayout.addRow(lb_interval,tx_interval)
        formlayout.addRow(lb_seed,tx_seed)

        self.gridGroupBox.setLayout(formlayout)
        self.setWindowTitle('Monkey')

    def creatVboxGroupBox(self):
        self.vboxGroupBox = QGroupBox("Vbox layout")
        layout = QVBoxLayout()

        nameLabel = QLabel("科研任务：")
        bigEditor = QTextEdit()
        bigEditor.setPlainText("搭载了空间冷原子钟等14项应用载荷，以及失重心血管研究等航天医学实验设备 "
                               "开展空间科学及技术试验.")
        layout.addWidget(nameLabel)
        layout.addWidget(bigEditor)
        self.vboxGroupBox.setLayout(layout)

    def view_event(self):
        self.formGroupBox = QGroupBox("事件配置")
        formlayout = QFormLayout()
        formlayout.setSpacing(8)
        lb_times = QLabel("Touch")
        tx_times = QLineEdit()

        lb_motion = QLabel("Motion")
        tx_motion = QLineEdit()

        lb_trackball = QLabel("Trackball")
        tx_trackball = QLineEdit()

        formlayout.addRow(lb_times,tx_times)
        formlayout.addRow(lb_motion,tx_motion)
        formlayout.addRow(lb_trackball,tx_trackball)

        self.formGroupBox.setLayout(formlayout)


    def view_buttons(self):
        self.btnGroupBox = QGroupBox("控制")
        layout = QVBoxLayout()
        # layout.addWidget(QPushButton("启动"))
        # layout.addWidget(QPushButton("停止"))
        layout.addWidget(QPushButton("开始"))
        layout.addWidget(QPushButton("停止"))

        self.btnGroupBox.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Monkey()
    ex.show()
    sys.exit(app.exec_())
