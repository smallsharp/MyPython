
def fun1():
    x = 5
    def fun2():
        nonlocal x
        x *= 2
        return x
    return fun2


f1 = fun1()
print(f1())