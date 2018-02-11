#coding=utf-8

import re


"""
.  匹配任意字符（除了换行符），当re.DOTALL标记被指定时，则可以匹配（包括换行符）任意字符
*  匹配0个或多个的表达式
+  匹配1个或多个的表达式
\d 匹配任意数字，等价于 [0-9]
\s 匹配任意空白字符，等价于 [\t\n\r\f].




"""

"""
例1：实现匹配出：ifyqyqni3775084
"""
url = "http://news.sina.com.cn/o/2018-01-27/doc-ifyqyqni3775084.shtml"
newurl = re.search("doc-i(.+).shtml",url)

print(newurl.group(0)) # 匹配到的整个字符串
print(newurl.group(1)) # 匹配到的括号中的字符串


"""
例2：实现匹配：6.0
"""

temp = "ro.build.version.release=6.0"
print(temp[25:]) # 普通方式

t = temp.split("=")[1] # s.split("")
print(t)

s = re.search(pattern="=(.*)",string=temp) # 使用re.search()
print(s.group(1))

s = re.findall(pattern="=(.*)",string=temp) # 使用re.findall()
print(s)