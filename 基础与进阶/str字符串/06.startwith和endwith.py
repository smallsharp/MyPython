filename = 'spam.txt'

filename.endswith('.txt')  # True
filename.startswith('http')  # False

url = 'http://www.python.org'
url.startswith('http:')  # True

# 如果需要同时检查多项
import os

filenames = os.listdir('.')
print(filenames)

newlist = [name for name in filenames if name.endswith(('.py', '.txt'))]  # 注意参数是元组
print(newlist)

# 是否存在 '.ini' 结尾的文件
any((name for name in filenames if name.endswith('.ini')))  # True
