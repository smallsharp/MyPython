# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt

# %matplotlib inline

"""
1.读取csv文件
"""
oo = pd.read_csv("olympics.csv", skiprows=4)
fo = oo[oo.Edition==1896]

""" 
2.显示线性图1 Line plot
"""
# p1 = fo.Sport.value_counts().plot()
# plt.show(p1)

"""
2.显示线性图2
"""
# p2 = fo.Sport.value_counts().plot()
# plt.show(p2)

"""
3.显示竖排柱状图 
"""
# p3 = fo.Sport.value_counts().plot(kind="bar")  # 竖排柱状图
# plt.show(p3)


"""
横排柱状图
"""
p4 = fo.Sport.value_counts().plot(kind="barh")  # 横排柱状图
plt.show(p4)

# p5 = fo.Sport.value_counts().plot(kind="pie")  # 饼状图
# plt.show(p5)
