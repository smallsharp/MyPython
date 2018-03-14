#coding=utf-8
"""
@Time:2018-03-1416:37
@Author:lfl5207
"""


class Age():

    def __get__(self, instance, owner):
        print("get")

    def __set__(self, instance, value):
        print("set")


class Person:

    age = Age()

    def __init__(self,name):
        self.name = name


if __name__ == '__main__':
    p1 = Person("tom")

    print(p1.age)
    p1.age = 20
    print(p1.age)

    # print(p1.__dict__)







