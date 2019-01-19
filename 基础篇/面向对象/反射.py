class Person(object):

    def __init__(self):
        self.name = 'lucy'

    def sing(self):
        print('{} is sing'.format(self.name))
        return 'ok'


obj = Person()

# 获取成员
ret = getattr(obj, 'sing')  # 获取的是个对象
r = ret()
print(r)

# 检查成员
ret = hasattr(obj, 'sing')  # 因为有func方法所以返回True
print(ret)

# 设置成员
print(obj.name)  # 设置之前为:abc
ret = setattr(obj, 'name', 19)
print(obj.name)  # 设置之后为:19

# 删除成员
print(obj.name)  # abc
delattr(obj, 'name')

# print(obj.name)  # 报错
