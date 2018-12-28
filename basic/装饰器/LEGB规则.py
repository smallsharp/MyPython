# Python   使⽤    LEGB    的顺序来查找⼀个符号对应的对象
#
# locals    ->   enclosing    function    ->   globals    ->    builtins
#
# 局部变量———闭包空间———全局变量———内建模块


a = 10

b = 100


def func1():
    a = 20
    print('func1', a)  # 20

    def func2():
        a = 30
        print('func2', a)  # 30

        def func3():
            print('func3', a)  # 闭包空间
            print('func3', b)  # 全局变量

        func3()

    func2()


func1()
