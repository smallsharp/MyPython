import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException

# https://blog.csdn.net/weixin_39198406/article/details/81482082

try:
    response = requests.get("http://httpbin.org/get", timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    # 超时异常
    print('Timeout')
except ConnectionError:
    # 连接异常
    print('Connection error')
except RequestException:
    # 请求异常
    print('Error')
