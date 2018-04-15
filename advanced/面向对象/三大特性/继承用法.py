
class A:
    name = 'zhang'
    age = 22

    def p(self):
        print(self.name,self.age)

a = A()
a.p()


class B(A):
    pass

    def q(self):
        print(self.name,self.age)

b = B()
b.q()