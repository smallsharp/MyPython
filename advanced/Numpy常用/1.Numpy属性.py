# encoding=utf-8

import numpy as np

"""
ndim：维度
shape：行数和列数
size：元素个数
"""

array = np.array([[1,2,3],[4,5,6]])
print(array)
print(array.ndim) # 维度 2
print(array.shape) # 行数和列数 (2, 3)
print(array.size)  # 元素个数 6