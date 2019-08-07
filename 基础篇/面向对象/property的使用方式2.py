class Person(object):

    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        print('get')
        return self.__age

    @age.setter
    def age(self, value):
        print("set")
        self.__age = value


p = Person()
print(p.age)
p.age = 20
print(p.age)
