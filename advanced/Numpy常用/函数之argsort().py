#coding=utf-8

import numpy as np


x=np.array([1,4,3,-1,6,9])


# 将x中的元素从小到大排列，提取其对应的index(索引)
y = x.argsort()
print(y) # [3 0 2 1 4 5]