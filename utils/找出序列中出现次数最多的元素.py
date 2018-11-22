from collections import Counter

words = ['hello', 'jack', 'top', 'money', 'tom', 'money', 'python', 'python', 'money', 'jack']

# 统计
counts = Counter(words)

# 获取出现次数最多的
top = counts.most_common(3)
print(top)

# 获取单个次的次数
print(counts['python'])

# 手动增加次数场景
morewords = ['why', 'name', 'looking', 'my','python','python']

for word in morewords:
    counts[word] += 1

print(counts.most_common(3))
