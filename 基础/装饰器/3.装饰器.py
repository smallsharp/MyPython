# coding=utf-8

"""
1 函数作为参数 来使用
"""
def foo(num):
    return num + 1


def bar(fun):
    return fun(3)

value = bar(foo)
# print(value)


"""
嵌套函数
inner做为嵌套函数，它可以访问外部函数的变量，
调用 outer 函数时，发生了3件事：
第一：给 变量 x 赋值为1
第二：定义嵌套函数 inner，此时并不会执行 inner 中的代码，因为该函数还没被调用，直到第3步
第三：调用 inner 函数，执行 inner 中的代码逻辑。
"""
def outter():
    x = 1
    def inner():
        print(x)
    inner()

outter() # 1


"""
闭包
"""

def outer(func):
    def inner():
        print("记录日志开始")
        func() # 业务函数
        print("记录日志结束")
    return inner

@outer #语法糖  省略 foo = outer(foo)
def foo():
    print("it is a real deal")


foo()



