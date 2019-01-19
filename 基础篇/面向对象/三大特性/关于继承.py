# coding=utf-8

class A:  # 类A继承自object类，这样才能使用super函数，因为这是python的“新式类”支持的特性
    def __init__(self):
        self.namea = "aaa"

    def funca(self):
        print("fun a : {}".format(self.namea))


class B(A):

    def __init__(self):
        # # 调用父类的未绑定的构造方法。在调用一个实例的方法时，该方法的self参数会被自动绑定到实例上（称为绑定方法）。
        # # 但如果直接调用类的方法（比如A.__init），那么就没有实例会被绑定。这样就可以自由的提供需要的self参数，这种方法称为未绑定unbound方法。
        # A.__init__(self)

        # 当前的类和对象可以作为super函数的参数使用，调用函数返回的对象的任何方法都是调用超类的方法，而不是当前类的方法。
        # super函数会返回一个super对象，这个对象负责进行方法解析，解析过程其会自动查找所有的父类以及父类的父类
        super(B, self).__init__()

        self.nameb = "bbb"

    def funcb(self):
        print("fun b : {}".format(self.nameb))


b = B()

print(b.nameb)
b.funcb()
b.funca()  # AttributeError: 'B' object has no attribute 'namea'
