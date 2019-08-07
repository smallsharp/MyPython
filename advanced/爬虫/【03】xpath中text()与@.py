html_str = """
<tr class="even">
    <td class="square">
        <a target="_blank" href="position_detail.php?id=48633">Python开发工程师</a>
    </td>
    <td>技术类</td>
    <td>2</td>
    <td>广州</td>
    <td>2019-03-18</td>
</tr>
"""

from lxml import etree
html = etree.HTML(html_str)

# 1. 提取a标签的href属性值
href = html.xpath("//a/@href")[0]

# 2. 提取第一个td标签的class属性值
clz = html.xpath("//td[1]/@class")[0]

# 3. 提取a标签的文本
text = html.xpath("//a/text()")[0]

print(href,clz)
print(text)
