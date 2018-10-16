import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'

# match()方法是从字符串的开头开始匹配，一旦开头不匹配，那么整个匹配就失败了
# 它是以Extra开头的，但是正则表达式我们是以Hello开头的，整个正则表达式是字符串的一部分，但是这样匹配是失败的
result = re.match('Hello.*?(\d+).*?Demo', content)
print(result) # None


# 在匹配时会扫描整个字符串，然后返回第一个成功匹配的结果，也就是说，正则表达式可以是字符串的一部分，
# 在匹配时，search()方法会依次扫描字符串，直到找到第一个符合规则的字符串，然后返回匹配内容，如果搜索完了还没有找到，那就返回None
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)
print(result.group(1))
