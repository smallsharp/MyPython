# coding=utf-8
# from tkinter import *
import tkinter as tk


class Monkey:

    def __init__(self):

        self.x1 = 1
        self.x2 = 65
        self.y1 = 1
        self.y2 = 30

        # 初始化界面
        self.window = tk.Tk()
        self.window.title("Monkey For Android")
        self.window.geometry("600x300")

        # 初始化设备,包名信息
        # self.init_v_base_params()
        self.init_v_event_percent()
        self.init_v_debug()

        # 初始化基本参数

        self.window.mainloop()

    def init_v_base_params(self):
        self.device = tk.Label(self.window, text='设备名称: ')  # 设备名称
        self.device.place(x=self.x1, y=self.y1)
        self.device_name = tk.Entry(self.window)
        self.device_name.place(x=self.x2, y=self.y1)
        print(self.device_name.get())

        self.package = tk.Label(self.window, text='应用包名: ')  # 应用包名
        self.package.place(x=self.x1, y=self.y2)
        package_name = tk.StringVar()
        package_name.set("com.tude.android")
        self.package_name = tk.Entry(self.window, textvariable=package_name)
        self.package_name.place(x=self.x2, y=self.y2)
        print(self.package_name.get())

    def init_v_event_percent(self):

        self.percent_name = ["touch", "motion", "trackball", "nav", "syskeys", "anyevent"]

        x1,y1 = 1,1
        y1 = 65

        for percent in self.percent_name:
            print(percent)
            # row = tk.Frame(self.window)
            lab = tk.Label(self.window, text=percent)
            lab.place(x=self.x1, y=self.y1)
            ent = tk.Entry(self.window)
            ent.place(x=self.x2, y=self.y1)
            # row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            # lab.pack(side=tk.LEFT)
            # ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            # self.y1 += 30
            self.y1+=30

    def init_v_debug(self):
        self.dug_items = ["ignore-crashes","ignore-timeouts","ignore-security","kill-process-after-error"]
        # 复选框
        chVarDis = tk.IntVar()
        # 用来获取复选框是否被勾选，通过chVarDis.get()来获取其的状态,其状态值为int类型 勾选为1  未勾选为0

        check1 = tk.Checkbutton(self.window, text="Disabled", variable=chVarDis,state='disabled')
        # text为该复选框后面显示的名称, variable将该复选框的状态赋值给一个变量，当state='disabled'时，该复选框为灰色，不能点的状态

        check1.select()  # 该复选框是否勾选,select为勾选, deselect为不勾选
        check1.grid(column=0, row=4,sticky=tk.W)
        # sticky=tk.W  当该列中其他行或该行中的其他列的某一个功能拉长这列的宽度或高度时，设定该值可以保证本行保持左对齐，N：北/上对齐  S：南/下对齐  W：西/左对齐  E：东/右对齐
        # for item in self.dug_items:


    def init_v_button(self):
        self.btn_start = ""
        self.btn_stop = ""
        pass

    def get_device_name(self):
        print(self.device_name.get())

    def get_device(self):
        res = os.popen("")
        pass

    def get_packages(self):
        pass

    def start_monkey(self):
        pass

    def stop_monkey(self):
        pass


monkey = Monkey()
