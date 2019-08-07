import json

# 原始格式

users_str = """[{"user": "lk", "age": 22, "vip": true, "sex": null}, {"user": "张三丰", "age": 33, "vip": false}]"""

users = json.loads(users_str)
print(type(users))
print(users)
