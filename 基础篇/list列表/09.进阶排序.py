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
