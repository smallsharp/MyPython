## 需求，踢除不必要的元素

list_x = [1, 3, 0, 5, 0, 7, 2]

# filter，过滤器： 通过函数返回结果，判断是否保留
r = filter(lambda x: True if x != 0 else False, list_x)

print(list(r))

## 需求：过滤大于4的数据
list_y = [2, 4, 6, 8, 10]

new_list = filter(lambda x: x > 4, list_y)

print(list(new_list))
