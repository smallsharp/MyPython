class Test():

    def __len__(self):
        # return 0
        return 1

    def __bool__(self):
        return False


if __name__ == '__main__':
    test = Test()

    print(len(test))  # 根据Test类中 __len__,返回值决定

    print(bool(test))  # 根据Test类中 __bool__,返回值决定,如果未定义__bool__,则根据__len__决定

    print(bool(test))
