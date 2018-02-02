'''
Created on 2017年9月15日

@author: cm
'''
import pymysql

def create_table():
    # 测试ip
    db = pymysql.connect("172.26.31.181","artsuser","artspassword","test")
    
    # 使用db.cursor()方法，创建一个游标对象cursor
    cursor = db.cursor()
    
    # 执行sql，如果表存在就先删除
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    
    sql = """ create table EMPLOYEE(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT,
        CREATE_TIME DATETIME)"""
        
    try:
        cursor.execute(sql)
        print("Create Table Success!")
        
    except Exception as e:
        print("Failed,%s"%e)
    finally:
        db.close()

if __name__ =="__main__":
    create_table()        
        
        
        
        
        