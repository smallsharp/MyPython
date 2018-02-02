'''
Created on 2017年9月15日

@author: cm
'''

import pymysql
import datetime

def insert_record():
    db = pymysql.Connect("172.26.31.181","artsuser","artspassword","test")
    cursor = db.cursor()
    
    sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME,"\
        "CREATE_TIME) VALUES('%s','%s','%d','%c','%d','%s')"\
        %('xiao','zhi',22,'M',20000,datetime.datetime.now())
    
    try:
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("insert success")
        
    except Exception as e:
        print("insert failed,%s"%e)
        # 如果发生异常，执行回滚
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()
if __name__ == '__main__':
    insert_record()
    
    