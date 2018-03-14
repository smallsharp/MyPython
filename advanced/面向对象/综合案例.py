# class Caculator:
#
#     def __init__(self, num):
#         if not isinstance(num,int):
#             raise TypeError("不是整形数据")
#         self.__result = num
#
#     def jia(self, n):
#         self.__result += n
#
#     def jian(self, n):
#         self.__result -= n
#
#     def cheng(self, n):
#         self.__result *= n
#
#     def chu(self, n):
#         self.__result /= n
#
#     def show(self):
#         print("result:", self.__result)
#
# c1 = Caculator(0)
# c1.jia(5)
# c1.cheng(2)
# c1.jian(3)
# c1.show()

# ------------------------------------------------------代码2----------------------------------------------------------------------------

class Caculator:

    def __check_num(func):
        def inner(self,num):
            if not isinstance(num, int):
                raise TypeError("输入的数据不是整形数据")
            return func(self, num)
        return inner

    def __init__(self, num):
        self.__result = num

    @__check_num
    def jia(self, n):
        self.__result += n

    @__check_num
    def jian(self, n):
        self.__result -= n

    @__check_num
    def cheng(self, n):
        self.__result *= n

    @__check_num
    def chu(self, n):
        self.__result /= n

    def show(self):
        print("result:", self.__result)


c1 = Caculator(0)
c1.jia("2")
# c1.cheng(2)
# c1.jian(3)
c1.show()
