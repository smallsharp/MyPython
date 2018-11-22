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
        "yearExpDays": 29.04
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

# 使用lambda的方式进行排序
# 用于对原列表进行重新排序，指定 key 参数，key 是匿名函数，item 是列表中的字典元素，我们根据字典中的age进行排序，默认是按升序排列，
mylist.sort(key=lambda item: item.get("total"))
print(mylist)

mylist.sort(key=lambda item: item.get("total"), reverse=True)  # 指定 reverse=True 按降序排列
print(mylist)

# 如果不希望改变原列表，而是生成一个新的有序列表对象，那么可以内置函数 sorted ，该函数返回新列表
new_items = sorted(mylist, key=lambda item: item.get("total"))
print(new_items, id(new_items))

# 使用itemgetter() 进行排序，性能更好
from operator import itemgetter

newlist = sorted(mylist, key=itemgetter('total'))
newlist = sorted(mylist, key=itemgetter('total', 'yearActDays'))  # 也可以接受多个键

print(newlist)
