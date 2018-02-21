# coding=utf-8
import pandas as pd

"""
读取csv文件
"""
s = pd.read_csv("abc.csv", skiprows=2)
# print(pd.__version__)

"""
筛选数据
"""

# 筛选出Ram=2G的数据
print( s[s.Ram == "2G"] )

# 筛选出Ram=2G的数据 并且 Version=6.0.1 的数据
print( s[(s.Ram == "2G")&(s.Version=="6.0.1")] )

# 筛选出Ram=2G的数据 或者 Version=6.0.1 的数据
print( s[(s.Ram == "2G")|(s.Version=="6.0.1")] )

# 筛选出Brand contains Meitu的数据
print(s[s.Brand.str.contains("Meitu")])
