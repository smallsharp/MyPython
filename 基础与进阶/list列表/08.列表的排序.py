# coding=utf-8
import random

list1 = [i for i in range(10)]  # 生成一个列表

list2 = list(range(10))  # 生成一个列表

print('原始列表：', list1, list2)

random.shuffle(list1)  # 打乱顺序
random.shuffle(list2)  # 打乱顺序
print('打乱后的：', list1, list2)

# 默认排序
b = sorted(list1)
print('默认排序：', b)

# 排序倒序
c = sorted(list1, reverse=True)
print('默认倒序：', c)