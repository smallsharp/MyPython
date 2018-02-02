#coding=utf-8
'''
正则表达式的用法
@author: cm
'''
import re

# match()方法的工作方式是只有当被搜索字符串的开头匹配模式的时候它才能查找到匹配对象。
match = re.match(r'dog', 'dog cat dog')
print('匹配的字符：%s，匹配的开始位置：%s，匹配的结束位置：%s'%(match.group(0),match.start(),match.end()))

# search()方法不会限制我们只从字符串的开头查找匹配
match = re.search(r'cat', 'dog cat dog')
print(match.group(0))

# search()方法会在它查找到一个匹配项之后停止继续查找，因此在我们的示例字符串中用searc()方法查找‘dog’只找到其首次出现的位置。
match = re.search(r'dog', 'dog cat dog')
print(match.group(0))

# 调用findall()方法，得到一个所有匹配模式的列表，而不是得到match的对象
print(re.findall(r'dog', 'dog cat dog'))


# 使用 mathch.group 通过数字分组,通过其在正则表达式中从左到右出现的数字顺序来定位（从1开始）,因为第0个组被预留来存放所有匹配对象
contactInfo = 'Doe, John: 555-1212'
match = re.search(r'(\w+), (\w+): (\S+)', contactInfo)
print(match.group(1))
print(match.group(2))
print(match.group(3))

match1 = re.search(r'(?P<last>\w+), (?P<first>\w+): (?P<phone>\S+)', contactInfo)
# match1 = re.search(r'(?P<last>\w+),(?P<first>\w+):(?P<phone>\S+)', contactInfo)
print(match1.group('last'))
print(match1.group('first'))
print(match1.group('phone'))


listc = re.findall(r'(\w+), (\w+): (\S+)', contactInfo)
print(listc)

modelpath = 'stag/model/upload/Pillow001_3D.zip?v1505444026044'
# match = re.search(r'(\S*/)?(\w+)', modelpath)
match = re.search(r'(\w*)/(\w*)/(\w*)/(\w*)', modelpath)
print(match.group(1))
print(match.group(2))
print(match.group(3))
print(match.group(4))




