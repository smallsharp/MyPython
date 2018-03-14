"""
描述器的定义方式之一：
使用 property 关键字
"""


class Person(object):

    def __init__(self):
        self.__age = 18

    def get_age(self):
        print("get")
        return self.__age

    def set_age(self, value):
        print("set")
        self.__age = value

    def del_age(self):
        print("de1")
        del self.__age

    # 这里传递的是 方法名称
    age = property(get_age, set_age, del_age)


p1 = Person()
p1.age = 20
print(p1.age)
del p1.age
# print(help(Person))

print("-" * 50)


class Person2(object):

    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        print("get")
        return self.__age

    @age.setter # 注意方法名称 要和 属性名称对应
    def age(self, value):
        print("set")
        self.__age = value

    @age.deleter
    def age(self):
        print("del")
        del self.__age


p2 = Person2()
p2.age = 22
print(p2.age)
del p2.age
