class Config():
    MAX_WAIT_TIME = 10
    DEBUG = True

    def __init__(self):
        self.cname = 'MAIN_CONFIG'


# 传入一个类,返回类的所有属性
print(dir(Config))  # ['DEBUG', 'MAX_WAIT_TIME', '__class__', '__delattr__', '__dict__', '__dir__', ...]

# 传入一个对象，返回对象的所有属性，如例，多了一个cname
config = Config()
print(dir(config))

# 如果不传，默认当前模块
print(dir())  # ['Config', ... , 'config']

# 传入其他模块，如sys
import time

print(dir(time))
print(dir(list))


def main():
    rdict = {}
    for item in dir(Config):
        if item.isupper():
            value = getattr(Config, item)  # 通过反射，在类中获取对应属性的值
            rdict[item] = value

    print(rdict)


if __name__ == '__main__':
    main()
