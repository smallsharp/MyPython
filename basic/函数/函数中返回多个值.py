# 从函数中返回多个值
def mathMaxMinSum(*args: int) -> int:
    return max(args), min(args), sum(args)


print(mathMaxMinSum(3, 5, 7, 9))

# 元组序列解包

max, min, avg = mathMaxMinSum(4, 5, 8, 3)

print(max, min, avg, sep='|')
