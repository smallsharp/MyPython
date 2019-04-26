# coding=utf-8

student1 = {'小智': '1002', "info": ["man", "20", "177"]}

"""
1.get(key,default=None)方法
通过key，查找value，没有找到指定key时，默认返回None,可以设置default值
"""

print(student1.get("小智"))
print(student1.get("小张"))  # None
# print(student1.get("小张",default="lll")) # 错误写法
print(student1.get("小张", "l000"))  # 正确写法 l000

"""
2. 判断字典中是否含有 指定key
"""
flag1 = "小智" in student1
flag2 = "小张" in student1
# print(flag1, flag2)  # True False


"""
3. items() 返回可遍历的 （k,v）元组 数组
"""
# print(student1.items()) # dict_items([('小智', '1002'), ('info', ['man', '20', '177'])])


"""
4. keys() 返回字典的所有键 数组
"""

print(student1.keys())  # dict_keys(['小智', 'info'])

"""
5. values() 返回字典中的所有值 列表 （包含重复的元素）
"""
# print(student1.values()) # dict_values(['1002', ['man', '20', '177']])


"""
6. setdefault(key,default=None) 方法
当 key 存在时，返回key对应的值
当 key 不存在时，返回默认值None，并更新字典
设置默认值时，如果key存在则不更新，不存在则使用设置的值
"""
v1 = student1.setdefault("小张")  # None
v2 = student1.setdefault("小智")  # 1002
v2 = student1.setdefault("小美", "1005")  # 1005
# print(student1,v1,v2)


"""
7. undate()方法 ： dict1.update(dict2),将dict2 更新到 dict1中
如果有相同的键，则值会覆盖
"""
st1 = {"1001": "晓晓", "1002": "美美"}
st2 = {"1003": "喵喵"}
st3 = {"1003": "苗苗"}
st1.update(st2)
st1.update(st3)
print(st1)  # {'1001': '晓晓', '1002': '美美', '1003': '苗苗'}

"""
8. fromkeys()方法 返回一个新的字典
传入参数可以是 字符串，列表，元素，字典
"""

# 8.1 传入列表
seq = ["name", "age", "sex"]
st4 = dict.fromkeys(seq)
print(st4)  # {'name': None, 'age': None, 'sex': None}

# 设置默认值
st4 = dict.fromkeys(seq, 10)
print(st4)  # {'name': 10, 'age': 10, 'sex': 10}

# 8.2 传入字符串
seq2 = "hello"
st4 = dict.fromkeys(seq2)
print(st4)  # {'h': None, 'e': None, 'l': None, 'o': None}

# 8.3 传入字典
seq3 = {1: 'one', 2: 'two'}
st4 = dict.fromkeys(seq3)
print(st4)  # {1: None, 2: None}
