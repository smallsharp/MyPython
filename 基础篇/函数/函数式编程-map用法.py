## 需求：对原列表进行原地平方

# 1.基本实现

def square(x):
    return x ** 2


list_x = [1, 2, 3, 4, 5, 6, 7]

# for i, x in enumerate(list_x):
#     list_x[i] = square(x)

# print(list_x)  # [1, 4, 9, 16, 25, 36, 49]


# 2. 使用map实现,集合中的每个元素，都进行映射(square)操作

r = map(square, list_x)
print(list(r))

# 3. 使用map结合lambda使用
r = map(lambda x: x ** 2, list_x)
print(list(r))

# 4. 多参数的场景，注意多个参数时，长度不一致的情形
list_x = [1, 2, 3, 4, 5, 6, 7]
list_y = [1, 2, 3, 4, 5]

r = map(lambda x, y: x + y, list_x, list_y)
# print(list(r)) # [2, 4, 6, 8, 10]
