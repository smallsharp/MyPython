"""
重写 __str__方法，相当于ava中的 toString 方法
格式化输出类实例字符串
"""

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "这个人姓名是：{}，年龄是：{}".format(self.name, self.age)


    # def __repr__(self):
    #     return "repr"


p1 = Person(name="张三", age=20)
print(p1)

p2 = Person("李四", 22)
print(p2)

p3 = Person("王五", 24)

s = str(p3)  # 这种方式 也会调用__str__方法
print(s)


print(repr(p1)) # repr ,如果覆写,则显示 <__main__.Person object at 0x0000018A40E886A0>
