# import requests,re
#
#
#
# res = requests.get('http://dema117.0898wj.com/a/qiyejianjie/')\
#
# # print(res.text)
#
# # list1 = re.findall(r'/.*/.*/(.*.jpg)', res.text)  # 匹配出所有的图片
# list1 = re.findall(r'/(.*.jpg)', res.text)  # 匹配出所有的图片
# print(res.text)
#
#
# print(list1)

class Person():
    def __init__(self):
        pass

def show():
    pass


print(Person.__name__)

print(show.__name__)

print(__name__)

from taidu import temp

print(temp.__name__)
