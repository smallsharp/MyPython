class Animal:
    """
    设置不同权限的属性和方法，测试在子类中能否继承这些资源
    注意：在python中，继承是指 使用权（读取）
    """
    a = 1
    _b = 2
    __c = 3  # 不能被继承

    def m1(self):
        print("m1")

    def _m2(self):
        print("_m2")

    def __m3(self):  # 不能被继承
        print("__m3")

    def __init__(self):
        print("init an Animal")


class Dog(Animal):

    def test(self):
        print(self.a)
        print(self._b)
        # print(self.__c) # AttributeError: 'Dog' object has no attribute '_Dog__c'

        self.m1()
        self._m2()
        # self.__m3()
        self.__init__()


d1 = Dog()
d1.test()
print(d1.__dict__)  # {}
d1.a = 8  # 注意：这里是给 d1 实例  新增一个a 属性，并非改变其父类的a属性。
print(d1.__dict__)  # {'a': 8}
