# _*_ encoding:utf-8 _*_

# ------------------------继承-资源的覆盖-------------------------------------

# class D(object):
#     age = "d"
#     pass
#
# class C(D):
#     age = "c"
#     def test(self):
#         print("c")
#     pass
#
# class B(D):
#     age = "b"
#     def test(self):
#         print self
#         # print("b")
#     @classmethod
#     def test2(cls):
#         print cls
#     pass
#
# class A(B, C):
#     pass
#
# A.test2()
# a = A()
# a.test()


# print(A.mro())
#
# print(A.age)
# print(A().test())


# ------------------------------继承-资源的累加-------------------------------------



#
# class B:
#     a = 1
#     def __init__(self):
#         self.b = 2
#
#     def t1(self):
#         print("t1")
#
#     @classmethod
#     def t2(cls):
#         print("t2")
#
#     @staticmethod
#     def t3():
#         print("t3")
#
#
# class A(B):
#     c = 3
#     def __init__(self):
#         self.e = "666"
#
#     def tt1(self):
#         print("t1")
#
#     @classmethod
#     def tt2(cls):
#         print("t2")
#
#     @staticmethod
#     def tt3():
#         print("t3")
#
#     pass
#
#
# a_obj = A()
#
# print(A.a)
# print(a_obj.b)
#
#
# a_obj.t1()
# A.t2()
# A.t3()
#
# print(A.c)
#
# a_obj.tt1()
# A.tt2()
# A.tt3()
#
# a_obj.d = "xxx"
# print(a_obj.d)
#
# print(a_obj.e)

# ------------------------------继承-资源的累加-2-------------------------------------

# class B:
#     a = 1
#
#     def __init__(self):
#         self.b = 2
#         self.xxx = "123"
#
#     def t1(self):
#         print("t1")
#
#     @classmethod
#     def t2(cls):
#         print("t2")
#
#     @staticmethod
#     def t3():
#         print("t3")
#
#
# class A(B):
#     c = 3
#
#     def __init__(self):
#         # self a_obj
#         # self.init
#         # b = B()
#         # b.__init__()
#         B.__init__(self)
#         # self.b = 2
#         self.e = "666"
#
#     def tt1(self):
#         print("t1")
#
#     @classmethod
#     def tt2(cls):
#         print("t2")
#
#     @staticmethod
#     def tt3():
#         print("t3")
#
#     pass
#
# a = A()
# print(a.__dict__)

# ------------------------------继承-资源的累加-2-存在问题-------------------------------------
#
# class B:
#     a = 1
#
#     def __init__(self):
#         self.b = 2
#         self.xxx = "123"
#
#     def t1(self):
#         print("t1")
#
#     @classmethod
#     def t2(cls):
#         print("t2")
#
#     @staticmethod
#     def t3():
#         print("t3")
#
#
# class A(B):
#     c = 3
#
#     def __init__(self):
#         B.__init__(self)
#         self.e = "666"
#
#     def tt1(self):
#         print("t1")
#
#     @classmethod
#     def tt2(cls):
#         print("t2")
#
#     @staticmethod
#     def tt3():
#         print("t3")
#
#     pass
#
# a = A()
# print(a.__dict__)


# class D(object):
#     def __init__(self):
#         print("d")
#
# class B(D):
#     def __init__(self):
#         D.__init__(self)
#         print("b")
#
# class C(D):
#     def __init__(self):
#         D.__init__(self)
#         print("c")
#
# class A(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print("a")


# B()
# C()
# A()


# ------------------------------继承-资源的累加-super使用-------------------------------------

# class B:
#     a = 1
#
#     def __init__(self):
#         self.b = 2
#         self.xxx = "123"
#
#     def t1(self):
#         print("t1")
#
#     @classmethod
#     def t2(cls):
#         print(cls)
#         print("t2")
#
#     @staticmethod
#     def t3():
#         print("t3")
#
#
# class A(B):
#     c = 3
#
#     def __init__(self):
#         # super(A, self).__init__()
#         super().__init__()
#         self.e = "666"
#
#     def tt1(self):
#         print("t1")
#
#     @classmethod
#     def tt2(cls):
#         super(A, cls).t2()
#         print("t2")
#
#     @staticmethod
#     def tt3():
#         print("t3")
#
#     pass
#
# a = A()
# # print(a.__dict__)
#
# A.tt2()

# class D(object):
#     def __init__(self):
#         print("d")
#
# class B(D):
#     def __init__(self):
#         super().__init__()
#         print("b")
#
# class C(D):
#     def __init__(self):
#         super().__init__()
#         print("c")
#
# class A(B, C):
#     def __init__(self):
#         # B.__init__(self)
#         # C.__init__(self)
#         super().__init__()
#         print("a")

# ------------------------------继承-资源的累加-super使用注意事项-------------------------------------


# class D(object):
#     def __init__(self):
#         print("d")
#
# class B(D):
#     def __init__(self):
#         super(self.__class__, self).__init__()
#         # super(A, self).__init__()
#         print("b")
#
# # class C(D):
# #     def __init__(self):
# #         super().__init__()
# #         print("c")
# # #
# class A(B):
#     def __init__(self):
#         super(A, self).__init__()
#         print("a")
#
#
# A()


# class D(object):
#     def __init__(self):
#         print("d")
#
# class B(D):
#     def __init__(self):
#         # super().__init__()
#         super(B, self).__init__()
#         print("b")
#
# class C(D):
#     def __init__(self):
#         # super().__init__()
#         super(C, self).__init__()
#         print("c")
#
# class A(B, C):
#     def __init__(self):
#         # super().__init__()
#         B.__init__(self)
#         C.__init__(self)
#         print("a")
# A()
# print(A.mro())