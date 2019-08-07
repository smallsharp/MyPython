import re

# 1. * 匹配0个或任意多个
text = "0731"
ret = re.match('\d*', text)
print('*:{}'.format(ret.group()))

# 2. + 可以匹配1个或者多个字符，最少匹配一个，没有满足则报错
text = "abc"
ret = re.match('\w+', text)
print('+:{}'.format(ret.group()))

# 3. ?：匹配的字符可以出现一次或者不出现（0或者1）。示例代码如下：

text = "a123"
ret = re.match('\d?', text)
print('?:{}'.format(ret.group()))

# 4. {m}：匹配m个字符。示例代码如下：
text = "123"
ret = re.match('\d{2}', text)
print('中括号1:{}'.format(ret.group()))

# 5. {m,n}：匹配m-n个字符，在这中间的字符都可以匹配到，最大匹配，示例代码如下：
text = "12345"
ret = re.match('\d{1,3}', text)
print('中括号2:{}'.format(ret.group()))

##################################################################################

# 贪婪和非贪婪

# 1. 示例1
text = "0123456"
ret = re.match('\d+', text)
print('贪婪模式:{}'.format(ret.group()))
# 因为默认采用贪婪模式，所以会输出0123456
# >> 0123456

# 可以改成非贪婪模式，那么就只会匹配到0, 加上?,表示尽可能少的匹配，示例代码如下：
text = "0123456"
ret = re.match('\d+?', text)
print('非贪婪模式:{}'.format(ret.group()))

# 示例2

text = "<span>姓名:<span>"
ret = re.match('<.+>', text)
print('贪婪模式:{}'.format(ret.group()))  # <span>姓名:<span>

text = "<span>姓名:<span>"
ret = re.match('<.+?>', text)
print('非贪婪模式:{}'.format(ret.group()))  # <span>
