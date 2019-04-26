import re

# 1. re.match(),匹配以指定字符开头的数据
text = 'Hello Python'
ret = re.match('Hel', text)
print('match:{}'.format(ret.group()))

# 2. re.search(),匹配以指定字符开头的数据
text = 'the price of apple is $299'
ret = re.search(r'\$\d+', text)
print('search:{}'.format(ret.group()))

# 3. re.findall(),匹配出所有符合条件的数据列表
text = 'the price of apple is $299, the price of meizu is $288'
ret = re.findall(r'\$\d+', text)
print('search:{}'.format(ret))

# 4. re.sub(pattern, repl, string, count=0, flags=0)
text = 'the price of apple is $299, the price of meizu is $288'
ret = re.sub(r'\$\d+', '$20', text)
print('sub:{}'.format(ret))

# 5. re.split
text = "hello&world ni hao"
ret = re.split('\W', text)
print('split:{}'.format(ret))

# compile：对于一些经常要用到的正则表达式，可以使用compile进行编译，后期再使用的时候可以直接拿过来用，执行效率会更快。而且compile还可以指定flag=re.VERBOSE，在写正则表达式的时候可以做好注释。示例代码如下：

text = "the number is 20.50"
r = re.compile(r"""
                \d+ # 小数点前面的数字
                \.? # 小数点
                \d* # 小数点后面的数字
                """, re.VERBOSE)
ret = re.search(r, text)
print(ret.group())
