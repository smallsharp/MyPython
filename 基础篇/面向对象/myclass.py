# coding=utf-8
count = 0

class MyClass:
    '''the description of MyClass'''

    def __init__(self):
        global count
        count += 1
        print("init count:{}".format(count))


a = MyClass()
a = MyClass()
a = MyClass()
a = MyClass()
b = MyClass()
