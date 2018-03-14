"""
简单的装饰器
"""


def check(func):
    def inner():
        print("check login status")
        func()

    return inner


# @check
def write():
    print("write sth")


write = check(write)
write()


print("--"*50)

"""
类装饰器
"""


class Check:

    def __init__(self, func):
        self.f = func

    def __call__(self, *args, **kwargs):
        print("check login status") # 额外的功能
        self.f()

@Check # 语法糖格式
def read():
    print("read something~")


read()

