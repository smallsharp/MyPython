#coding=utf-8
"""
find() 查找字符串中  指定字符串是否存在
找到：返回字符串的索引
找不到：返回 -1
"""
str = "Hello Python!"
str.find("Hello") # 0
print(str.find("P")) # 6
print(str.find("P",2)) # 从索引为2的位置开始找
print(str.find("P",7)) # 从索引为7的位置开始找
print(str.find("name"))  # -1




