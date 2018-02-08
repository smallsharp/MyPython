# coding=utf-8
import os

# 1.得到当前工作目录，即当前Python脚本工作的目录路径。
currentpath = os.getcwd()  # D:\workspace\PythonStation\Python学习\基础\os模块

# 2.列举目录下的所有文件和文件夹名称，可指定目录(不深入遍历)
files = os.listdir()  # 当前目录 ['1.常用.py', '__init__.py']
files2 = os.listdir(r"D:\workspace\PythonStation\Python学习\基础")

# 3.绝对路径
abspath1 = os.path.abspath("1.常用.py")
abspath2 = os.path.abspath("123")  # 不存在的文件也会正常返回 D:\workspace\PythonStation\Python学习\基础\os模块\123

# 4.操作系统名
system = os.name  # nt 如果是window 则用'nt'表示，对于Linux/Unix用户，它是'posix'

# 5.删除文件
# os.remove()


# 6.判断是文件，还是文件夹
flag1 = os.path.isfile("test.py")  # True
flag2 = os.path.isdir(r"D:\workspace\PythonStation\Python学习\基础")  # True

# 7.判断给出的路径 是否存在
flag3 = os.path.exists("test.py")  # True
flag4 = os.path.exists("test2.py")  # Flase

# 8. os.path.dirname(path):返回path中的文件夹或文件部分，结果不包含'\'; os.path.basename(path):返回path中的文件夹或文件名称
folder1 = os.path.dirname(r"D:\workspace\PythonStation\Python学习\基础\test.py")  # D:\workspace\PythonStation\Python学习\基础
folder2 = os.path.dirname(r"D:\workspace\PythonStation\Python学习")  # D:\workspace\PythonStation

file1 = os.path.basename(r"D:\workspace\PythonStation\Python学习\基础\test.py")  # test.py
file2 = os.path.basename(r"D:\workspace\PythonStation\Python学习")  # Python学习

file3 = os.path.split(
    r"D:\workspace\PythonStation\Python学习\基础\test.py")  # 返回元组 ('D:\\workspace\\PythonStation\\Python学习\\基础', 'test.py')
file4 = os.path.split(
    r"D:\workspace\PythonStation\Python学习\基础")  # 返回元组 ('D:\\workspace\\PythonStation\\Python学习', '基础')

# 9. 获取文件大小
size1 = os.path.getsize(r"D:\workspace\PythonStation\Python学习\.project")
size2 = os.path.getsize(r"D:\workspace\PythonStation\Python学习\基础")

# 10.
print(os.path.dirname(__file__))
p = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../test/ADB.py"))  # 上层目录/上层目录
print(p)
