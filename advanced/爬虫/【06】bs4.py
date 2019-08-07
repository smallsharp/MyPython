from bs4 import BeautifulSoup

html = """
<table class="tablelist" cellpadding="0" cellspacing="0">
    <tbody>
    <tr class="h">
        <td class="l" width="374">职位名称</td>
        <td>职位类别</td>
        <td>人数</td>
        <td>地点</td>
        <td>发布时间</td>
    </tr>
    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=48636&amp;keywords=&amp;tid=0&amp;lid=0">25664-政府行业解决方案架构师（北京/广州）（广州）</a>
        </td>
        <td>技术类</td>
        <td>1</td>
        <td>广州</td>
        <td>2019-03-18</td>
    </tr>
    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=48637&amp;keywords=&amp;tid=0&amp;lid=0">25664-数据挖掘高级工程师</a>
        </td>
        <td>技术类</td>
        <td>2</td>
        <td>广州</td>
        <td>2019-03-18</td>
    </tr>
    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=48633&amp;keywords=&amp;tid=0&amp;lid=0">25664-数据治理高级工程师</a>
        </td>
        <td>技术类</td>
        <td>2</td>
        <td>广州</td>
        <td>2019-03-18</td>
    </tr>
    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=48634&amp;keywords=&amp;tid=0&amp;lid=0">25664-web前端开发高级工程师</a>
        </td>
        <td>技术类</td>
        <td>2</td>
        <td>广州</td>
        <td>2019-03-18</td>
    </tr>
    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=48635&amp;keywords=&amp;tid=0&amp;lid=0">25664-政府行业解决方案架构师（北京/广州）（北京）</a>
        </td>
        <td>技术类</td>
        <td>1</td>
        <td>北京</td>
        <td>2019-03-18</td>
    </tr>
    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=48631&amp;keywords=&amp;tid=0&amp;lid=0">25925-Linux
            C++后台开发工程师</a></td>
        <td>技术类</td>
        <td>1</td>
        <td>深圳</td>
        <td>2019-03-18</td>
    </tr>
    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=48632&amp;keywords=&amp;tid=0&amp;lid=0">29303-视觉设计师</a>
        </td>
        <td>设计类</td>
        <td>1</td>
        <td>深圳</td>
        <td>2019-03-18</td>
    </tr>
    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=48628&amp;keywords=&amp;tid=0&amp;lid=0">22989-中间件高级交付工程师（北京）</a>
        </td>
        <td>技术类</td>
        <td>1</td>
        <td>北京</td>
        <td>2019-03-18</td>
    </tr>
    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=48629&amp;keywords=&amp;tid=0&amp;lid=0">25927-先游产品运营组组长</a>
        </td>
        <td>产品/项目类</td>
        <td>1</td>
        <td>上海</td>
        <td>2019-03-18</td>
    </tr>
    <tr class="odd">
        <td class="l square"><a id="test" class="test" target="_blank" href="position_detail.php?id=48630&amp;keywords=&amp;tid=0&amp;lid=0">19511-Web前端开发</a>
        </td>
        <td>技术类</td>
        <td>1</td>
        <td>深圳</td>
        <td>2019-03-18</td>
    </tr>
    </tbody>
</table>
"""

soup = BeautifulSoup(html, 'lxml')

# 1 .获取所有的tr标签
trs = soup.find_all('tr')

# 2. 获取第二个tr标签,limit 表示查找的数量
tr = soup.find_all('tr', limit=2)[-1]

# 3. 获取所有class等于even的tr标签\
# 第一种写法，注意是 class_ 与 python的class关键字区分
trs = soup.find_all('tr', class_='even')

# 第二种写法
trs = soup.find_all('tr', attrs={"class": "even"})
# for tr in trs:
#     print(tr)
#     print('-' * 40)

# 4. 获取id等于test 且 class等于test的a标签
# 第一种写法，注意是 class_ 与 python的class关键字区分
trs = soup.find_all('a', id='test', class_='test')

# 第二种写法
trs = soup.find_all('tr', attrs={"id": "test", "class": "test"})

# 5. 获取所有a标签的href属性
aList = soup.find_all('a')
for a in aList:
    # print(a['href'])
    # print(a.attrs['href'])
    pass

# 6. 获取所有职位信息（纯文本）
trs = soup.find_all('tr')[1:]
for tr in trs:
    tds = tr.find_all('td')
    title = tds[0].find('a').string
    category = tds[1].string
    nums = tds[2].string
    city = tds[3].string
    pubtime = tds[4].string
    # print(title, category, nums, city, pubtime)
    # print('-' * 40)

# find
aElement = soup.find('a', attrs={'id': 'test'})
print(aElement)

href = aElement['href']
class_ = aElement['target']
clz = aElement.attrs['class']

soup.select('tr')
