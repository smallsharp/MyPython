from advanced.MongoDB import mongoService
import datetime
from dateutil.relativedelta import relativedelta

now = datetime.datetime.now()
one_year_ago = (now + relativedelta(years=-1)).timestamp()
asset = mongoService.connTable('assets_saas')  # 资产表

# 1. 查询
rows = asset.find({'appId': '2683', 'buyTheYear': {'$gte': one_year_ago, '$lte': now.timestamp()}})

print(list(rows))
