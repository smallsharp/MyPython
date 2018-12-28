class Person(object):

    def __init__(self):
        # self.__age = 22
        pass

    # 使用  实例.属性 = 值，会调用如下方法
    def __setattr__(self, key, value):
        print("调用 __setattr__方法：", key, value)
        if key == "age" and key in self.__dict__.keys():  # 第一次赋值成功，再次失败
            print(key, "是只读属性")
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        print("调用 __getattr__方法：", item)


p = Person()
p.name = "redbull"
print(p.__dict__)  # {'name': 'redbull'}
#
p.age = 18
print(p.age)
#
# p.age = 20  # age 是只读属性
# print(p.age)
