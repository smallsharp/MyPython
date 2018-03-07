from PyQt5 import QtWidgets


"""
refer:http://www.cnblogs.com/hhh5460/p/5173645.html
本文的四个知识点：
1. 布局不能直接嵌套
2. 内层的布局必须先“附着”在一个空 QWidget 上
3. 然后把这个“承载”着内层布局的空部件添加至外层布局
4. 最后，别忘记把全局布局“附着”到窗体本尊
"""

class MyWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5布局示例')

        # 开始：
        wlayout = QtWidgets.QHBoxLayout()  # 全局布局（1个）：水平

        hlayout = QtWidgets.QHBoxLayout()  # 局部布局（4个）：水平、竖直、网格、表单
        vlayout = QtWidgets.QVBoxLayout()
        glayout = QtWidgets.QGridLayout()
        flayout = QtWidgets.QFormLayout()

        hlayout.addWidget(QtWidgets.QPushButton(str(1)))  # 局部布局添加部件（例如：按钮）
        hlayout.addWidget(QtWidgets.QPushButton(str(2)))

        vlayout.addWidget(QtWidgets.QPushButton(str(3)))
        vlayout.addWidget(QtWidgets.QPushButton(str(4)))

        glayout.addWidget(QtWidgets.QPushButton(str(5)), 0, 0)
        glayout.addWidget(QtWidgets.QPushButton(str(6)), 0, 1)
        glayout.addWidget(QtWidgets.QPushButton(str(7)), 1, 0)
        glayout.addWidget(QtWidgets.QPushButton(str(8)), 1, 1)

        flayout.addWidget(QtWidgets.QPushButton(str(9)))
        flayout.addWidget(QtWidgets.QPushButton(str(10)))
        flayout.addWidget(QtWidgets.QPushButton(str(11)))
        flayout.addWidget(QtWidgets.QPushButton(str(12)))

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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())