'''
Created on 2017年9月15日

@author: cm
'''
import pymysql

def query():
    db = pymysql.Connect("172.26.31.181","artsuser","artspassword","test")
    cursor = db.cursor()
    sql = "SELECT * FROM EMPLOYEE WHERE INCOME>%d"%10000
    try:
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            create_time = row[5]
            print(fname,lname,age,sex,income,create_time)
    except Exception as e:
        print("error:%s"%e)
    finally:
        db.close()
if __name__ == '__main__':
    query()