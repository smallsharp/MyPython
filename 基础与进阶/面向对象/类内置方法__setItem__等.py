
"""
通过 覆写三个方法，可以是 类实例通过 索引进行访问属性
"""
class Person:

    def __init__(self):
        self.cache = dict()

    def __getitem__(self, item):
        return self.cache[item]

    def __setitem__(self, key, value):
        self.cache[key] = value

    def __delitem__(self, key):
        del self.cache[key]


p = Person()

p["name"] = "lee"  # 调用　__setitem__
print(p["name"]) # 调用 __getitem__
print(p.cache)
del p["name"]
print(p.cache)  # {}
