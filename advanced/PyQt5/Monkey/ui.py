# coding=utf-8
"""
@Time:2018-03-2216:51
@Author:lfl5207
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QValidator


class Monkey(QWidget):
    def __init__(self):
        super(Monkey, self).__init__()
        self.initUi()

    def initUi(self):
        # 第一步，定义全局布局（垂直布局）
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)  # 设置整体窗口布局
        self.setWindowIcon(QIcon('../icon.jpg'))

        self.setWindowTitle('Monkey')
        self.basicGroupBox = QGroupBox("基础参数")
        self.eventGroupBox = QGroupBox("事件配置")
        self.btnGroupBox = QGroupBox("执行")
        self.init_basic_view()
        self.init_event_view()
        self.init_btn_view()
        self.init_debug_view()

        # 第二步，定义一个子布局,并添加包含的控件
        hlayout_a = QHBoxLayout()
        hlayout_a.addWidget(self.basicGroupBox)
        hlayout_a.addWidget(self.btnGroupBox)

        hlayout_b = QHBoxLayout()
        hlayout_b.addWidget(self.eventGroupBox)
        hlayout_b.addWidget(self.debugGroupBox)

        # 第三步，将子布局 和 子控件添加到全局布局中
        mainLayout.addLayout(hlayout_a)
        mainLayout.addLayout(hlayout_b)

    def init_basic_view(self):
        # self.basicGroupBox = QGroupBox("基础参数")
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

        formlayout.addRow(lb_devices, cb_devices)
        formlayout.addRow(lb_pkg, tx_pkg)
        formlayout.addRow(lb_times, tx_times)
        formlayout.addRow(lb_interval, tx_interval)
        formlayout.addRow(lb_seed, tx_seed)

        self.basicGroupBox.setLayout(formlayout)

    def init_event_view(self):
        formlayout = QFormLayout()
        formlayout.setSpacing(8)
        events = ["触摸事件", "滑动事件", "轨迹球事件", "导航事件", "主导航事件", "系统按键事件", "页面切换事件"]
        self.percent = [40, 20, 10, 10, 5, 5, 10]

        # 批量初始化元素
        self.event_group = []
        for (event, p) in zip(events, self.percent):
            text = QLineEdit(str(p))
            formlayout.addRow(QLabel(event), text)
            print(text.text())
            self.event_group.append(int(text.text()))
        self.eventGroupBox.setLayout(formlayout)

    def init_btn_view(self):
        layout = QVBoxLayout()
        self.btn_start = QPushButton("开始")
        self.btn_start.clicked.connect(self.calc_sum)
        # self.btn.clicked.connect(self.changeBtnText)

        btn_stop = QPushButton("停止")
        layout.addWidget(self.btn_start)
        layout.addWidget(btn_stop)
        self.btnGroupBox.setLayout(layout)

    def init_debug_view(self):
        self.debugGroupBox = QGroupBox("调试选项")
        vlayout = QVBoxLayout()
        vlayout.setSpacing(8)
        vlayout.addWidget(QCheckBox("默认启动页面"))
        vlayout.addWidget(QCheckBox("忽略程序崩溃"))
        vlayout.addWidget(QCheckBox("忽略程序无响应"))
        vlayout.addWidget(QCheckBox("忽略证书"))
        vlayout.addWidget(QCheckBox("忽略超时"))
        vlayout.addWidget(QCheckBox("出错直接杀掉进程"))
        vlayout.addStretch(1)
        self.debugGroupBox.setLayout(vlayout)

    def calc_sum(self):
        print("click")
        print(sum(self.event_group))

        if sum(self.event_group) > 100:
            if sum(self.percent) > 100 or sum(self.percent) < 0:
                QMessageBox.information(self,
                                        "消息框标题",
                                        "这是一条消息。",
                                        QMessageBox.Yes | QMessageBox.No)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Monkey()
    ex.show()
    sys.exit(app.exec_())
