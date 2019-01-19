# encoding=utf-8

import numpy as np

"""
ndim：维度
shape：行数和列数
size：元素个数
"""

array1 = np.array([[0, 1, 2], [4, 5, 6]])
# print(array1)
print(array1.ndim)  # 维度 2
print(array1.shape)  # 行数和列数 (2, 3)
print(array1.size)  # 元素个数 6
print(array1.dtype)

arr2 = np.arange(1, 10, 2)
print(arr2)

# 全0矩阵
arr3 = np.zeros(5)
print(arr3)

arr4 = np.zeros([2, 3])
print(arr4)

# 单位矩阵
arr5 = np.eye(5)
print(arr5)

# 一维数组切片

arr = np.arange(1, 10, 1)
print(arr)  # [1 2 3 4 5 6 7 8 9]
print(arr[1:5])  # [2 3 4 5]

# 二维数组切片
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6]])
print(arr[:2, 1:])  # 第一个参数：前两行，第二个参数：下标1的切到最后
# [[2 3 4]
#  [6 7 8]]
