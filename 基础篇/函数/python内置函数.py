# https://www.cnblogs.com/tina-python/p/5483924.html
# https://www.cnblogs.com/xiao1/p/5856890.html

# abs绝对值
# i = abs(-123)
# print(i)  #返回123，绝对值


# #all，循环参数，如果每个元素为真，那么all返回的为真，有一个为假返回的就是假的
# a = all((None,123,456,False))
# print(a)   #返回的为假的，证明中间有False值
#
# #所有的假值有
#     #0，None,空值
#

# #any  只要之前有一个是真的，返回的就是真
# b = any([11,False])
# print(b)


# ascii，去指定对象的类中找__repr__,获取返回值
# #ascii函数
# class Foo:
#     def __repr__(self):
#         return "tina"
# obj =Foo()
# r = ascii(obj)
# print(r)


# 布尔值返回真或假
# print(bool(1))
# print(bool(0))

# #bin二进制
# r = bin(123)
# print(r)

# #oct八进制
# r = oct(123)
# print(r)

# #int十进制
# r = int(123)
# print(r)

# #hex十六进制
# r = hex(123)
# print(r)

# #二进制转十进制
# i= int("0b11",base=2)
# print(i)

# #八进制转十进制
# i= int("11",base=8)
# print(i)

# #十六进制转十进制
# i = int("0xe",base=16)
# print(i)

#  bin oct int hex   二进制  八进制  十进制  十六进制
# bin() 可以将 八 十 十六 进制 转换成二进制
print(bin(10), bin(0o13), bin(0x14))
# oct() 可以将 二 十 十六 进制 转换为八进制
print(oct(10), oct(0b101), oct(0x14))
# int() 可以将 二 八 十六进制转换为十进制
print(int(0o13), int(0b101), int(0x14))
# hex() 可以将 二 八 十 进制转换为十六进制
print(hex(0b101), hex(110), hex(0o12))

# #数字代表字母
# c = chr(66)chr()输入数字，找到ascii码对应的字母
# print(c)

# #字母代表数字
# c = ord("a")
# print(c)
# bytes,  字节
# 字节和字符串的转换
# a = bytes("tina",encoding="utf-8")
# print(a)
# bytearray  字节列表
# chr(),把数字转换成字母,只适用于ascii码
# a = chr(65)
# print(a)

# ord(),把字母转换成数字，只适用于ascii码
# a = ord("a")
# print(a)

# callable表示一个对象是否可执行
# def f1():        #看这个函数能不能执行，能则返回True
#     return 123
# f1()
# r = callable(f1)
# print(r)
# dir,查看一个类里面存在的功能
# li = []
# print(dir(li))
# help(list)


# divmod() 分页的时候使用
a = 10 / 3
r = divmod(10, 3)
print('divmod:', r)


# compile编译, 把字符串转移成python可执行的代码，知道就行

# eval(),简单的表达式，可以给算出来
# b = eval("a + 69" , {"a":99})  #a可以通过字典声明变量去写入
# print(b)

# exec,不会返回值，直接输出结果
# exec("for i in range(10):print(i)")


# filter对于序列中的元素进行筛选，最终获取符合条件的序列（需要循环）
# def f1(x):
#     if x >22:
#         return  True
#     else:
#         return False
#
# ret = filter(f1,[11,22,33,44,55])
# for i in ret:
#     print(i)

# ret = filter(lambda x: x > 22, [11, 22, 33, 44, 55, 66, 77])
# for i in ret:
#     print(i)

# map(函数，可以迭代的对象，让元素统一操作)
# def f1(x):
#     return x+123
#
# # li = [11,22,33,44,55,66]
# # ret = map(f1,li)
# print(ret)
# for i in ret:
#     print(i)
#
# ret = map(lambda x: x + 100 if x%2==1 else x, [11, 22, 33, 44])
# print(ret)
# for i in ret:
#     print(i)

# globals()获取当前所有的全局变量

# locals（）获取当前所有的局部变量
# ret = "asziusdhf"
# def fu1():
#     name = 123
#     print(locals())
#     print(globals())
#
# fu1()


# hash 对key的优化，相当于给输出一种哈希值
# li = "sdglgmdgongoaerngonaeorgnienrg"
# print(hash(li))

# isinstance()判断是不是一个类型
# li = [11,22]
# ret = isinstance(li,list)
# print(ret)
############小案例#######################

def obj_len(a):
    if isinstance(a, str) or isinstance(a, list) or isinstance(a, tuple):
        if len(a) > 5:
            return True
        else:
            return False
    return None


t = [111, 22, 2, 2, ]
tt = obj_len(t)
print(tt)
# iter创建一个可以被迭代的元素
# obj = iter([11,22,33,44])
# print(obj)
# #next，取下一个值，一个变量里的值可以一直往下取，直到没有就报错
# ret = next(obj)

# max（）取最大的值
# li = [11,22,33,44]
# ret = max(li)
# print(ret)

# min()取最小值
# li = [11,22,33,44]
# ret = min(li)
# print(ret)

# 求一个数字的多少次方
# ret = pow(2,10)
# print(ret)

# reversed反转
# a = [11,22,33,44]
# b = reversed(a)
# for i in b:
#     print(i)

# round 四舍五入
# ret = round(4.8)
# print(ret)

# sum求和
# ret = sum((11,22,33,44))
# print(ret)

# zip，1 1对应
# li1 = [11,22,33,44,55]
# li2 = [99,88,77,66,89]
# dic = dict(zip(li1,li2))
# print(dic)


# sorted 排序
# li = ["1","2sdg;l","57","a","b","A","中国人"]
# lis = sorted(li)
# print(lis)
# for i in lis:
#     print(bytes(i,encoding="utf-8"))
######################小案例：############################
# #随机生成6位验证码
# import random
# temp = ''
# for i in range(6):
#     num = random.randrange(0,4)
#     if num ==3 or num ==1:
#         rad1 = random.randrange(0,10)
#         temp+=str(rad1)
#     else:
#         rad2 = random.randrange(65,91)
#         c1 = chr(rad2)
#         temp+=c1
# print(temp)
