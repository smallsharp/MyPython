# 普通版
items = ['python', 'js', 'java', 'c++']
for index in range(len(items)):
    print(index, "-->", items[index])

# 优雅版
for index, item in enumerate(items):  # 音标：[ɪ'njuːməreɪt]
    print(index, "-->", item)

# enumerate 还可以指定元素的第一个元素从几开始，默认是0，也可以指定从1开始：
for index, item in enumerate(items, start=1):
    print(index, "-->", item)

# 如果只需要遍历值
for item in items:
    print(item)
