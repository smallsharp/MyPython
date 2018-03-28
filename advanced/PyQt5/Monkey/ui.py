# coding=utf-8
"""
@Time:2018-03-2216:51
@Author:lfl5207
@Description: UI界面设计
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QIntValidator

class MonkeyUi(QWidget):
    def __init__(self):
        super(MonkeyUi, self).__init__()
        self.initUi()

    def initUi(self):
        # 第一步，定义全局布局（垂直布局）
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)  # 设置整体窗口布局
        self.setWindowIcon(QIcon('../icon.jpg'))
        self.setWindowTitle('Monkey')

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
        self.basicGroupBox = QGroupBox("基础参数")
        formlayout = QFormLayout()
        formlayout.setSpacing(8)
        self.basicGroupBox.setLayout(formlayout)

        self.btn_refresh = QPushButton("刷新设备")
        self.comb_devices = QComboBox()
        self.device = self.comb_devices.currentText()
        self.tx_pkg = QLineEdit()
        self.tx_times = QLineEdit()
        self.tx_interval = QLineEdit()
        self.tx_seed = QLineEdit()
        labels = [self.btn_refresh, "应用包名", "执行次数", "事件间隔", "种子数"]
        txs = [self.comb_devices, self.tx_pkg, self.tx_times, self.tx_interval, self.tx_seed]

        for (x, y) in zip(labels, txs):
            formlayout.addRow(x, y)

    def init_event_view(self):
        self.eventGroupBox = QGroupBox("事件配置")
        formlayout = QFormLayout()
        formlayout.setSpacing(8)
        events = ["触摸事件", "滑动事件", "轨迹球事件", "导航事件", "主导航事件", "系统按键事件", "页面切换事件"]
        self.percent = [40, 20, 10, 10, 5, 5, 10]

        # 批量初始化元素
        self.tx_events = []
        for (event, p) in zip(events, self.percent):
            tx_event = QLineEdit(str(p))
            pInt = QIntValidator(self)  # 设置只允许输入数字
            pInt.setRange(0, 100)
            tx_event.setValidator(pInt)
            formlayout.addRow(QLabel(event), tx_event)
            self.tx_events.append(tx_event)
            # tx_event.text()


        self.eventGroupBox.setLayout(formlayout)

    def init_btn_view(self):
        self.btnGroupBox = QGroupBox("执行")
        layout = QVBoxLayout()
        self.btn_start = QPushButton("开始")
        self.btn_stop = QPushButton("停止")
        layout.addWidget(self.btn_start)
        layout.addWidget(self.btn_stop)
        self.btnGroupBox.setLayout(layout)

    def init_debug_view(self):
        self.debugGroupBox = QGroupBox("调试选项")
        vlayout = QVBoxLayout()
        vlayout.setSpacing(8)
        cb_tx = ["默认启动页面", "忽略程序崩溃", "忽略程序无响应", "忽略证书", "忽略超时", "出错直接杀掉进程"]
        self.ckb_debugs = []
        for tx in cb_tx:
            ckb = QCheckBox(tx)
            vlayout.addWidget(ckb)
            self.ckb_debugs.append(ckb)

        vlayout.addStretch(1)
        self.debugGroupBox.setLayout(vlayout)
