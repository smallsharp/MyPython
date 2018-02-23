# coding=utf-8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # seaborn基于matplotlib

oo = pd.read_csv("olympics.csv", skiprows=4)
print(oo.head())


"""
使用 seaborn，seaborn基于matplotlib
"""

"""
统计所有奖牌
"""
t1 = sns.countplot(x="Medal",data=oo)
plt.show(t1)

"""
根据性别显示 奖牌
"""
t2 = sns.countplot(x="Medal",data=oo,hue="Gender")
plt.show(t2)
