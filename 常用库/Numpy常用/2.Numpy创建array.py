#encoding=utf-8
import numpy as np

"""
array：创建数组
dtype：指定数据类型
zeros：创建数据全为0
ones：创建数据全为1
empty：创建数据接近0
arrange：按指定范围创建数据
linspace：创建线段
"""

# (1) 创建数组
a = np.array([2,23,4])
print(a)
# [ 2 23  4]

# (2) 指定数据类型：dtype
a = np.array([2,23,4],dtype=np.int)
# print(a.dtype)
# int32

a = np.array([2,23,4],dtype=np.int32)
# print(a.dtype)
# int32

a = np.array([2,23,4],dtype=np.float)
# print(a.dtype)
# float64

a = np.array([2,23,4],dtype=np.float32)
# print(a.dtype)
# float32

# (3) 创建特定数据
a = np.array([[2,23,4],[2,32,4]]) # 2d 矩阵 2行3列
print(a)
# def zeros(shape, dtype=None, order='C')
# (3-1) 创建全零数组
a = np.zeros((3,4)) #数据全为0,3行4列
print("全0数组：",a)

# (3-2) 创建全一数组, 同时也能指定这些特定数据的 dtype:
a = np.ones((3,4),dtype = np.float)   # 数据为1，3行4列
print("全1数组：",a)

#(3-3)创建全空数组, 其实每个值都是接近于零的数:
a = np.empty((3,4))# 数据为empty，3行4列
print(type(a))

# (4) 用 arange 创建连续数组:
a  = np.arange(10,20,2) # 10-19 的数据，2步长(前包 后不包)
print(a)

# （5）使用 reshape 改变数据的形状
a = np.arange(12)
print("reshape前：",a)
a  = np.arange(12).reshape((3,4)) # 必须要保证可以正好重新拆分已有的array，如12/3=4，Returns an array containing the same data with a new shape.
print("reshape后：",a)

# （6）用 linspace 创建线段型数据:
a = np.linspace(1,10,10) # 开始端1，结束端10，且分割成20个数据，生成线段,Return evenly spaced numbers over a specified interval.
print(a)

# (6-1) linspace同样也能进行 reshape 工作:
a = np.linspace(1,10,10).reshape(5,2)
print(a)





