# encoding=utf-8

# 1.列表推导式
a = [x ** 2 for x in [1, 2, 3, 4]]  # [1, 4, 9 16]
c = [x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 1]  # [1, 3, 5]

# 2 .列表生成式 如果需要生成 迭代器 只需要把[]换成()
iter_gen = (x ** 2 for x in [1, 2, 3, 4, 5] if x % 2)
print(iter_gen, type(iter_gen), end="\n")

# 将生成式 快速 转成list
print(list(iter_gen))

# 3. 如果需要生成 字典 只需要把[]换成{}
square_dict = {x: x ** 2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# print(square_dict,type(square_dict),end="\n")
