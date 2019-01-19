# coding=utf-8
import os

# 1.得到当前工作目录，即当前Python脚本工作的目录路径。
currentpath = os.getcwd()  # D:\workspace\PythonStation\Python学习\基础\os模块

# 2.列举目录下的所有文件和文件夹名称，可指定目录(不深入遍历)
files = os.listdir()  # 当前目录 ['1.常用.py', '__init__.py']
files2 = os.listdir(r"D:\workspace\PythonStation\Python学习\基础")


# 3.操作系统名
system = os.name  # nt 如果是window 则用'nt'表示，对于Linux/Unix用户，它是'posix'

# 4.删除文件
# os.remove()


