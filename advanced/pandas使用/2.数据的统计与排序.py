# coding=utf-8
import pandas as pd
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 设置控制台显示宽度
pd.set_option("display.width", 1000)

"""
1.读取csv文件
"""
oo = pd.read_csv("olympics.csv", skiprows=4)

# print(oo.head())

"""
2.value_counts(),统计不同值出现的次数,默认降序排列
"""

"""
2.1 统计出不同年份的数据量
"""
# print(oo.Edition.value_counts())

"""
2.1 统计出不同年份的数据量，并且按照正序排列，去除空数据
"""
print(oo.Edition.value_counts(ascending=True, dropna=False))  # 正序排列，去除None数据


"""
3.排序 pandas.DataFrame.sort_values
"""

"""
3.1单行排序
"""
# noc = oo.NOC.sort_values() # 按照字母顺序

"""
3.1 多行排序
如： 先按照年份排序，再按照运动员姓名排序
"""
n1 = oo.sort_values(by=["Edition", "Athlete"])
print(n1.head(20))
