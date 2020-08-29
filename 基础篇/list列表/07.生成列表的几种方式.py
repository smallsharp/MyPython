# coding=utf-8

print("第一种：列表生成式")
alist = [i for i in "python"]
print(alist)

print("第二种：list关键字")
blist = list("python")
print(blist)

print("第三种：分割")
str = "i love python"
clist = str.split()
print(clist)

mdate = "2018-02-10"
dlist = mdate.split("-")
print(dlist)

print("第四种：列表自身切片")
s = ["zhangsan", "wangwu", "lisi"]
flist = s[:]
print(flist)
