# coding=utf-8


"""
使用
isinstance(x,xx)
issubclass(x,xx) # 判断继承关系
"""

class Animal(object):

    def __init__(self, name, id):
        self.name = name

        self.id = id

    def func(self):
        print("name:{},age:{}".format(self.name, self.id))


# 继承Animal，不写构造方法，默认继承父类构造方法
class Person(Animal):
    pass

# 使用类名称 进行实例化
# Person("xi",19).func()

p1 = Person("xx", 1001)

print(isinstance(p1, object))
print(isinstance(p1, Animal))
print(isinstance(p1, Person))
print(Animal in Person.__bases__) # Person 的所有父类

print(issubclass(Person, Animal))  # 判断参数 class 是否是类型参数 classinfo 的子类。
print(issubclass(Person, object))  # 判断参数 class 是否是类型参数 classinfo 的子类。
