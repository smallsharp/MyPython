# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt

# %matplotlib inline

"""
读取csv文件
"""
s = pd.read_csv("abc.csv", skiprows=2)


""" 显示图形 """
# t1 = s.Ram.value_counts().plot() # 显示线性图
# plt.show(t1)

# t2 = s.Ram.value_counts().plot(kind="line")  # 默认，同上
# plt.show(t2)

t3 = s.Ram.value_counts().plot(kind="bar")  # 竖排柱状图
plt.show(t3)

# t4 = s.Ram.value_counts().plot(kind="barh")  # 横排柱状图
# plt.show(t4)

# t5 = s.Ram.value_counts().plot(kind="pie")  # 饼状图
# plt.show(t5)
