# coding=utf-8
import json
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import requests


def get_page_index(offset, keyword):
    data = {
        "offset": offset,
        "format": "json",
        "keyword": keyword,
        "autoload": "true",
        "count": 20,
        "cur_tab": 3,
        "from": "gallery"
    }
    url = "https://www.toutiao.com/search_content/?" + urlencode(data)
    res = requests.get(url)
    if res.status_code == 200:
        return res.text
    return None


def parse_page_index(html):
    urllist = []
    json_data = json.loads(html)
    if json_data and "data" in json_data.keys():
        for d in json_data.get("data"):
            urllist.append(d.get("article_url"))
        return urllist

def get_page_detail(url):
    res = requests.get(url)
    if res.status_code==200:
        return res.text
    return None

def parse_page_detail(html):
    soup = BeautifulSoup(html,"lxml") # pip install lxml
    title = soup.select("title")
    print(title[0].text)


def main():
    html = get_page_index(0, "街拍美女")
    print(html)
    urllist = parse_page_index(html)
    print(urllist)
    if urllist:
        for url in urllist:
            detail = get_page_detail(url)
            if detail:
                parse_page_detail(detail)
if __name__ == '__main__':
    main()
