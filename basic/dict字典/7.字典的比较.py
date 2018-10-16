# 比较两个字典的值
a = {"name": "likai", "age": 22, "height": 180}
b = {"height": 177, "sex": "male", "age": 22, "name": "zhangkai"}


def getSameKeys():
    # 找出两个字典中相同的key,字典的顺序可以不一致
    for k in a.keys() & b.keys():
        if a[k] != b[k]:
            print("except {}:{},but get:{}".format(k, a[k], b[k]))
        # print("key:{},value1:{},value2:{}".format(k,a[k],b[k]))

# find same key and same values
def getSameKeyVal():
    c = a.items() & b.items()
    print(c)

# find key in b but not in a
def getKeys():
    c = b.keys() - a.keys()
    print(c)

if __name__ == '__main__':
    # getSameKeyVal()
    getKeys()
