# coding=utf-8

adict = {"tom": "22", "jack": "25", "fanny": "28", "amy": "18"}

# 1. 字典的遍历方式1：只对键遍历
for key in adict:
    # print(key,adict.get(key))
    print(key, adict[key])

# 2. 字典的遍历方式2：遍历 键和值
for key, value in adict.items():
    print(key, value)

# 3. 单独遍历key
for key in adict.keys():
    print(key)

# 4. 单独遍历value
for value in adict.values():
    print(value)
