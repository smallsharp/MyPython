# 1.生成器
g = (i ** 2 for i in range(5))
print(g)  # <generator object <genexpr> at 0x0000024C0F81A2B0>

# 2.列表推导式
chars = [c for c in 'python']
print(chars)

# 3.字典推导式
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
double_dict1 = {k: v * 2 for (k, v) in dict1.items()}
print(double_dict1)

# 4.集合推导式
set1 = {1, 2, 3, 4}
double_set1 = {i * 2 for i in set1}
print(double_set1)

# 5.合并字典
x = {'a': 1, 'b': 2}
y = {'c': 3, 'd': 4, 'b': 5}
z = {**x, **y}
print('合并后的字典：', z)

# 6.反转列表
nums = [1, 2, 3]
reverse_nums = nums[::-1]
print(reverse_nums)

# 7.序列解包1
a, *b = 1, 2, 3  # a==1 ,b==[2,3]
a, *b, c = 1, 2, 3, 4, 5  # # a==1 ,b==[2,3,4], c==5


# 序列解包2
def f():
    return 1, 2, 3, 4


a, b, c, d = f()

# 8.in 代替 or
if x == 1 or x == 2 or x == 3:
    pass
if x in (1, 2, 3):
    pass


# 9.字典代替多个if else

def fun(x):
    if x == 'a':
        return 1
    elif x == 'b':
        return 2
    else:
        return None


def fun(x):
    return {"a": 1, "b": 2}.get(x)


# 10.需要遍历index，valuee
for i, e in enumerate(["a", "b", "c"]):
    print(i, e)
