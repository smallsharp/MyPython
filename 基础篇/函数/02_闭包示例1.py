# coding=utf-8
# 在Python中创建一个闭包前提【重要】：

# 闭包函数必须有内嵌函数
# 内嵌函数需要引用该嵌套函数上一级namespace中的变量
# 闭包函数必须返回内嵌函数

# 闭包函数的实例, 闭包 = 函数 + 环境变量（x,y都是环境变量,外部函数的变量）
def outer(x):
    y = 10

    def inner():
    	nonlocal y
        # print(f"{x},{y}")  # 在内函数中 用到了外函数的临时变量
        # return x + y
        y = y+x
        return y

    return inner


out = outer(5)  # 外函数结束的时候,发现内部函数用到自己的临时变量，那么这两个临时变量就不会释放，会绑定到这个内部函数
# print(out.__closure__[0].cell_contents, out.__closure__[1].cell_contents)
out()  # 15
print(out())

