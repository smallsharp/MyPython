#coding=utf-8
import random


l = [i for i in range(10)] # 生成一个列表
a = list(range(10)) # 生成一个列表

print(type(l),type(a))
random.shuffle(l) # 打乱顺序
print(l)

# 排序
b = sorted(l)
print(b)

# 排序
c = sorted(l,reverse=True)
print(l)
print(c)