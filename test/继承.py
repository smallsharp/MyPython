class Animal:
    def __init__(self):
        print("i am an animal!!!")

    def run(self):
        print("i am running")


class Dog(Animal):
    # def __init__(self):
    #     print("i am a dog")

    def eat(self):
        print("Dog is eatting!")

if __name__ == '__main__':
    d = Dog()
    d.run()
    d.eat()