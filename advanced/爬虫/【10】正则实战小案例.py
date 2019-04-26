import re

# 1. 验证手机号码：规则是以1开头，第二位可以是35678，后面9个数字。示例代码如下：
text = '13344445555'
ret = re.match('1[35678]\d{9}', text)
print('手机号匹配:{}'.format(ret.group()))

# 2. 验证邮箱：邮箱的规则是邮箱名称是用数字、数字、下划线组成的，然后是@符号，后面就是域名了。示例代码如下：

text = 'lfl5207_888@163.com'
ret = re.match('\w+@\w+\.[a-zA-Z]+', text)
print('邮箱匹配:{}'.format(ret.group()))

# 3. 验证URL：URL的规则是前面是http或者https或者是ftp然后再加上一个冒号，再加上一个斜杠，再后面就是可以出现任意非空白字符了。示例代码如下：
text = "https://www.baidu.com/"
ret = re.match('(http|https|ftp)://.+', text)
print('URL匹配:{}'.format(ret.group()))

# 4. 验证身份证：身份证的规则是，总共有18位，前面17位都是数字，后面一位可以是数字，也可以是小写的x，也可以是大写的X。示例代码如下：
text = "31131118908123232x"
ret = re.match('\d{17}(x|X|\d)$', text)
print('身份证匹配:{}'.format(ret.group()))

# 5. 案例：精确匹配0-100之间的数字：1,2,11,99,100,不可出现 01,101等
text = '100'

ret = re.match('[1-9]\d?$|100$', text)
print('数字匹配:{}'.format(ret.group()))

## 在正则表达式中，有些字符是有特殊意义的字符。因此如果想要匹配这些字符，那么就必须使用反斜杠进行转义。比如$代表的是以...结尾，如果想要匹配$，那么就必须使用\$。示例代码如下：

text = "apple price is \$99,orange price is $88"
ret = re.search('\$(\d+)', text)
print('转义匹配:{}'.format(ret.group()))

# 原生字符串：
# 在正则表达式中，\是专门用来做转义的。在Python中\也是用来做转义的。因此如果想要在普通的字符串中匹配出\，那么要给出四个\。示例代码如下：

text = "apple \c"
ret = re.search('\\\\c', text)
print('转义匹配:{}'.format(ret.group()))

# 因此要使用原生字符串就可以解决这个问题：
text = "apple \c"
ret = re.search(r'\\c', text)
print('原生匹配:{}'.format(ret.group()))
