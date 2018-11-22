def add(x: int, y: int) -> int:
    return x + y


print(add(3, 5))

help(add)  # add(x:int, y:int) -> int


class Animal():
    def __init__(self, name):
        self.name = name

    def say(self):
        print('{} is saying'.format(self.name))
