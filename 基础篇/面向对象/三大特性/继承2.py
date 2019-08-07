class Base(object):

    def func(self):
        super(Base, self).func()
        print('Base.func')

class Bar(object):
    def func(self):
        print('Bar.func')

class Foo(Base,Bar):
    pass

# 示例一
obj = Foo()
obj.func()
print(Foo.__mro__)

# 示例二
# obj = Base()
# obj.func()