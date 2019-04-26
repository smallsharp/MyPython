########## 安装 ##########

# pip install pymongo

from pymongo import MongoClient

# 连接到mongo服务
# client = MongoClient()
client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://192.168.40.32:27017/')

print(client.PORT, client.HOST, client.address)

## 选择数据库
db = client['zhihu']
# db = client.leili_admin
print(db)

c1 =db.qa
c1.insert({"name":"zhang"})