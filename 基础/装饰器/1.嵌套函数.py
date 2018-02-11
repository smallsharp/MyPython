#coding=utf-8


print("嵌套函数 和 闭包 的使用")

"""
嵌套函数
嵌套函数，可以访问到其外层作用域声明的非局部变量（non-local）,如msg可以被printer正常访问
"""
def print_msg():
    msg = "hello python!"
    def printer():
        print(msg)
    printer()
print_msg()


"""
闭包
内部函数printer直接作为返回值  返回了

一般情况下，函数中的局部变量仅在函数的执行期间可用，一旦print_msg()调用过后，msg变量将不再可用
但是，发现调用p()时，msg变量值正常输出，这就是闭包的作用 
"""

def print_msg():
    msg = "hello python!"
    def printer():
        print(msg)
    return printer

p = print_msg()
p()

