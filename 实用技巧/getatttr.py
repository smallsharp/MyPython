class Person():

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("{} is eating".format(self.name))


p1 = Person("tom")

# 1. 获取属性
print(getattr(p1, "name"))
# print(getattr(p1, "age")) # AttributeError: 'Person' object has no attribute 'age'
print(getattr(p1, "age", 20))

# 2. 判断属性
print(hasattr(p1, "sex"))  # False

# 3. 设置属性
setattr(p1, "sex", "male")

print(hasattr(p1, "sex"))  # True

# 4. 删除属性
delattr(p1, "sex")

print(hasattr(p1, "sex"))  # False
