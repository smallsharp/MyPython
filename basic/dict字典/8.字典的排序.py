adict = {"tom": "22", "jack": "25", "fanny": "28", "amy": "18"}

# 1 先对字典进行排序，然后遍历,按照key的字符顺序遍历，先对dict进行排序sorted(adict)
for key in sorted(adict):
    print(key, adict.get(key))

# 2 按照字典的key排列
list1 = sorted(adict.items(), key=lambda x: x[0])  # ('jack', '25')
print(list1)  # [('amily', '18'), ('fanny', '28'), ('jack', '25'), ('tom', '22')]

# 3 按照字典的value排列
list2 = sorted(adict.items(), key=lambda x: x[1], reverse=True)  # ('jack', '25')
print(list2)  # [('amily', '18'), ('tom', '22'), ('jack', '25'), ('fanny', '28')]
