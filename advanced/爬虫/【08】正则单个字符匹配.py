import re

# 匹配单个字符串

# 1. 匹配某个字符串：
text = 'hello'
ret = re.match('he', text)
print(ret.group())

# 2. 点（.）匹配任意的字符：
text = "ab"
ret = re.match('.', text)
print(ret.group())

# 注意 .匹配不到换行符，如下
text = "\nab"
ret = re.match('.', text)
# print(ret.group()) # >> AttributeError: 'NoneType' object has no attribute 'group'

# 3. \d匹配任意一个数字：
text = "123"
ret = re.match('\d', text)
print('\d:{}'.format(ret.group()))

# 4. \D匹配任意一个的非数字：
text = "a"
ret = re.match('\D', text)
print('\D:{}'.format(ret.group()))

# 5. \s匹配的是任意一个空白字符（包括：\n，\t，\r和空格）
text = "\t\r"
ret = re.match('\s', text)
print('\s:{}'.format(ret.group()))

# 6. \w匹配的是a-z和A-Z以及数字和下划线
text = "_"
ret = re.match('\w', text)
print('\w:{}'.format(ret.group()))

# 7. \W匹配的是和\w相反的
text = "*+="
ret = re.match('\W', text)
print('\W:{}'.format(ret.group()))

# 8. []组合的方式，只要满足中括号中的某一项都算匹配成功，只匹配一个
# \d:[0-9]
# \D:[^0-9]
# \w:[0-9a-zA-Z]
# \W:[^0-9a-zA-Z]

text = "0731-88888888"
ret = re.match('[\d\-]+', text)
print('[]:{}'.format(ret.group()))

# 9. ^（脱字号）：表示以...开始，注意re.match()本身就是以开头匹配，所以加不加^,效果一样
#  注意：如果放在[]中，则表示取反操作
text = "hello"
ret = re.match('^he', text)
print('^:{}'.format(ret.group()))

# 10 $：表示以...结束：
# 匹配163.com的邮箱
text = "abc_888@163.com"
ret = re.search('\w+@163\.com$', text)
print('$:{}'.format(ret.group()))  # .需要转义，表示匹配的是.，不是正则中的.

# 11. |：匹配多个表达式或者字符串：
text = "a,Hello,Python"
ret = re.search('a|Python', text)
print('|:{}'.format(ret.group()))  # 匹配a 或者 Python，如果前面一个匹配成功则返回，否则下一个匹配
