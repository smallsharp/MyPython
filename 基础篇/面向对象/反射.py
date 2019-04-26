class Person(object):

    def __init__(self, name):
        self.name = name

    def sing(self):
        print('{} is sing'.format(self.name))
        return 'ok'


obj = Person('lucy')

#### 一. 获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。

# 1. 获取对象中的属性【存在】
ret = getattr(obj, 'name')

# 2. 获取对象中的属性【不存在】-异常
# ret = getattr(obj, 'sex') # AttributeError: 'Person' object has no attribute 'sex'

# 3. 获取对象中的属性【不存在】-指定默认值
ret = getattr(obj, 'sex', 'male')
print(ret)

# 4. 如果获取的是个方法，则返回的是内存地址,如果需要运行这个方法，可以在后面添加括号。
ret = getattr(obj, 'sing')
print(ret)  # <bound method Person.sing of <__main__.Person object at 0x000001E2366C18D0>>  # 如需调用 ret()

#### 二.判断一个对象里面是否有xxx属性或xxx方法，有返回True，否则返回False。
ret = hasattr(obj, 'sing')  # True
ret = hasattr(obj, 'age')  # False

#### 三.给对象的属性赋值，若属性不存在，先创建再赋值。
print(obj.name)  # 设置之前为:abc
ret = setattr(obj, 'name', 'lili')
print(obj.name)  # 设置之后为:lili

#### 四.删除对应的xxx属性,删除后不可访问
print(obj.name)  # abc
delattr(obj, 'name')

# print(obj.name)  # 报错


#### 五. 综合运用（判断是否有某个属性【hasattr】，没有则赋一个属性【setattr】，最后获取该属性【getattr】）

feifei = Person('feifei')

print(hasattr(feifei, 'name'))

if not hasattr(feifei, 'age'):
    setattr(feifei, 'age', 22)

print(getattr(feifei, 'age'))
