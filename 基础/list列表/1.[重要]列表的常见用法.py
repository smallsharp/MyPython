# encoding=utf-8
import copy

print("列表的用法")


"""
1、遍历列表的下标和索引
"""
# 普通版
items = [8, 23, 45]
for index in range(len(items)):
    print(index, "-->", items[index])

# 优雅版
for index,item in enumerate(items): # 音标：[ɪ'njuːməreɪt]
    print(index,"-->",item)

# enumerate 还可以指定元素的第一个元素从几开始，默认是0，也可以指定从1开始：
for index, item in enumerate(items, start=1):
    print(index, "-->", item)

"""
2、append 与 extend 方法有什么区别
append表示把某个数据当做新元素追加到列表的最后面，它的参数可以是任意对象
extend 的参数必须是一个可迭代对象，表示把该对象里面的所有元素逐个地追加到列表的后面
"""
x = [1, 2, 3]
y = [4, 5]
x.append(y) #[1, 2, 3, [4, 5]]
print(x)

x = [1, 2, 3]
y = [4, 5]
x.extend(y) # [1, 2, 3, 4, 5]
print(x)
"""
# 等价于：
for i in y:
    x.append(i)
"""

"""
3、检查列表是否为空
"""
# 普通版
if len(items) == 0:
    print("空列表")

if items == []:
    print("空列表")

# 优雅版
if not items:
    print("空列表")

"""
5、如何拷贝一个列表对象
"""
old_list = [2,4,6,8,10]
print(id(old_list))

#第一种方法：
newlist = old_list[:]
print(id((newlist)))

#第二种方法：
new_list2 = list(old_list)
print(id(new_list2))

#第三种方法：
new_list3 = copy.copy(old_list) #浅拷贝
print(id(new_list3))

new_list4 = copy.deepcopy(old_list) #深拷贝
print(id(new_list4))

"""
6、如何随机获取列表中的某个元素
"""
import random

print(random.choice(items))
print(random.choice(items))
print(random.choice(items))

"""
7、如何对列表进行排序
"""
items = [{'name': 'Homer', 'age': 39},
         {'name': 'Bart', 'age': 10},
         {"name": 'cater', 'age': 20}]

items.sort(key=lambda item: item.get("age")) #用于对原列表进行重新排序，指定 key 参数，key 是匿名函数，item 是列表中的字典元素，我们根据字典中的age进行排序，默认是按升序排列，
print(items)
items.sort(key=lambda item: item.get("age"), reverse=True) #指定 reverse=True 按降序排列
print(items)

#如果不希望改变原列表，而是生成一个新的有序列表对象，那么可以内置函数 sorted ，该函数返回新列表
new_items = sorted(items, key=lambda item: item.get("age"))
print(items,id(items))
print(new_items,id(new_items))

"""
8、如何移除列表中的元素
"""
a = [0, 2, 4, 7]
a.remove(2) #remove 移除某个元素值，而且只能移除第一次出现的元素,# 如果要移除的元素不在列表中，则抛出 ValueError 异常
print(a)

a = [3, 2, 2, 1]
del a[1] # 移除索引为1元素，当超出列表的下表索引时，抛出IndexError的异常
print(a)

