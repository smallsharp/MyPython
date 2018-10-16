import requests,re



res = requests.get('http://dema117.0898wj.com/a/qiyejianjie/')\

# print(res.text)

# list1 = re.findall(r'/.*/.*/(.*.jpg)', res.text)  # 匹配出所有的图片
list1 = re.findall(r'/(.*.jpg)', res.text)  # 匹配出所有的图片
print(res.text)


print(list1)