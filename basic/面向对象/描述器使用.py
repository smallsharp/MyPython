class Age():

    def __get__(self, instance, owner):
        print("get", self, instance, owner)
        # return self.v
        return instance.v

    def __set__(self, instance, value):
        print("set", self, instance, value)
        # self.v = value
        instance.v = value

    def __delete__(self, instance):
        print("del", instance)


class Person:
    age = Age()


p1 = Person()
p2 = Person()

p1.age = 22
print(p1.age)

p2.age = 24
print(p1.age, p2.age)
