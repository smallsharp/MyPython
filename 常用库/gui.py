

from tkinter import *
import os

def init_window():
    root = Tk()
    root.title("Tkinter")
    # 窗口大小
    width, height = 600, 600
    # 窗口居中显示
    root.geometry('%dx%d+%d+%d' % (width, height, (root.winfo_screenwidth() - width) / 2, (root.winfo_screenheight() - height) / 2))

    button1 = Button(root, text="Button1", command=insert_one)
    button1.pack()

    button2 = Button(root, text="Button2", command=insert_two)
    button2.pack()

    label = Label(root, text="label")
    label.pack()

    entry = Entry(master=root,text="请输入",show="*")
    entry.pack()

    t = Text(root, height=2)
    t.pack()

    checkbutton = Checkbutton(root, text="CheckButton")
    checkbutton.pack()

    radioButton = Radiobutton(root, text="RadioButton")
    radioButton.pack()

    root.mainloop()

def insert_one():
    var = entry.get()
    t.insert("a",var)

def insert_two():
    var = entry.get()
    t.insert("e",var)

def get_devices():
    res = os.system("adb devices")
    return res

def main():
    init_window()
    # get_devices()

if __name__ == '__main__':
    main()
