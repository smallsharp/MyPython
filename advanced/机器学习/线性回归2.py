#coding=utf-8
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model


# read_csv里面的参数是csv在你电脑上的路径，此处csv文件放在notebook运行目录下面的CCPP目录里
data = pd.read_excel('abcd.xlsx')

# 测试一下
# print(data.head())

# 数据的维度
# print(data.shape) #(9568, 5)


# 现在我们开始准备样本特征X，我们用AT， V，AP和RH这4个列作为样本特征。

X = data[['AT', 'V', 'AP', 'RH']]
# print(X.head())


# 接着我们准备样本输出y， 我们用PE作为样本输出。

y = data[['PE']]


# 5. 划分训练集和测试集

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


print (X_train.shape)
print (y_train.shape)
print (X_test.shape)
print (y_test.shape)

"""
(7176, 4)
(7176, 1)
(2392, 4)
(2392, 1)
"""


