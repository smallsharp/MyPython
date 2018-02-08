#coding=utf-8
'''
正则表达式的用法
@author: cm
'''
import re

modelpath = 'stag/model/upload/Pillow001_3D.zip?v1505444026044'
# match = re.search(r'(\S*/)?(\w+)', modelpath)

match = re.search(r'(\w*)/(\w*)/(\w*)/(\w*)', modelpath)
print(match.group(1))
print(match.group(2))
print(match.group(3))
print(match.group(4))

s1= modelpath.split(".")[0].split("/")[-1]
print(s1)

s2=modelpath.find(".")
print(s2)




