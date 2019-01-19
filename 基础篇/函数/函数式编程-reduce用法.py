from functools import reduce

# 连续运算,连续调用lambda

list_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

r = reduce(lambda x, y: x + y, list_x, 100)  # 1，2 ==》(1+2)，3==》(1+2+3)，4 ...

print(r)
