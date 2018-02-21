# coding=utf-8
import pandas as pd

"""
读取csv文件
"""
s = pd.read_csv("abc.csv", skiprows=2)
# print(pd.__version__)


"""
head(n) 和 tail(n)的用法
"""
print(s.head())  # 默认前5行
print("-" * 50)
print(s.tail())  # 默认后五行
print("-" * 50)

"""
info的用法
"""
print(s.info())
print("-" * 50)

"""
value_counts()
"""
print(s.Brand.value_counts())
print("-" * 50)
print(s.Brand.value_counts(ascending=True, dropna=False)) # 正序排列，去除None数据
