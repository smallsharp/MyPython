import requests
from selenium import webdriver

# 您操作太频繁,请稍后再访问

def parse_html():
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput=py',
        'Cookie': '_ga=GA1.2.160313812.1552557462; user_trace_token=20190314175742-9bbb622d-463f-11e9-9551-5254005c3644; LGUID=20190314175742-9bbb6ae2-463f-11e9-9551-5254005c3644; index_location_city=%E4%B8%8A%E6%B5%B7; _gid=GA1.2.3286368.1554257468; JSESSIONID=ABAAABAAAFCAAEGDAF54D79FF179178C0E548D085E22519; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552558388,1552558429,1554257468,1554360140; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22169e71a9ee439d-0be5b86232086c-7a1b34-1327104-169e71a9ee677a%22%2C%22%24device_id%22%3A%22169e71a9ee439d-0be5b86232086c-7a1b34-1327104-169e71a9ee677a%22%7D; sajssdk_2015_cross_new_user=1; LG_LOGIN_USER_ID=6b8da8540651ea00a5209a895d8a2eda8bf096c3e7e9b122; _putrc=FD28266050045FF0; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B75133; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=f8ac8319f83f1282a3e0a3f7388fd3fa1ecd77882172d892; TG-TRACK-CODE=index_search; _gat=1; LGSID=20190404163847-109d4128-56b5-11e9-bd68-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3Fcity%3D%25E4%25B8%258A%25E6%25B5%25B7%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3Fcity%3D%25E4%25B8%258A%25E6%25B5%25B7%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; X_HTTP_TOKEN=40503342bf6c3d452837634551a4426bb7117694bc; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1554367383; LGRID=20190404164302-a8a44207-56b5-11e9-bd68-5254005c3644; SEARCH_ID=3325ed934cc54a67a795a2d407bf1e09'
    }
    data = {
        'first': 'true',
        'pn': 1,
        'kd': 'python'
    }
    response = requests.post(url, data=data, headers=headers, verify=False)
    response = response.json()
    print(response)
    return
    result = response['content']['positionResult']['result']

    for r in result:
        positionId = r['positionId']
        print(positionId)
        # parse_detail2(positionId)


def parse_detail2(positionId):
    driver = webdriver.Chrome()
    url = 'https://www.lagou.com/jobs/{}.html'.format(positionId)
    driver.get(url)


def main():
    parse_html()


if __name__ == '__main__':
    main()
