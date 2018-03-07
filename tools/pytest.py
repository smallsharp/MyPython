#coding=utf-8
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QHBoxLayout, QVBoxLayout,QLabel,QLineEdit,QTextEdit,QGridLayout
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon


class AndroidTool(QWidget):

    def __init__(self):
        super().__init__()
        self.result = self.__get_values__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5布局示例')

        # 开始：
        wlayout = QtWidgets.QVBoxLayout()  # 全局布局（1个）：垂直布局

        hlayout = QtWidgets.QHBoxLayout()  # 局部布局（4个）：水平、竖直、网格、表单
        vlayout = QtWidgets.QVBoxLayout()
        glayout = QtWidgets.QGridLayout()
        flayout = QtWidgets.QFormLayout()

        hlayout.addWidget(QtWidgets.QPushButton("检查设备"))
        hlayout.addWidget(QtWidgets.QLineEdit("已连接"))
        hlayout.addWidget(QtWidgets.QLabel("  "))

        hlayout.addWidget(QtWidgets.QPushButton("当前应用包名"))
        hlayout.addWidget(QtWidgets.QLineEdit(""))
        glayout.setSpacing(10)
        glayout.addWidget(QtWidgets.QLabel("序列号:"), 0, 0)
        glayout.addWidget(QtWidgets.QLabel(self.result.get("serial")), 0, 1)
        glayout.addWidget(QtWidgets.QLabel("系统版本:"), 1, 0)
        glayout.addWidget(QtWidgets.QLabel("6.0.1"), 1, 1)

        glayout.addWidget(QtWidgets.QLabel("品牌型号:"))
        glayout.addWidget(QtWidgets.QLabel("meizu_Mx5"))


        hwg = QtWidgets.QWidget()  # 准备四个部件
        vwg = QtWidgets.QWidget()
        gwg = QtWidgets.QWidget()
        fwg = QtWidgets.QWidget()

        hwg.setLayout(hlayout)  # 四个部件设置局部布局
        vwg.setLayout(vlayout)
        gwg.setLayout(glayout)
        fwg.setLayout(flayout)

        wlayout.addWidget(hwg)  # 四个部件加至全局布局
        wlayout.addWidget(vwg)
        wlayout.addWidget(gwg)
        wlayout.addWidget(fwg)

        self.setLayout(wlayout)  # 窗体本尊设置全局布局

        self.show()


    def __get_values__(self):
        # cmd = "adb devices"
        # import os
        # res = os.popen(cmd)
        # return  [i.split()[0] for i in res if 'devices' not in i and len(i) > 5]
        # return "meizu"
        result = {}
        result["serial"] = "mx5"
        result["model"] = "meizu"
        result["version"] = "6.0.1"

        return result


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ui = AndroidTool()
    sys.exit(app.exec_())