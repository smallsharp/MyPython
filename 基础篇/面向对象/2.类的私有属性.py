class Person:
    __age = 20  # 私有化属性存储为：_Person__age

    _name = 'lk'  # _name

    def __eat(self):  # 私有化方法存储为：_Person__eat
        print("eat")


# print(Person.__dict__)
# {'__module__': '__main__', '_Person__age': 20, '_name': 'lk', '_Person__eat': <function Person.__eat at 0x000002256DC33730>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}

p = Person()
print(p.__dict__)  # _{}

"""
类 的内置属性
"""
print(Person.__name__)  # 类的名称

print(Person.__dict__)  # 类的属性

print(Person.__bases__)  # 类的父类

print(Person.__module__)  # 类的模块名称

print(Person.__doc__)  # 类的描述
