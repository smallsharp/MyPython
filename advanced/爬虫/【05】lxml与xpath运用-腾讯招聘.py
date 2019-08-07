from lxml import etree
import requests

Headers = {
    # 403
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
    'Cookie': '_ga=GA1.2.1441170981.1548490074; pgv_pvi=7176464384; _gcl_au=1.1.573574173.1548490074; _gcl_aw=GCL.1548905142.EAIaIQobChMIt6WakomX4AIV0RsqCh31eAJaEAEYASAAEgLYm_D_BwE; PHPSESSID=5enrp94hc6eduucicol2h0mv11; pgv_si=s3715151872',
    'Referer': 'https://hr.tencent.com/position.php?&start=0',
    'Host': 'hr.tencent.com',
    'Upgrade-Insecure-Requests': '1'
}


def parse_page(page):
    url = 'https://hr.tencent.com/position.php?&start={}#a'.format(page)
    response = requests.get(
        url=url,
        headers=Headers
    )
    # print(response.text)
    html = etree.HTML(response.text)
    trs = html.xpath("//tr[position()>1 and position()<last()]")
    prefix_url = 'https://hr.tencent.com/'
    urlList = []
    for tr in trs:
        urlList.append(prefix_url + tr.xpath(".//a/@href")[0])
    return urlList


def parse_detail(url):
    response = requests.get(
        url=url,
        headers=Headers
    )
    html = etree.HTML(response.text)
    more_infos = html.xpath("//ul[@class='squareli']"),
    position = {
        'title': html.xpath("//tr[1]/td/text()")[0],
        'city': html.xpath("//tr[2]/td[1]/text()")[0],
        'category': html.xpath("//tr[2]/td[2]/text()")[0],
        'nums': html.xpath("//tr[2]/td[3]/text()")[0],
        'duties': html.xpath("//tr[3]//ul//text()")[0],
        'duty': more_infos[0][0].xpath(".//text()"),
        'requirement': more_infos[0][1].xpath(".//text()"),
    }
    print(position)


def main():
    for i in range(10):
        urlList = parse_page(i)
        for detail_url in urlList:
            parse_detail(detail_url)
        break


if __name__ == '__main__':
    main()
