# 需求：实际业务中，添加时间日志

import time


def f1():
    print('Tom adds two goods!')


def decorator(func):
    def wrapper():
        print(time.time())

    return wrapper
