# coding=utf-8
from functools import wraps

# 1. 不带参数的装饰器
print('1. 不带参数的装饰器')
def my_log(func):
    def wrapper():
        print("开始记录日志")
        func()
        print("结束记录日志")
    return wrapper


@my_log
def my_func():
    print('it is the bussiness code')

my_func()

# 如何理解
# my_func == my_log(my_func)==wrapper
# my_func() == wrapper()

print('-' * 50)
print('2. 带参数的装饰器')


# 2. 带参数的装饰器
def my_log(func):
    def wrapper(a, b):
        print("开始记录日志")
        func(a, b)
        print("结束记录日志")
    return wrapper


@my_log
def my_func(a, b):
    c = a + b
    print('结果是：%s' % (c))

my_func(3, 4)


print('-' * 50)
print('3. 带任意参数,且 安全的装饰器')
def my_log(func):
    @wraps(func) # 这样不会丢失原来的__name__等属性
    def wrapper(*args, **kwargs):
        print("开始记录日志")
        func(*args, **kwargs)
        print("结束记录日志")
    return wrapper


@my_log
def my_func(a, b, c=9):
    print('a+b=%s' % (a + b))
    print('c=%s' % c)

my_func(2, 4)
my_func(2, 4, 100)
