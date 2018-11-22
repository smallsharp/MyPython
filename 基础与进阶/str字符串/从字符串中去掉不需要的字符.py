# coding=utf-8

# strip() 默认去掉左右空格
s = ' Hello World \n'
s.strip()  # 'Hello World'

# lstrip() 默认去掉左侧空格，可指定执行字符或字符串
s.lstrip()  # 'Hello World \n'

# rstrip() 默认去掉右侧空格，可指定执行字符或字符串
s.rstrip()  # ' Hello World'

# 实战演练
t = '=====Hello World-------'
t1 = t.lstrip('=')  # 'Hello World-------'
print(t1)
t2 = t.rstrip('-')  # '======Hello World'
print(t2)

# 去除中间多余的空格
x = ' Hello    World '

import re

x1 = re.sub(r'\s+', ' ', x.strip())  # 'Hello World'
print(x1)