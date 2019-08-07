from functools import reduce

# 连续运算,连续调用lambda

list_x = [2, 4, 6, 8, 10]

new_list = reduce(lambda x, y: x + y, list_x, 20)  # 2，4 ==》(2+4)，6==》(2+4+6)，8 ...

print(new_list)
