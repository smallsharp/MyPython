# coding=utf-8
import numpy

"""
斐波那契数列（Fibonacci）
"""

print("第一种写法")
"""
递归是一种写法最简洁的方法，但它是效率非常低，因为会出现大量的重复计算，时间复杂度是：O(1.618 ^ n)，1.618 是黄金分割点。
同时受限于 Python 中递归的最大深度是 1000，所以用递归来求解并不是一种可取的办法。
"""


def fib_recur(n):
    assert n >= 0
    if n in (0, 1):
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)


for i in range(20):
    print(fib_recur(i), end=" ")


print(" ")
print("第二种写法")
"""
递推法就是从0和1开始，前两项相加逐个求出第3、第4个数，直到求出第n个数的值
这种算法的时间复杂是O(n)，呈线性增长，如果数据量巨大，速度越到后面会越慢。
"""


def fib_loop(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


for i in range(20):
    print(fib_loop(i), end=" ")


print(" ")
print("第三种写法")


def fib_matr(n):
    return (numpy.matrix([[1,1],[1,0]]))**(n-1)*numpy.matrix([[1],[0]])[0,0]

for i in range(20):
    print(int(fib_matr(i)),end=" ")
