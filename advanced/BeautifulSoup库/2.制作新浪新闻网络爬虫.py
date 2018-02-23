import requests
from bs4 import BeautifulSoup

res = requests.get("http://news.sina.com.cn/china")
res.encoding="utf-8"

soup = BeautifulSoup(res.text,"html.parser")

for news in soup.select(selector=".news-item"):
    print(len(news.select("h2")))
    print("-"*50)
    if len(news.select("h2"))>0:
        h2 = news.select("h2")[0].text
        a = news.select("a")[0]["href"]
        time = news.select(".time")[0].text
        # print(time,h2,a)

# newss = soup.select(".news-item")
# for news in newss:
#     if len(news.select("h2")) > 0:
#         h2 = news.select("h2")[0].text
#         a = news.select("a")[0]["href"]
#         time = news.select(".time")[0].text
#         print(time, h2, a)