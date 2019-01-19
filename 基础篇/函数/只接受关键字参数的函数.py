# 只通过关键字的形式，接收特定的参数
def recv(maxsize, *, block):
    pass


# recv(333, True)
recv(333, block=True)  # YES


def minnum(*value, clip=None):
    m = min(value)
    if clip:
        m = clip if clip > m else m
    print(m)
    return m


minnum(10, 21, 33, 5, 8, clip=6)

help(minnum)
