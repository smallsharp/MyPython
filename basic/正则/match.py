
import re

content = 'Hello 1234567 World_This is a Regex Demo'


# 使用() 匹配目标
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result.group(0))
print(result.group(1))
print(result.span())


result = re.match('^Hello.*World', content)
print(result.group())
print(result.span())


# 贪婪模式
result = re.match('^He.*(\d+).*Demo$', content)
print(result.group(1)) # 7


# 非贪婪模式(.*匹配尽可能少的字符)
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$', content)
print(result.group(1)) # 1234567


content = '''Hello 1234567 World_This
is a Regex Demo
'''
result = re.match('^He.*?(\d+).*?Demo$', content)
# print(result.group(1)) #  'NoneType' object has no attribute 'group'

# 因为.匹配的是除换行符之外的任意字符，当遇到换行符时，.*?就不能匹配了，所以导致匹配失败。加一个修饰符re.S，即可修正。
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
