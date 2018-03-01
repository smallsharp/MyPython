# coding=utf-8


class Person:
    pass

"""
实例化类对象，并赋值
"""
p = Person()
p.name = "tim"
p.age = "22"

print(p.name, p.age, p.__dict__)  # tim 22 {'name': 'tim', 'age': '22'}

# 类对象  对应的 类
print(p.__class__) # <class '__main__.Person'>


"""
通过类名称，访问类属性
"""
class Person2:
    name = "people"
    age = "0-100"

print(Person2.name, Person2.age, Person2.__dict__)
p2 = Person2()

# 类实例对象可以访问 类属性==> 类实例对象优先查找自身的属性，找不到则找类的属性（通过 p2.__class__）
# 如果p2.__class__ 被更改，则会查找失败
print(p2.name, p2.age) # people 0-100


"""
修改 类属性
通过类访问后，可修改
"""
Person2.name = "person"

p2.name = "ppp" # 注意：此时并不是修改，而是新增类实例对象的属性，之前访问的是类属性。

print(Person2.name)

