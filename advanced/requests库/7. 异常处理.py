import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException


try:
   response = requests.get("http://httpbin.org/get", timeout = 0.5)
           print(response.status_code)
except ReadTimeout:
   # ��ʱ�쳣
   print('Timeout')
except ConnectionError:
   # �����쳣
   print('Connection error')
except RequestException:
   # �����쳣
   print('Error')