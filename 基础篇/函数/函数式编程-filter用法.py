## 需求，踢除不必要的元素

list_x = [1, 3, 0, 5, 0, 7, 2]

# filter，过滤器： 通过函数返回结果，判断是否保留
r = filter(lambda x: True if x != 0 else False, list_x)

print(list(r))

list_y = ['a', "B", 'ss', 'Tom', 'xx']

r = filter(lambda x: x, list_y)

print(list(r))
