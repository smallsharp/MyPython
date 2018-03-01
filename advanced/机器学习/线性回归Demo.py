# coding=utf-8


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 20)

# print(x)

a = np.random.randint(1, 10, 20)

y = x * 4 + a

# p1 = plt.plot(x, y, "o")
# plt.show(p1)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x.reshape(20, 1), y.reshape(20, 1))

model.predict(6)

print(model.coef_)
print(model.intercept_)

# y = kx + b
value = model.coef_*6 + model.intercept_
print(value)
