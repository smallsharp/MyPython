
class Person(object):

    def __init__(self):
        # self.__age = 22
        pass
    # 使用  实例.属性 = 值，会调用如下方法
    def __setattr__(self, key, value):
        print("调用 __setattr__方法：",key,value)

        if key=="age" and key in self.__dict__.keys(): # 第一次赋值成功，再次失败
            print(key,"是只读属性")
            pass
        else:
            self.__dict__[key] = value

p = Person()
p.name = "yaos"
print(p.name)
print(p.__dict__)

p.age = 18
print(p.age)

p.age = 20 # age 是只读属性