# 普通函数

def add(x, y):
    return x + y


# 匿名函数 lambda 表达式 ":"后是 表达式
lambda x, y: x + y



# 错误的写法
funcs = [lambda x: x + n for n in range(0, 5)]

# for f in funcs:
#     print(f(0))

# 正确的写法

funcs = [lambda x, n=n: x + n for n in range(0, 5)]  # 这样定义，才能捕获到n的值

for f in funcs:
    print(f(10))