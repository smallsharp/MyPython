import requests
from urllib import request
from lxml import etree
import re


def parse_page(page):
    url = 'https://www.doutula.com/photo/list/?page={}'.format(page)
    response = requests.get(url)

    html = etree.HTML(response.text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")

    for img in imgs:
        name = img.get('alt')
        # 替换图片名称中的特殊字符
        name = re.sub(r'[\?？\.。!！\*]', '', name)
        img_url = img.get('data-original')
        suffix = str(img_url).rsplit('.', maxsplit=1)[-1]
        filename = name + '.' + suffix
        # imgs 文件夹需要手动创建
        request.urlretrieve(img_url, filename='imgs/' + filename)
        print(img_url, name, suffix)


def main():
    for page in range(1, 3):
        parse_page(page)
        # break


if __name__ == '__main__':
    main()
