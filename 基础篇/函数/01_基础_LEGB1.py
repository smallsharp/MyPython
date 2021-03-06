# Python 使⽤ LEGB 的顺序来查找⼀个符号对应的对象

# locals    ->   enclosing function    ->   globals    ->    builtins

# 局部变量———闭包空间———全局变量———内建模块


a = 10

b = 100


def func1():
    a = 20
    print('func1', a)  # 20(局部变量)
    print('id:', id(a))

    def func2():
        a = 30
        print('func2', a)  # 30（局部变量）
        print('id:', id(a))
        def func3():
            print('func3-->a:', a)  # 30 （闭包变量）
            print('func3-->b:', b)  # 100 （全局变量）

        func3()

    func2()
    print('a:', a)
    print('id:', id(a))

func1()
