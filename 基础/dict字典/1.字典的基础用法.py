#coding=utf-8

print("字典的基本用法")

"""
字典的初始化和集合很像，集合就像是 没有值只有键 的字典
"""

a = {'Tom': 8, 'Jerry': 7}
print(a['Tom'])             # 8

b = dict(Tom=8, Jerry=7)    # 一种字符串作为键更方便的初始化方式
print(b['Tom'])             # 8

if 'Jerry' in a:            # 判断'Jerry'是否在keys里面
    print(a['Jerry'])        # 7
print(a.get('Spike'))       # None，通过get获得值，即使键不存在也不会报异常

a['Spike'] = 10
a['Tyke'] = 3
a.update({'Tuffy': 2, 'Mammy': 42})

print(a.values())   # dict_values([8, 2, 3, 7, 10, 42])
print(a.pop('Mammy'))     # 移除'Mammy Two Shoes'的键值对，并返回42
print(a.keys())     # dict_keys(['Tom', 'Tuffy', 'Tyke', 'Jerry', 'Spike'