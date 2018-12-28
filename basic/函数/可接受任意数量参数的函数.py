# 接受任意数量的位置参数，可以使用 * 开头
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


avg1 = avg(3, 5, 2, 6)
print(avg1)


# 接受任意数量的关键字参数

def make_dict(**kwargs):
    print(kwargs)


make_dict(name='li', age='22', addr="ShangHai")


# 接受任意参数的函数
def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)


anyargs(3, 'H', False, 0.22, [2], city='ShangHai', country='China')
