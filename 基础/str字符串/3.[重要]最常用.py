#coding=utf-8

"""
split():以xx分割
rstrip():去掉右边指定的字符串
lstrip():去掉左边指定的字符串
"""

url = "http://news.sina.com.cn/o/2018-01-27/doc-ifyqyqni3775084.shtml"

newurl = url.split(r"/")[-1] # 最后一个/
new1 = newurl.rstrip(".shtml")
new2 = new1.lstrip("doc-i")

print(newurl,new1,new2)
