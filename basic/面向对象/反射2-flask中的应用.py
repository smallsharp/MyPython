# from basic.面向对象.setting import Config

'''
通过字符串 反射出类和 类属性方法
'''
import importlib

path = "basic.面向对象.setting.Config"
m, c = path.rsplit('.', maxsplit=1)
print(m, c)

m = importlib.import_module(m)
cls = getattr(m, c)
print(cls)

for item in dir(cls):
    if item.isupper():
        v = getattr(cls, item)
        print(item, v)
