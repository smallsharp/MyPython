# 在Python中创建一个闭包可以归结为以下三点：
#
# 闭包函数必须有内嵌函数
# 内嵌函数需要引用该嵌套函数上一级namespace中的变量
# 闭包函数必须返回内嵌函数

# https://blog.csdn.net/Liveor_Die/article/details/78953633


def test(number):
    # 在函数内部定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包
    def test_in(number_in):
        print("in test_in 函数, number_in is %d" % number_in)
        return number + number_in

    # 其实这里返回的就是闭包的结果
    return test_in


if __name__ == '__main__':
    # 给test函数赋值，这个20就是给参数number
    ret = test(20)

    # 注意这里的100其实给参数number_in
    print(ret(100))

    # 注意这里的200其实给参数number_in
    print(ret(200))
