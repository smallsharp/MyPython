class Config():
    MAX_WAIT_TIME = 10
    DEBUG = True

    def __init__(self):
        self.cname = 'MAIN_CONFIG'


def main():
    rdict = {}
    for item in dir(Config):
        if item.isupper():
            value = getattr(Config, item)  # 通过反射，在类中获取对应属性的值
            rdict[item] = value

    print(rdict)


if __name__ == '__main__':
    main()
