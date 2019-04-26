import pymongo

# 1. 连接mongo服务,返回client对象
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 2. use db
mydb = myclient["qa"]

# 3. use collection(table)
mycol = mydb["sites"]

mylist = [
    {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
    {"_id": 2, "name": "Google", "address": "Google 搜索"},
    {"_id": 3, "name": "Facebook", "address": "脸书"},
    {"_id": 4, "name": "Taobao", "address": "淘宝"},
    {"_id": 5, "name": "Zhihu", "address": "知乎"}
]
# 4. insert data
x = mycol.insert_many(mylist)

# 输出插入的所有文档对应的 _id 值
print(x.inserted_ids)
