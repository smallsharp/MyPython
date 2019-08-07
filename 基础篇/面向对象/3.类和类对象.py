# coding=utf-8

# 1. 实例化类对象，并赋值
class Person:

    def __init__(self, name):
        self.name = name


tom = Person("tom")
pgg = Person("nick")

tom.age = "22"
print(tom.name, tom.age, tom.__dict__)  # tim 22 {'name': 'tim', 'age': '22'}
#
# # 2. 类实例  对应的 类
# print(p.__class__) # <class '__main__.Person'>


# 3. 通过类名称，访问类属性
class Person2:
    name = "smith"
    age = "22"


print(Person2.name, Person2.age, Person2.__dict__)
p2 = Person2()

# 4. 类实例可以访问 类属性
# 类实例是优先查找自身的属性，如果找不到，则查找类的属性（通过 p2.__class__）
# 如果p2.__class__ 被更改，则会查找失败
print(p2.name, p2.age)  # people 0-100

# 5. 修改 类属性,通过类访问后，可修改
Person2.name = "person"
p2.name = "ppp"  # 注意：此时并不是修改，而是新增类实例对象的属性，之前访问的是类属性。
print(Person2.name)
