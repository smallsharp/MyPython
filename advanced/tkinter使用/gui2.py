import tkinter as tk
import os

window = tk.Tk()
window.title("my window")
window.geometry("500x300")

# 创建输入框entry，用户输入任何内容都显示为*
# e = tk.Entry(window, show='*')
# e.pack()

# 创建一个文本框用于显示
t = tk.Text(window, width=15, height=2)
t.pack()

# 定义触发事件时的函数（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
def insert_point():
    t.insert('insert', "Hello")

def insert_end():
    t.insert('end', get_device())

def get_device():
    res = os.popen("adb devices")
    return res.read()

# 窗口内容（窗口上的控件）
b1 = tk.Button(window, text="insert1", width=15, height=2, command=insert_point)
b1.pack()

b2 = tk.Button(window, text="insert2", width=15, height=2,command=insert_end)
b2.pack()
window.mainloop()
window.quit()



