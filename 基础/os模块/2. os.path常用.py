#coding=utf-8


# 1.绝对路径
abspath1 = os.path.abspath("1.常用.py")
abspath2 = os.path.abspath("123")  # 不存在的文件也会正常返回 D:\workspace\PythonStation\Python学习\基础\os模块\123

# 2.判断是文件，还是文件夹
flag1 = os.path.isfile("test.py")  # True
flag2 = os.path.isdir(r"D:\workspace\PythonStation\Python学习\基础")  # True

# 3.判断给出的路径 是否存在
flag3 = os.path.exists("test.py")  # True
flag4 = os.path.exists("test2.py")  # Flase

# 4. 返回path中的文件夹或文件部分，结果不包含'\'; os.path.basename(path):
folder1 = os.path.dirname(r"D:\workspace\PythonStation\Python学习\基础\test.py")  # D:\workspace\PythonStation\Python学习\基础
folder2 = os.path.dirname(r"D:\workspace\PythonStation\Python学习")  # D:\workspace\PythonStation

# 5. 返回path中的文件夹或文件名称
file1 = os.path.basename(r"D:\workspace\PythonStation\Python学习\基础\test.py")  # test.py
file2 = os.path.basename(r"D:\workspace\PythonStation\Python学习")  # Python学习

# 6.
file3 = os.path.split(
    r"D:\workspace\PythonStation\Python学习\基础\test.py")  # 返回元组 ('D:\\workspace\\PythonStation\\Python学习\\基础', 'test.py')
file4 = os.path.split(
    r"D:\workspace\PythonStation\Python学习\基础")  # 返回元组 ('D:\\workspace\\PythonStation\\Python学习', '基础')

# 7. 获取文件大小
size1 = os.path.getsize(r"D:\workspace\PythonStation\Python学习\.project")
size2 = os.path.getsize(r"D:\workspace\PythonStation\Python学习\基础")

# 8.
print(os.path.dirname(__file__))
p = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../test/ADB.py"))  # 上层目录/上层目录
print(p)
