import re

content = 'Hello 1234567 World_This is a Regex Demo'

# 使用() 匹配目标
result = re.match(r'^Hello\s(\d+)\sWorld', content)
print(result.group(0))
print(result.group(1))
print(result.span())

result = re.match('^Hello.*World', content)
print(result.group())
print(result.span())

# 贪婪模式
result = re.match('^He.*(\d+).*Demo$', content)
print(result.group(1))  # 7

# 非贪婪模式(.*匹配尽可能少的字符)
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$', content)
print(result.group(1))  # 1234567

content = '''Hello 1234567 World_This
is a Regex Demo
'''
result = re.match('^He.*?(\d+).*?Demo$', content)
# print(result.group(1)) #  'NoneType' object has no attribute 'group'

# 因为.匹配的是除换行符之外的任意字符，当遇到换行符时，.*?就不能匹配了，所以导致匹配失败。加一个修饰符re.S，即可修正。
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)

##########################
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
# m = datepat.match('11/27/2018')
m = datepat.match('11/27/2018xyz')  # None 是否以日期格式结尾，False，所以匹配不到
if m:
    print('pp')
else:
    print('nnn')
