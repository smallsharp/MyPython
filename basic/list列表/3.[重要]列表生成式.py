#encoding=utf-8

a = [x**2 for x in [1, 2, 3, 4]]                      # [1, 4, 9 16]

"""
zip()可以按顺序同时输出两个列表对应位置的元素对,
zip()不会自动帮助判断两个列表是否长度一样，所以最终的结果会以短的列表为准
"""
b = [sum(x) for x in zip([1,2,3],[5,6,7])]  # [6, 8, 10]


c = [x for x in [1,2,3,4,5,6] if x %2==1 ] # [1, 3, 5]

"""
如果需要生成 迭代器 只需要把[]换成()
"""
iter_odd = (x**2 for x in [1, 2, 3, 4, 5] if x % 2)

# print(a,type(a),end="\n")
print(iter_odd,type(iter_odd),end="\n")

# print(iter_odd.__next__())
# print(iter_odd.__next__())
# print(iter_odd.__next__())
# print(iter_odd.__next__())

for i in iter_odd:
    print(i)

"""
如果需要生成 字典 只需要把[]换成{}
"""
square_dict = {x: x ** 2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# print(square_dict,type(square_dict),end="\n")

