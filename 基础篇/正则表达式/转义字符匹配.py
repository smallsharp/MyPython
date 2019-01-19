import re

content = '(百度)www.baidu.com'


# 当遇到用于正则匹配模式的特殊字符时，我们在前面加反斜线来转义一下就可以匹配了。例如.我们就可以用\.来匹配
result = re.match('\(百度\)www\.baidu\.com', content)
print(result)