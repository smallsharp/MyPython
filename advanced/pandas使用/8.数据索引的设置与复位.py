# coding=utf-8
import pandas as pd

# 设置控制台显示宽度
pd.set_option("display.width", 1000)

"""
读取csv文件
"""
oo = pd.read_csv("olympics.csv", skiprows=4)

type(oo.index)  # <class 'pandas.core.indexes.range.RangeIndex'>
type(oo.index[100]) # <class 'int'>
# oo.index[100]=9  # 尝试修改索引，失败
oo.index # RangeIndex(start=0, stop=29216, step=1)


"""
1.设置索引 set_index()
"""

ath = oo.set_index("Athlete") # 将运动员姓名作为索引
# print(ath.head())

"""
2.修改原数据索引 inplace 表示是否替换原数据
"""
oo.set_index("Athlete",inplace=True)
print(oo.head())


"""
3.复位索引
"""
ath.reset_index()
# print(ath.head())


"""
4.复位索引2
"""
oo.reset_index(inplace=True)
print(oo.head())