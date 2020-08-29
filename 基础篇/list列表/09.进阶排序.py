mylist = [
    {
        "companyName": "上海雷凌信息科技有限公司",
        "total": 1.1
    },
    {
        "companyName": "上海载德物流有限公司",
        "total": 0.4
    },
    {
        "companyName": "上海云视科技股份有限公司",
        "total": 0.5
    },
    {
        "companyName": "北京百度网讯科技有限公司",
        "total": 1.2
    }
]


# 自定义排序,按照元素中的total值排序
def getKey(elem):
    return elem['total']  # 获取元素中的total值


# list.sort() 对原列表进行排序
mylist.sort(key=getKey, reverse=True)

# sorted() 生成一个新列表(不改变原列表)
newlist = sorted(mylist, key=getKey, reverse=True)
print(mylist)
print(newlist)

# 使用lambda
print(sorted(mylist, key=lambda x: x['total'], reverse=True))

lists = [
    {"id": 1001, "price": 100},
    {"id": 1001, "price": 120},
    {"id": 1002, "price": 25},
    {"id": 1003, "price": 55}
]

from operator import itemgetter
from itertools import groupby

# rows.sort(key=itemgetter('date'))

for id, items in groupby(lists, key=itemgetter('id')):
    print(id, sum([i['price'] for i in items]))
    # for i in items:
    #     print(' ', i)

from collections import defaultdict


rows_by_date = defaultdict(list)
for row in lists:
    rows_by_date[row['id']].append(row)

print(list(rows_by_date))
