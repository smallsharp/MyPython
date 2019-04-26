class Person(object):

    # 使用  实例.属性 = 值，会调用如下方法
    def __setattr__(self, key, value):
        print("__setattr__：", key, value)
        if key == "age" and key in self.__dict__.keys():  # 第一次赋值成功，再次失败
            print(key, "是只读属性")
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        print("__getattr__：", item)


p = Person()
print(p.name)
p.name = "xiaoming"
print(p.name)
# print(p.__dict__)  # {'name': 'xiaoming'}

p.age = 18
print(p.age)
# #
p.age = 20  # age 是只读属性
print(p.age)
