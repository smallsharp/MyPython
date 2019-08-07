import pymongo

# 1. 连接mongo服务,返回client对象
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 2. use db
mydb = myclient["qa"]

# 3. use collection(table)
mycol = mydb["sites"]

# 4. 删除整个集合
mycol.drop()