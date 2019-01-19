# coding=utf-8

words = 'Life is short, you need Python'

words.lower()  # 'life is short, you need Python'
words.upper()  # 'LIFE IS SHORT, YOU NEED PYTHON'
words.count('i')  # 指定字符出现的次数,2

words.find('is')  # 从左向右查找'is'的下标, 5
words.rfind('need')  # 从右向左查找'need'的下标, 19

words.replace('you', 'I')  # 'Life is short, I need Python'

# 分隔符，默认按照 空格
nlist = words.split()  # ['Life', 'is', 'short,', 'you', 'need', 'Python']

"""
将列表 转为 字符串
join() 用指定分隔符按顺序把字符串列表组合成新字符串
tokens:['Life', 'is', 'short,', 'you', 'need', 'Python']
"""
nlist = ['Life', 'is', 'short,', 'you', 'need', 'Python']
new = " ".join(nlist)  # Life is short, you need Python

c = words + '\n'  # 加了换行符，注意+用法是字符串作为序列的用法
c.rstrip()  # 右侧去除换行符

tlist = [x for x in words]  # 遍历字符串中每个字符，生成新的列表

# 判断某个字符是存在
'Python' in words  # True
