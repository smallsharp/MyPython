from pymongo import MongoClient
from dateutil.relativedelta import relativedelta
from datetime import datetime

# client = MongoClient()
# client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://192.168.40.32:27017/')

# 资产表
ASSETS_SAAS = 'assets_saas'

# 资产核销
ASSET_CHECKLOG_SAAS = 'assetCheckLog_saas'

# 负债表
LIABILITY_SAAS = 'liability_saas'

# 还款计划
REPAYMENT_LOAN_SAAS = 'repaymentLoan_saas'

# 负债核销
LIABILITY_CHECKLOG_SAAS = 'liabilityCheckLog_saas'


def connectMongo():
    client = MongoClient('mongodb://192.168.40.32:27017/')  # 连接Mongo服务
    db = client['leili_admin']  # 选择指定库
    return db


def connTable(table):
    '''
    连接库中的表
    :param table:
    :return:
    '''
    db = connectMongo()
    conn = db[table]
    return conn
