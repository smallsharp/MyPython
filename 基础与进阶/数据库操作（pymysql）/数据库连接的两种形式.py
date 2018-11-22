import pymysql.cursors

config = {
    'host': '192.168.40.32',
    'port': 3306,
    'user': 'dbdev',
    'password': '123456',
    'db': 'saas',
    'charset': 'utf8',
    # 'cursorclass': pymysql.cursors.DictCursor,
}
dbSaas = pymysql.connect(**config)
cursorSaas = dbSaas.cursor()
print('connect saas db now！')

config2 = {
    'host': '192.168.40.32',
    'port': 3306,
    'user': 'dbdev',
    'password': '123456',
    'db': 'saas_cost',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor  # 查询到的数据，以Dict格式返回
}

# dbCost = pymysql.connect(host='192.168.40.32', user='dbdev', password='123456', database='saas_cost')

dbCost = pymysql.connect(**config2)
cursorCost = dbCost.cursor()
print('connect saas cost db now！')


def getCompanys(appId, year):
    '''
    获取收入前10的公司id
    :param appId: 公司ID
    :param year: 年份
    :return: 公司对应的客户ID集合
    '''
    sql = '''
        SELECT
            companyId
        FROM
            bill
        WHERE
            appId = %s
        AND billType = 1
        AND isDel = 1
        AND `year` = %s
        AND `status` IN (1, 2, 3)
        AND companyId > 0
        GROUP BY
            companyId
        ORDER BY SUM(totalMoneyE2) DESC
        LIMIT 10;
            '''
    cursorCost.execute(sql, (appId, year))
    data = cursorCost.fetchall()
    print(data)
    companys = [i['companyId'] for i in data]
    return companys


# print(getCompanys(2683, 2018))
