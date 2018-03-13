#coding=utf-8


"""
通过 __slots__ 限制 类实例对象可以使用的属性
"""
class Person:
    __slots__ = ["name","age"]

    pass

p1 = Person()

p1.name = "xiaoming"
p1.age = 20

p1.sex = "man" # 'Person' object has no attribute 'sex'