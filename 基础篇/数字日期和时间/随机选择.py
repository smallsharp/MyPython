import random

values = [1, 2, 3, 4, 5, 6, 7]

v = random.choice(values)  # 随机从序列中取一个值
print(v)

v2 = random.sample(values, 2)  # 随机从序列中取多个值
print(v2)
print(values)

random.shuffle(values)  # 原地打乱元素顺序
print(values)

##########################################################################

n1 = random.randint(0, 10)  # [0,10]中随机一个整数
print(n1)

n2 = random.random()  # [0,1) 种浮点数字
print(n2)
