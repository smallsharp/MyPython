# coding=utf-8
import pandas as pd

"""
读取csv文件
"""
s = pd.read_csv("abc.csv", skiprows=2)
# print(pd.__version__)

"""
pandas.DataFrame.sort_values
排序方式1
"""

# print(s.Brand)
# print(type(s.Brand))
# print(s.Version.sort_values())
n1 = s.Version.sort_values()
print(n1)

"""
pandas.DataFrame.sort_values
排序方式2
"""
new = s.sort_values(by=["Version","Ram"])
print(new)