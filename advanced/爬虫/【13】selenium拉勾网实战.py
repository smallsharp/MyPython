from selenium import webdriver
from lxml import etree
import time
import pymongo


def parse_html():
    # 打开第一页，并获取页面上的所有的url
    driver = webdriver.Chrome()
    url = 'https://www.lagou.com/jobs/list_python?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput='
    driver.get(url)
    driver.maximize_window()
    html = etree.HTML(driver.page_source)
    liTags = html.xpath('//li[@data-positionid]')
    positionIds = []

    while True:
        for li in liTags:
            # get positionid
            positionId = li.xpath('./@data-positionid')[0]
            positionIds.append(positionId)
        print('-' * 40)
        try:
            # 点击下一页
            next_btn = driver.find_element_by_xpath("//span[@action='next']")
            next_btn.click()
            time.sleep(1.5)
            # 获取新页面的liTags,继续循环抓取
            html = etree.HTML(driver.page_source)
            liTags = html.xpath('//li[@data-positionid]')
        except Exception:
            print('没有找到下一页')
            break
    print(positionIds)
    print(len(positionIds))


def parse_detail(driver, positionId):
    url = 'https://www.lagou.com/jobs/{}.html'.format(positionId)

    # 打开详情页，新窗口
    js = 'window.open("{}")'.format(url)
    driver.execute_script(js)
    print(js)
    time.sleep(1)
    # 切换句柄到 新窗口
    driver.switch_to_window(driver.window_handles[-1])

    # 获取页面中需要的数据信息
    html = etree.HTML(driver.page_source)
    position = {
        'title': html.xpath("//span[@class='name']/text()")[0],
        'salary': html.xpath("//span[@class='salary']/text()")[0],
        'publish_time': str(html.xpath("//p[@class='publish_time']/text()")[0]).split()[0],
        'company': html.xpath("//div[@class='company']/text()")[0],
        'work_addr': ''.join(html.xpath("//div[@class='work_addr']/a/text()")[0:-1])
    }
    # print(position)

    # 4. insert data
    mycol = conMongoDB()
    x = mycol.insert_one(position)
    print('{}：插入成功，id:{}'.format(positionId, x.inserted_id))

    # 操作完毕后，关闭该窗口
    driver.close()
    # 切换句柄到主窗口
    driver.switch_to_window(driver.window_handles[0])


def conMongoDB():
    # 1. 连接mongo服务,返回client对象
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # 2. use db
    mydb = myclient["qa"]
    # 3. use collection(table)
    mycol = mydb["job"]
    return mycol


def main():
    parse_html()


if __name__ == '__main__':
    main()
