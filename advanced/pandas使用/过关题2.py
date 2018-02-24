#coding=utf-8
import pandas as pd
import sys, io

import matplotlib.pyplot as plt

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 设置控制台显示宽度
pd.set_option("display.width", 1000)

oo = pd.read_csv("olympics.csv",skiprows=4)
# print(oo.head())

"""
1.In which events did Jesse Owens win a medal?，show events he take part in.
"""
p1 = oo.Edition.sort_index().plot()

plt.show(p1)

