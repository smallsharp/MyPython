adict = {"tom": "22", "jack": "25", "fanny": "28", "amy": "18"}

print(sorted(adict))  # 返回的是一个列表：['amy', 'fanny', 'jack', 'tom']

# 1 默认按字典的key进行排序,按照key的字符顺序遍历
for key in sorted(adict):
    print(key, adict.get(key))

# 2 按照字典的key排列
list1 = sorted(adict.items(), key=lambda x: x[0])  # ('jack', '25')
print(list1)  # [('amily', '18'), ('fanny', '28'), ('jack', '25'), ('tom', '22')]

# 3 按照字典的value排列
list2 = sorted(adict.items(), key=lambda x: x[1], reverse=True)  # ('jack', '25')
print(list2)  # [('amily', '18'), ('tom', '22'), ('jack', '25'), ('fanny', '28')]
