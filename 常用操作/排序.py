rows = [
    {'element': '//*[@id="white-head"]/div/div[3]/div[2]/a[1]', 'operation': 'click', 'findmode': 'xpath',
     'data': '',
     'thinktime': '1', 'desc': '点击登录', 'sort': '1'},

    {'element': '//*[@id="app"]/div[1]/div[2]/div[1]/div/div/span[2]', 'operation': 'click',
     'findmode': 'xpath', 'data': '',
     'thinktime': '1', 'desc': '点击账号登录', 'sort': '2'},

    {'element': '//*[@id="app"]/div[1]/div[2]/div[1]/div/form[2]/div[1]/div/div[1]/input',
     'operation': 'sendkeys', 'findmode': 'xpath', 'data': '13344445555',
     'thinktime': '1', 'desc': '输入账号', 'sort': '3'},

    {'element': '//*[@id="app"]/div[1]/div[2]/div[1]/div/form[2]/div[2]/div/div/input',
     'operation': 'sendkeys', 'findmode': 'xpath', 'data': '123456',
     'thinktime': '1', 'desc': '输入密码', 'sort': '4'}
]

from operator import itemgetter

rows_by_sort = sorted(rows,key=itemgetter('sort'))
print(rows_by_sort)
