import copy

list1 = [2, 4, 6, 8, 10]
print(id(list1))

# 第一种方法：
newlist = list1[:]
print(id((newlist)))

# 第二种方法：
list2 = list(list1)

list2[0] = 'hello'
print(id(list2))
print(list1, list2)

# 第三种方法：
list3 = copy.copy(list1)  # 浅拷贝
print("copy:", id(list3), id(list1))
list3[1] = 'world'
print(list1, list3)

list4 = copy.deepcopy(list1)  # 深拷贝
print("deepcopy:", id(list4), id(list1))

list5 = list1
list5[0] = 'hi'
print(list1, list5)
