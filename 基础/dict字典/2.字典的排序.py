# coding=utf-8


adict = {"tom":"22","jack":"25","fanny":"28"}

for key in adict:
    print(key,adict.get(key))


"""
按照key的字符顺序遍历
需要先对dict进行排序sorted(adict)，然后遍历
"""
for key in sorted(adict):
    print(key,adict.get(key))




