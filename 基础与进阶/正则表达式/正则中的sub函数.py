import re

# 1. 最基础的替换：将数字替换为空字符
content = '123He456ll7o890'
content = re.sub('\d+', '', content)  # Hello

text = 'Today is 11/27/2018,PyCon starts 12/03/2019'
# ==>  Today is 2018-11-27,PyCon starts 2019-12-03

# 2.sub() 参数1：匹配的模式，参数2：需要替换上的模式，\3"指的是模式捕获组中的数字
newtext = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(newtext)

# 3. 先写匹配模式
datapat = re.compile(r'(\d+)/(\d+)/(\d+)')
newtext = datapat.sub(r'\3-\1-\2', text)
print(newtext)


# 也可以指定个函数
def change_date(m):
    return '{}-{}-{}'.format(m.group(3), m.group(1), m.group(2))


print(datapat.sub(change_date, text))
