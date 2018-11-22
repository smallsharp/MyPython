# 错误的写法
funcs = [lambda x: x + n for n in range(0, 5)]

# for f in funcs:
#     print(f(0))

# 正确的写法

funcs = [lambda x, n=n: x + n for n in range(0, 5)]  # 这样定义，才能捕获到n的值

for f in funcs:
    print(f(0))
