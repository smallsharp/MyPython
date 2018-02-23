# coding=utf-8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""使用 seaborn"""

oo = pd.read_csv("olympics.csv", skiprows=4)


"""
    统计 2008年 中国队获得奖牌数量（男，女）
"""
# t1 = sns.countplot(x="Medal",data=oo)

"""第一步：先筛选出08年 中国队的数据"""
chn = oo[(oo.Edition==2008)&(oo.NOC=="CHN")]
print(chn.head(10))

"""第二步：使用pyplot 显示统计数据"""
# t1 = chn.Gender.value_counts().plot(kind="bar")
# plt.show(t1)

"""第二步：使用sns 显示统计数据"""
# t2 = sns.countplot(data=oo,x="Gender")
# plt.show(t2)

"""第三步：使用sns 显示统计数据，并改变图形显示的颜色（palette）"""
# t3 = sns.countplot(data=oo,x="Gender",palette="bwr")
# plt.show(t3)


"""
    分性别，统计金牌，银牌，铜牌的数量,order调整显示的顺序
"""
t4 = sns.countplot(data=oo,x="Medal",hue="Gender",palette="bwr",order=["Gold","Silver","Bronze"])
plt.show(t4)

# t5 = sns.countplot(data=oo,x="Gender",hue="Medal")
# plt.show(t5)