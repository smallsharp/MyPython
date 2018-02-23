# coding=utf-8
import pandas as pd

"""
读取csv文件
"""
oo = pd.read_csv("olympics.csv", skiprows=4)

# print(type(oo.index))  # <class 'pandas.core.indexes.range.RangeIndex'>
# print(type(oo.index[100])) # <class 'int'>
# oo.index[100]=9  # 尝试修改索引，失败


"""设置索引 set_index()"""

ath = oo.set_index("Athlete")
# print(ath.head())

""" 修改原数据索引 """
# oo.set_index("Athlete",inplace=True)
# oo.head()


"""复位索引"""
# print(ath.head())
ath1 = ath.reset_index()
print(ath1.head())