from tkinter import *


class GuiDemo:

    def say_hello(self):
        print("Hello")

    def __init__(self):
        root = Tk()
        root.title("Monkey")  # 窗口名称
        width, height = 400, 400
        root.geometry('%d x%d+%d+%d' % (
            width, height, (root.winfo_screenwidth() - width) / 2, (root.winfo_screenheight() - height) / 2))
        # root.resizable(width=True,height=True)

        # 绑定事件
        button = Button(master=root, text="click", bg="pink", width="8", height="2", command=self.say_hello)
        button.pack(side=LEFT)
        root.mainloop()


m = GuiDemo()
