# coding=utf-8

a = 'Life is short, you need Python'
a.lower()  # 'life is short, you need Python'
a.upper()  # 'LIFE IS SHORT, YOU NEED PYTHON'

a.count('i')  # 出现的次数,2

"""
查找字符串的下标
"""
a.find('e')  # 从左向右查找'e'的下标, 3
a.rfind('need')  # 从右向左查找'need'的下标, 19

a.replace('you', 'I')  # 'Life is short, I need Python'

tokens = a.split()  # ['Life', 'is', 'short,', 'you', 'need', 'Python']
print(tokens)

"""
将列表 转为 字符串
join() 用指定分隔符按顺序把字符串列表组合成新字符串
tokens:['Life', 'is', 'short,', 'you', 'need', 'Python']
"""
print("token:",tokens)
new = " ".join(tokens)  # Life is short, you need Python
print(new)

c = a + '\n'  # 加了换行符，注意+用法是字符串作为序列的用法
c.rstrip()  # 右侧去除换行符

[x for x in a]  # 遍历每个字符并生成由所有字符按顺序构成的列表
'Python' in a  # True
