# coding=utf-8

a = [5, 7, 6, 3, 4, 1, 2]

"""
sorted(iterable[, cmp[, key[, reverse]]])
返回重新排序的列表对象
"""
b = sorted(a)  # 保留原列表
# print(a)  # [5, 7, 6, 3, 4, 1, 2]
# print(b)  # [1, 2, 3, 4, 5, 6, 7]

list1 = [('b', 3), ('a', 4), ('c', 2), ('d', 1)]

"""
利用key值 遍历，默认升序
"""
list2 = sorted(list1, key=lambda x: x[0])
print(list2)  # [('a', 4), ('b', 3), ('c', 2), ('d', 1)]

list2 = sorted(list1, key=lambda x: x[1])
print(list2)  # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]


"""
对字典进行排序
"""
dict1 = {"dJim": 30, "aSmith": 22, "bTom": 20, "cJack": 25}
s = sorted(dict1.items(), key=lambda x: x)
print(s, dict(s))

"""
按照降序排列
"""
s = sorted(dict1.items(), key=lambda x: x, reverse=True)
print(s, dict(s))

