class Person(object):  # 定义一个人类，继承objec
    def __init__(self):
        print("Person:我要好好学习")

    def study(self):
        print("Person ==>我要学习")


class Man(Person):  # 定义一个男人，继承人类
    def __init__(self):
        print("Man")

    def study(self):
        print("Man ==>我要学好数学")
        # super().study()


class Women(Person):  # 定义一个女人，继承人类
    def __init__(self):
        print("Wowen")

    def study(self):
        print("Wowen ==>我要学好英语")
        super().study()


class Son(Man, Women):  # 定义一个儿子，继承男人和女人
    def __init__(self):
        print("Son")

    def study(self):
        print("Son ==>我要学好化学和物理")
        # woman.study(self)
        # man.study(self)
        super().study()


# son1 = Son()
# son1.study()
# print(Son.mro())
# son1.study1()

# 结果是man类中的sutdy方法打印出来了然而woman和Person类中的study方法没有打印出来；相当与 son--man--woman中在man这里打断了，然后后面的也就不执行了。