# coding=utf-8

print("字典的基本用法")

"""
1. 字典的创建方式
"""
dict1 = {}  # 创建一个空字典
dict1 = {"name": "miao", "age": 20}  # 创建一个非空字典
dict2 = dict(name="miao", age=20)  # 通过dict函数 创建字典

stu = [("name", "miao"), ("age", 20)]
dict3 = dict(stu)  # 使用dict函数 可以将序列 转为 字典
# print(dict1,dict2,dict3)


"""
2.字典的修改 和 添加
"""
student = {"小萌": "1001", "小智": "1002", "小强": "1003"}

# 2.1 更新小强的学号
student["小强"] = 1005
# print(student) # {'小萌': '1001', '小智': '1002', '小强': 1005}

# 2.2 添加一个学生 姓名 小张，学号1006
student["小张"] = 1006
# print(student) # {'小萌': '1001', '小智': '1002', '小强': 1005, '小张': 1006}

print("kk %(小张)s"%student)

"""
3. 字典的删除操作
"""
student2 = {'小萌': '1001', '小智': '1002', '小强': 1005, '小张': 1006}

# 3.1 删除键值对(根据键 删除),原字典中键值会被删除
del student2["小张"]
print(student2) # {'小萌': '1001', '小智': '1002', '小强': 1005}

# 3.2 删除整个字典, 删除后就不可访问了
del student2
# print(student2) # NameError: name 'student2' is not defined

