# coding=utf-8
import pandas as pd

import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 设置控制台显示宽度
pd.set_option("display.width", 1000)

""" 读取csv文件 """
oo = pd.read_csv("olympics.csv", skiprows=4)


"""
1.分组 groupby
"""

edition = oo.groupby("Edition") # 通过年份分组
# print(type(edition)) # <class 'pandas.core.groupby.DataFrameGroupBy'>
# print(list(edition))
print(list(edition)[0])
print(type(list(edition)[0])) # <class 'tuple'>

# for k,v in list(edition)[0]:
#     print(k)
#     print(v)
"""
2.分组内容的遍历
"""
# for k,v in edition:
#     print(k)
#     print(v)
# 1896
# type(value)  DataFrame


"""
3.查看分组的大小
"""
# print(edition.size())
"""
Edition
1896     151
1900     512
1904     470
1908     804
1912     885
1920    1298
"""


