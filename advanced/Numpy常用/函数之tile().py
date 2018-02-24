# coding=utf-8

import numpy as np

a = np.array([0, 1, 2])
# a,type(a) # [0 0] <class 'numpy.ndarray'>


# print(np.tile(a, 2)) # [0 1 2 0 1 2]

print(np.tile(a, (2, 3))) # 行重复2次，列重复3次

