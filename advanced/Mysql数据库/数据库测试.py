'''
Created on 2017年11月28日

@author: cm
'''
from 基础知识.数据库操作.MysqlUtil import MysqlHelper


db1 = MysqlHelper(host='10.24.194.171', user='artsuser', password='artspassword', database='product', charset='utf8')

sql = '''SELECT model_style_id,photo_url,cip_url,photo_type,updated_date
      FROM tb_model_goods_picture_box WHERE
      model_style_id = (SELECT id from tb_model_goods_template_style where goods_id = %s)'''

# print(db1.find(sql, "3275"))
results = db1.runQuery(sql, "3275")

for result in results:
    
    print(result)
#     print(type(result))
    for r in result:
        pass
#         print(r)

