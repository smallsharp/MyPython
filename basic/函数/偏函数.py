from functools import partial


def spam(a, b, c, d):
    print(a, b, c, d)


f1 = partial(spam, a=10, d=9)
f1(b=3, c=22)


def mod(n: int, m: int) -> int:
    print(n % m)


# 整数100对不同数m进行取余
mod_by_100 = partial(mod, 100)

mod_by_100(3)
mod_by_100(4)

# 整数99对不同数m进行取余，不用在写一个函数实现
mod_by_99 = partial(mod, 99)
mod_by_99(3)
mod_by_99(4)

# -----------------------------------------实战-----------------------------------------------------#

points = [(1, 2), (3, 4), (5, 6), (7, 8)]

import math


# 计算两点之间的距离
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


pt1 = (4, 3)
# 按距离点pt 最近的距离排序
points.sort(key=partial(distance, pt1))
print(points)

pt1 = (5, 5)
# 按距离点pt 最近的距离排序
points.sort(key=partial(distance, pt1))
print(points)
