# coding=utf-8
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

"""
1.获取数据，定义问题

数据的介绍： http://archive.ics.uci.edu/ml/datasets/Combined+Cycle+Power+Plant
数据的下载地址： http://archive.ics.uci.edu/ml/machine-learning-databases/00294/
文件中是一个循环发电场的数据，共有9568个样本数据，每个数据有5列，
分别是:AT（温度）, V（压力）, AP（湿度）, RH（压强）, PE（输出电力)
我们的问题是得到一个线性的关系，对应PE是样本输出，而AT/V/AP/RH这4个是样本特征， 机器学习的目的就是得到一个线性回归模型，即:

PE=θ0+θ1∗AT+θ2∗V+θ3∗AP+θ4∗RH，而我们需要学习的，就是θ0,θ1,θ2,θ3,θ4这5个参数。
"""



"""
2.整理数据

下载后的数据可以发现是一个压缩文件，解压后可以看到里面有一个xlsx文件，我们先用excel把它打开，接着“另存为“”csv格式，保存下来，后面我们就用这个csv来运行线性回归。
打开这个csv可以发现数据已经整理好，没有非法数据，因此不需要做预处理。但是这些数据并没有归一化，也就是转化为均值0，方差1的格式。也不用我们搞，后面scikit-learn在线性回归时会先帮我们把归一化搞定。
好了，有了这个csv格式的数据，我们就可以大干一场了。
"""

"""
3.用pandas来读取数据
"""
# 读取源文件
# data = pd.read_excel('abcd.xlsx')

data = pd.read_csv("test.csv")

# 测试一下
# print(data.head())


"""
4.准备运行算法的数据
"""
# 数据的维度
print("data.shape:",data.shape) #(9568, 5) # 说明我们有9568个样本，每个样本有5列。


# 现在我们开始准备样本特征X，我们用AT， V，AP和RH这4个列作为样本特征。
X = data[['AT', 'V', 'AP', 'RH']]
# print(X.head())


# 接着我们准备样本输出y， 我们用PE作为样本输出。
y = data[['PE']]

"""
5. 划分训练集和测试集
"""

# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split

# 　我们把X和y的样本组合划分成两部分，一部分是训练集，一部分是测试集，代码如下：
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# 查看下训练集和测试集的维度，可以看到75%的样本数据被作为训练集，25%的样本被作为测试集
print("X_train.shape:",X_train.shape)
print("X_test.shape",X_test.shape)
print("y_train.shape",y_train.shape)
print("y_test.shape",y_test.shape)


"""
6.运行scikit-learn的线性模型
"""

# 我们可以用scikit-learn的线性模型来拟合我们的问题了。scikit-learn的线性回归算法使用的是最小二乘法来实现的。代码如下：
from sklearn.linear_model import LinearRegression

linreg = LinearRegression()
linreg.fit(X_train, y_train)

# 拟合完毕后，我们看看我们的需要的模型系数结果

print("linreg.intercept_",linreg.intercept_)   # [ 447.06297099]
print("linreg.coef_",linreg.coef_)  # [[-1.97376045 -0.23229086  0.0693515  -0.15806957]]

# 这样我们就得到了在步骤1里面需要求得的5个值。也就是说PE和其他4个变量的关系如下：
# PE=447.06297099 − 1.97376045∗AT − 0.23229086∗V + 0.0693515∗AP − 0.15806957∗RH


"""
7.模型评价
"""
# 我们需要评估我们的模型的好坏程度，对于线性回归来说，我们一般用均方差（Mean Squared Error, MSE）或者均方根差(Root Mean Squared Error, RMSE)在测试集上的表现来评价模型的好坏。

#模型拟合测试集
y_pred = linreg.predict(X_test)

from sklearn import metrics

#用scikit-learn计算MSE
print("MSE:",metrics.mean_squared_error(y_test, y_pred))

## 用scikit-learn计算RMSE
print("RMSE",np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# 得到了MSE或者RMSE，如果我们用其他方法得到了不同的系数，需要选择模型时，就用MSE小的时候对应的参数。

# 比如这次我们用AT， V，AP这3个列作为样本特征。不要RH， 输出仍然是PE
X = data[['AT', 'V', 'AP']]
y = data[['PE']]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X_train, y_train)
#模型拟合测试集
y_pred = linreg.predict(X_test)
from sklearn import metrics
# 用scikit-learn计算MSE
print ("MSE:",metrics.mean_squared_error(y_test, y_pred))
# 用scikit-learn计算RMSE
print ("RMSE:",np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# 可以看出，去掉RH后，模型拟合的没有加上RH的好，MSE变大了


"""
8.交叉验证
"""
# 我们可以通过交叉验证来持续优化模型，代码如下，我们采用10折交叉验证，即cross_val_predict中的cv参数为10：

X = data[['AT', 'V', 'AP', 'RH']]
y = data[['PE']]
from sklearn.model_selection import cross_val_predict
predicted = cross_val_predict(linreg, X, y, cv=10)
# 用scikit-learn计算MSE
print ("MSE:",metrics.mean_squared_error(y, predicted))
# 用scikit-learn计算RMSE
print ("RMSE:",np.sqrt(metrics.mean_squared_error(y, predicted)))

# 可以看出，采用交叉验证模型的MSE比第6节的大，主要原因是我们这里是对所有折的样本做测试集对应的预测值的MSE，而第6节仅仅对25%的测试集做了MSE。两者的先决条件并不同。


"""
9.画图观察结果
"""
# 这里画图真实值和预测值的变化关系，离中间的直线y=x直接越近的点代表预测损失越低。代码如下：

fig, ax = plt.subplots()
ax.scatter(y, predicted)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()