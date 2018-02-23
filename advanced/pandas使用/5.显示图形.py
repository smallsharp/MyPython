# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt

# %matplotlib inline

"""
读取csv文件
"""
s = pd.read_csv("abc.csv", skiprows=2)


""" 1.改变线条颜色 """
t1 = s.Ram.value_counts().plot(kind="line",color="green") # 设置线条的颜色
# plt.show(t1)

""" 2.设置图形的宽度，高度 """
t2 = s.Ram.value_counts().plot(kind="line",color="green",figsize=(10,3)) # 设置图形的宽度、高度
# plt.show(t2)

"""3.设置饼图的颜色"""
t3 = s.Ram.value_counts().plot(kind="pie")  # 饼状图
t3 = s.Ram.value_counts().plot(kind="pie",colormap="Dark2")  # 饼状图
plt.show(t3)
