# coding=utf-8

import operator

"""
operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值。
"""

a = [1, 2, 3]

#  定义函数b，获取对象的第1个域的值
b = operator.itemgetter(1)
# print(b(a))

# 定义函数b，获取对象的第1个域和第0个的值
b = operator.itemgetter(1, 0)  # 定义函数b，获取对象的第1个域和第0个域的值
# print(b(a))


a = [("b", 2), ("a", 1), ("c", 0), ("d", 2), ("e", 3)]

# 使用元组的第一个元素 进行排序
b = sorted(a, key=operator.itemgetter(0))
print(b)

# 使用元组的第二个元素 进行排序
b = sorted(a, key=operator.itemgetter(1))
print(b)

# 多级排序: 先按元组的第二个元素进行排序，再对元组的第一个元素进行排序
b = sorted(a, key=operator.itemgetter(1, 0))
print(b)

# 使用 reverse 逆序
b = sorted(a, key=operator.itemgetter(0, 1), reverse=True)
print(b)
