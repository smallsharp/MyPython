class Person(object):
    def __init__(self):
        self.__age = 18

    def get_age(self):
        print("get")
        return self.__age

    def set_age(self, value):
        print("set")
        self.__age = value

    age = property(get_age, set_age)

p = Person()
print(p.age)
print(p.__dict__) # {'_Person__age': 18}

p.age = 20 # 修改属性值，调用set_agesssss
print(p.__dict__) # {'_Person__age': 20}
print(p.age)

