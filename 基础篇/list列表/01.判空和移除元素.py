# encoding=utf-8

# append 注意和 extend 区别
x = [1, 2, 3]
y = [4, 5]
x.append(y)  # [1, 2, 3, [4, 5]] # 追加的是 可迭代对象的整体

# extend
x = [1, 2, 3]
y = [4, 5]
x.extend(y)  # [1, 2, 3, 4, 5]  # 追加的是可迭代对象中的 元素

# 判断列表是否为空
items = []
# 普通版
if len(items) == 0:
    pass

if items == []:
    pass

# 优雅版
if not items:
    pass

# remove 移除某个元素值，而且只能移除第一次出现的元素,如果要移除的元素不在列表中，则抛出 ValueError 异常
a = [0, 2, 4, 7]
a.remove(2)  # [0, 4, 7]
print(a)

# 移除索引为1元素，当超出列表的下表索引时，抛出IndexError的异常
a = [3, 2, 2, 1]
del a[1]
print(a)  # [3, 2, 1]

# 移除列表中最后一个元素
a = [0, 2, 4, 7]
a.pop()
print(a)  # [0, 2, 4]

# a = []

a[1] = 1
print(a)
