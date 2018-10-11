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

mylist = [
    {
        "companyName": "上海雷凌信息科技有限公司",
        "total": 1.1,
        "yearActDays": 8,
        "yearExpDays": 25
    },
    {
        "companyName": "上海载德物流有限公司",
        "total": 0.4,
        "yearActDays": 9,
        "yearExpDays": 29.000000000000004
    },
    {
        "companyName": "上海云视科技股份有限公司",
        "total": 0.5,
        "yearActDays": 162,
        "yearExpDays": 31
    },
    {
        "companyName": "北京百度网讯科技有限公司",
        "total": 1.2,
        "yearActDays": 30,
        "yearExpDays": 15
    }
]


# 自定义排序,按照元素中的total值排序
def getKey(elem):
    return elem['total']  # 获取元素中的total值

# list.sort() 对原列表进行排序
mylist.sort(key=getKey, reverse=True)

# sorted() 不改变元列表，生成一个新列表
newlist = sorted(mylist, key=getKey, reverse=True)
print(mylist)
print(newlist)


# 补充说明

items = [{'name': 'Homer', 'age': 39},
         {'name': 'Bart', 'age': 10},
         {"name": 'cater', 'age': 20}]
#用于对原列表进行重新排序，指定 key 参数，key 是匿名函数，item 是列表中的字典元素，我们根据字典中的age进行排序，默认是按升序排列，
items.sort(key=lambda item: item.get("age"))
print(items)

items.sort(key=lambda item: item.get("age"), reverse=True) #指定 reverse=True 按降序排列
print(items)

#如果不希望改变原列表，而是生成一个新的有序列表对象，那么可以内置函数 sorted ，该函数返回新列表
new_items = sorted(items, key=lambda item: item.get("age"))
print(items,id(items))
print(new_items,id(new_items))

