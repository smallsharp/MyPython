class Person:
    country = 20
    __identity = 'spy'  # 私有化属性存储为：_Person__identity

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("{}正在吃饭".format(self.name))

    def __work(self):  # 私有化方法存储为：_Person__work
        print("{}正在窃听情报".format(self.name))


print(Person.__dict__)

# {'__module__': '__main__', 'country': 20, '_Person__identity': 'spy', '__init__': <function Person.__init__ at 0x000002AB74CC38C8>, 'eat': <function Person.eat at 0x000002AB7FD61510>, '_Person__work': <function Person.__work at 0x000002AB7FD61598>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}

tom = Person("tom")
tom.height = 180
print(tom.__dict__) # {'name': 'tom', 'height': 180}

print(Person.__dict__)

"""
类 的内置属性
"""
print(Person.__name__)  # 类的名称

print(Person.__dict__)  # 类的属性

print(Person.__bases__)  # 类的父类

print(Person.__module__)  # 类的模块名称

print(Person.__doc__)  # 类的描述

# print(Person.__identity)
print(Person.__dict__["_Person__identity"])
print(Person.__dict__["_Person__work"])
