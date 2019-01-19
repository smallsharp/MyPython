s = "string in global"
num = 99


def numFunc(a, b):
    num = 100
    print("numFunc的s: ", s)

    def addFunc(a, b):
        s = "string in addFunc"
        print("addFunc的 s: ", s)
        print("addFunc的num: ", num)
        print("addFunc的locals : ", locals())
        print()
        return "%d + %d = %d" % (a, b, a + b)

    print("numFunc的locals: ", locals())
    print()
    return addFunc(a, b)


tup = numFunc(3, 6)
print(tup)
print("全局: ", globals())
