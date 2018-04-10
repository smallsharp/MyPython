# coding=utf-8
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

mtaidu = "https://m.taidu.com"


def initSession():
    """
    通过登录 获取session
    :return: session
    """
    url = "{}/memberSite/sso/loginJson?loginAccount=18521035133&password=111111&code=&rememberMe=1&clientType=H5&abbr=CN&clientVersion=".format(
        mtaidu)
    session = requests.Session()
    # session.close()
    # requests.adapters.DEFAULT_RETRIES = 5
    session.get(url)
    return session


def productList():
    url = "{}/goodsSite/home/categoryProductList?abbr=CN&clientType=H5&clientVersion=".format(mtaidu)
    res = requests.get(url)
    res = res.json()
    if res['code'] == '200' and len(res['result']) > 0:
        categoryList = []
        category = {}
        for r in res['result']:
            category['categoryName'] = r['categoryName']
            category['categroyCode'] = r['categroyCode']
            category['imagePath'] = r['imagePath']
            categoryList.append(category)
    else:
        print("Error", url)
    return categoryList


def goodsList(category):
    url = "{}/goodsSite/home/categoryGoodsList?abbr=CN&categoryCode={}&clientType=H5&clientVersion=".format(mtaidu,category['categroyCode'])
    res = requests.get(url)
    res = res.json()
    if res['code'] == '200' and len(res['result']) > 0:
        goodsInfo = []
        goodsInfoList = []
        for r in res['result']:
            # print(r)
            goodsInfo.append()



def main():
    # initSession()
    for product in productList():
        goodsList(product)


if __name__ == '__main__':
    main()
