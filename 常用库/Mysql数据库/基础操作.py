'''
Created on 2017年11月28日

@author: cm
'''
import pymysql as ps

# 打开数据库连接
db = ps.connect(host='10.24.194.171', user='artsuser', password='artspassword', database='product', charset='utf8')

# 创建一个游标对象
cur = db.cursor()

# 参数化处理
# sql = "INSERT INTO USER(NAME,PASSWORD) VALUES(%s,%s)"
sql = "select * from tb_model where gray_img = %s"

# 执行sql
cur.execute(sql, 1)

# 获取结果集
result = cur.fetchall()

print("OK")
print(result)

# 提交事务(update等操作需要执行)
db.commit()

# 关闭游标
cur.close()

# 关闭数据库连接
db.close()