# 在Python中创建一个闭包可以归结为以下三点：

# 闭包函数必须有内嵌函数
# 内嵌函数需要引用该嵌套函数上一级namespace中的变量
# 闭包函数必须返回内嵌函数

# https://blog.csdn.net/Liveor_Die/article/details/78953633


def outer(x):
    # 在函数内部定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包
    def inner(y):
        print('y:', y)
        return x + y

    # 其实这里返回的就是闭包的结果
    return inner


if __name__ == '__main__':
    # x
    ret = outer(20)

    # y
    print(ret(100))

    # y
    print(ret(200))
