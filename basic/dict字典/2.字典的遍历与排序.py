# coding=utf-8

adict = {"tom": "22", "jack": "25", "fanny": "28", "amily": "18"}

"""
1. 字典的遍历方式1：只对键遍历
"""
for key in adict:
    # print(key,adict.get(key))
    print(key, adict[key])

"""
2. 字典的遍历方式2：遍历 键和值
"""
for key, value in adict.items():
    print(key, value)

"""
3. 单独遍历key 或者 value
"""
for key in adict.keys():
    print(key)

for value in adict.values():
    print(value)

"""
4.按照key的字符顺序遍历，先对dict进行排序sorted(adict)
"""

# 4.1 先对字典进行排序，然后遍历
for key in sorted(adict):
    print(key, adict.get(key))

# 4.2 按照字典的key排列
list1 = sorted(adict.items(), key=lambda x: x[0])  # ('jack', '25')
print(list1) # [('amily', '18'), ('fanny', '28'), ('jack', '25'), ('tom', '22')]

# 4.3 按照字典的value排列
list1 = sorted(adict.items(), key=lambda x: x[1])  # ('jack', '25')
# print(list1) # [('amily', '18'), ('tom', '22'), ('jack', '25'), ('fanny', '28')]
