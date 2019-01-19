"""
zip()可以按顺序同时输出两个列表对应位置的元素对,
zip()不会自动帮助判断两个列表是否长度一样，所以最终的结果会以短的列表为准
"""
b = [sum(x) for x in zip([1, 2, 3], [5, 6, 7])]  # [6, 8, 10]

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = list(zip(x, y, z))
print(xyz)  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

u = list(zip(*xyz))
print(u)  # [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# zip 结合 for 进行遍历的用法
list1 = [2, 3, 4]
list2 = [4, 5, 6]

for x, y in zip(list1, list2):
    print(x, y, '--', x * y)

# 优雅的写法，同上
list3 = [x * y for x, y in zip(list1, list2)]
print(list3)
