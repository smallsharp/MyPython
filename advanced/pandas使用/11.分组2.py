# coding=utf-8
import pandas as pd

import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 设置控制台显示宽度
pd.set_option("display.width", 1500)

""" 读取csv文件 """
oo = pd.read_csv("olympics.csv", skiprows=4)


"""
1.根据多列分组 groupby
"""

edition = oo.groupby(["Edition","NOC","Medal"])

# print(list(edition))


"""
2.统计最大值，最小值等
"""
# counts = edition.agg(["min","max","count"])
counts = edition.agg({"Edition":["min","max","count"]})
# print(counts)

# print(edition.size())

"""
"""
ete = oo.loc[oo.Athlete=="LEWIS, Carl"].agg({"Edition":["min","max","count"]})
ete = oo.loc[oo.Athlete=="LEWIS, Carl"].groupby("Athlete").agg({"Edition":["min","max","count"]})
print(ete)