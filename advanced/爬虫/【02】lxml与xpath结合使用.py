from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('tencent.html')

# html.xpath("xxx") 返回的是元素列表

# 1. 获取所有tr标签
# trs = html.xpath("//tr[position()>1]")
#
# print(len(trs))
#
# for tr in trs:
#     tr_str = etree.tostring(tr, encoding='utf-8').decode('utf-8')
#     # print(tr_str)
#     print('-' * 50)

# 2. 获取第二个tr标签
# trs = html.xpath("//tr[2]")  # 取第二个tr标签
# tr = trs[0]  # 取第一个
# print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))

# 3. 获取所有class等于even的标签
# trs = html.xpath("//tr[@class='even']")
# for tr in trs:
#     tr_str = etree.tostring(tr, encoding='utf-8').decode('utf-8')
#     print(tr_str)
#     print('-' * 50)

# 4. 获取所有a标签的href属性值,待优化

# alist = html.xpath("//a/@href")
# for a in alist:
#     print(a)

# 5. 获取所有职位信息
positions = []
trs = html.xpath("//tr[position()>1 and position()<last()]")
for tr in trs:
    href = tr.xpath(".//a/@href")[0]
    url = 'http://tencent.com/' + href
    job = tr.xpath(".//a/text()")[0]
    type = tr.xpath(".//td[2]/text()")[0]
    city = tr.xpath(".//td[4]/text()")[0]
    position = {
        'url': url,
        'job': job,
        'type': type,
        'city': city
    }
    positions.append(position)
