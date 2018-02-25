# coding=utf-8

score = 88

class A:
    num = 100
    # print(num) # num.pri

    def fun1(self):
        print("fun1，and num:", self.num, score)

    @classmethod
    def fun2(cls):
        print("fun2，and num:", cls.num)

    @staticmethod
    def fun3():
        print("fun3")


# print(A.num)

"""
实例方法(self)，类不可直接访问
"""
# A.fun1()
a = A()
a.fun1()
a.fun2()  # 类方法，实例对象也可访问
a.fun3()  # 静态方法，实例对象也可访问

"""
类方法（cls，classmethod修饰），可以访问类中变量,需要传递类指针（cls）
"""
# A.fun2()


"""
静态方法（staticmethod修饰），不能访问类中变量
"""
# A.fun3()
