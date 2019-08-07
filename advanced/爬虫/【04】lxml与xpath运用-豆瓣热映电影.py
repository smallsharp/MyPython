# coding=utf-8
from lxml import etree
import requests


def parse_html(url):
    response = requests.get(url)
    html = etree.HTML(response.text)

    movelist = html.xpath("//div[@id='nowplaying']//ul[@class='lists']/li")
    print('电影总数：%d' % len(movelist))

    for move in movelist:
        move_dict = {
            'title': move.xpath("./@data-title")[0],
            'score': move.xpath("./@data-score")[0],
            'director': move.xpath("./@data-director")[0],
            'actors': move.xpath("./@data-actors")[0],
            'uptime': move.xpath("./@data-release")[0]
        }
        print(move_dict)


def main():
    url = 'https://movie.douban.com/cinema/nowplaying/shanghai/'
    parse_html(url)


if __name__ == '__main__':
    main()
