# coding=utf-8
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

mtaidu = "https://m.taidu.com"

session = None

def initSession():
    """
    通过登录 获取session
    :return: session
    """
    global session
    if session == None:
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

def add2Cart():
    url = 'https://m.taidu.com/goodsSite/userDiy/saveDiyGoodsAndAddShopCart'
    params = {
        "skuniCode": "8006_8006100_10103",
        "productId": 8006,
        "goodsId": 7435,
        "goodsType": 2,
        "clientVersion": "3.0.3",
        "userId": "",
        "buyGoodsInfoVos": [{
            "number": 1,
            "productDetailCode": 8006100,
            "salePrice": 249,
            "skuGroup": "LEVEL,10103#OPTION,10001#SIZE,S"
        }],
        "mchCode": "#36227",
        "words": "[]",
        "imgUri": "[{\"matrix\":\"matrix(1 0 0 1 372 306)\",\"height\":309,\"maskX\":372,\"maskY\":306,\"width\":256,\"isSuit\":\"N\",\"id\":\"\",\"imgFlag\":1,\"url\":\"pre/model/2D/goodsSvgTemplate/20180508060554/7435/1/BA8702A2.png\"}]",
        "opusUri": "https://imgex.cmall.com/imgsrv/nospc/html5/Q2rHhzzfjE2018_5_14_13.png",
        "abbr": "CN",
        "clientType": "H5"
    }
    # headers = {'toKen':'c846416154d3fba69dfebc1558f'}
    # res = requests.post(url,json=params,headers=headers)
    res = requests.post(url,json=params,cookies=initSession().cookies)
    print(res.text)

def queryOrder():
    url = 'https://m.taidu.com/orderPaySite/tude/order/queryOrderList'
    params = {'pageSize': '100', 'currPage': '1', 'status': '0%2C21%2C22', 'clientType': 'H5', 'abbr': 'CN', 'clientVersion': '', 'sign': '2E269FE54CF9E1C08396EA94F056DEE9'}
    res = requests.post(url,params,cookies=initSession().cookies)
    print(res.text)


if __name__ == '__main__':
    for i in range(20):
        add2Cart()
        print(i)