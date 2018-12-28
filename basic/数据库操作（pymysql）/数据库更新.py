'''
Created on 2017年9月15日

@author: cm
'''
import pymysql
def update_table():
    
    db = pymysql.Connect("172.26.31.181","artsuser","artspassword","test")
    cursor = db.cursor()
    
    sql = "UPDATE EMPLOYEE SET AGE=AGE+1 WHERE SEX = %s"%'M'
    
    try:
        cursor.execute(sql)
        db.commit()
        print('update success')
    except Exception as e:
        print("error,%s"%e)