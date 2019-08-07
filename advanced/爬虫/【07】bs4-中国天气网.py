from bs4 import BeautifulSoup
import requests
from pyecharts import Bar

all_data = []


def parser_html(url):
    response = requests.get(url)
    html = response.content.decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')

    all_provinces = soup.find('div', attrs={'class': 'conMidtab'})

    # 当前页面中的 所有省份数据
    provices = all_provinces.find_all('div', class_='conMidtab2')

    for provice in provices:  # 每个省份的信息
        # 省份下的所有城市数据
        citys = provice.find_all('tr')[2:]

        # 每个城市的数据
        for index, city in enumerate(citys):
            tds = city.find_all('td')
            if index == 0:
                city_name = tds[1].find('a').get_text()
            city_name = tds[0].find('a').get_text()
            city_min_temp = tds[-2].get_text()
            data = {"city": city_name, 'min_temp': int(city_min_temp)}
            all_data.append(data)


def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml', 'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml', 'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml', 'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml'
    ]
    total_data = []
    for url in urls:
        parser_html(url)

    all_data.sort(key=lambda x: x['min_temp'])
    topTen = all_data[0:10]
    data_citys = [i['city'] for i in topTen]
    data_temp = [i['min_temp'] for i in topTen]

    bar = Bar('TopTen')
    bar.add('', data_citys, data_temp)
    bar.render('topTen.html')


if __name__ == '__main__':
    main()
