# coding=utf-8

class MyClass:
    num = 100
    print("00000")  # 只会执行一次

    def func_nomal(self):
        print("this is nomal func，and num:", self.num)

    @classmethod
    def func_cls(cls):
        print("this is class func，and num:", cls.num)

    @staticmethod
    def func_static():
        print("this is static func and num：", MyClass.num)


"""实例方法(self)，类不可直接访问"""
# MyClass.func_nomal()   TypeError: func_nomal() missing 1 required positional argument: 'self'

a = MyClass()
a.func_nomal()

"""类方法（cls，classmethod修饰），可以访问类中变量,需要传递类指针（cls）"""
MyClass.func_cls()

"""静态方法（staticmethod修饰），不能访问类中变量"""
MyClass.func_static()

'''注意'''
a.func_cls()  # 类方法，实例对象也可访问
a.func_static()  # 静态方法，实例对象也可访问

b = MyClass()
b.func_nomal()

print(MyClass.__dict__)
