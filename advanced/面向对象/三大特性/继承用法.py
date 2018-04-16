
class A:
    name = 'zhang'
    age = 22

    def __init__(self):
        print('init an A')

    def p(self):
        print(self.name,self.age)

    @classmethod
    def c(cls):
        print('c',cls)

    @staticmethod
    def s():
        print('s')

# a = A() # a = A()
A.s()
A.c()



# class B(A):
#     pass
#
#     def q(self):
#         print(self.name,self.age)
#
# b = B()
# b.q()