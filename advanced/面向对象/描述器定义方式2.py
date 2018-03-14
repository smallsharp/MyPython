# coding=utf-8
"""
@Time:2018-03-1416:37
@Author:lfl5207
@Description:描述器只能在新式类中生效

1. 一个实例的访问顺序：
0.是否实现了描述器的__get__方法
1.实例自身的__dict__
2.实例对应类的__dict__
3.查找父类的__dict__
4.如果没找到，又定义了 __getattr__,则调用这个方法

2.资料描述器和 非资料描述器

资料描述器：实现了__get__,__set__
非资料描述器：只实现了__get__
资料描述器 > 实例属性 > 非资料描述器

"""


class Age():

    def __get__(self, instance, owner):
        print("get")

    def __set__(self, instance, value):
        print("set")

    def __delete__(self, instance):
        print("del")


class Person:
    age = Age()


"""
主要通过 类实例对象 进行访问
"""
p1 = Person()
p1.age
p1.age = 20
print(p1.__dict__)  # {}
del p1.age
