

import pymysql
from urllib import request
import urllib

def getModelList():
    # 预发布
    db = pymysql.Connect("10.24.194.171","artsuser","artspassword","product")
    cursor = db.cursor()
    sql = "select product_id,model_name,product_name from tb_model where state = 1 ORDER BY product_id asc"
    
    try:
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()      
    except Exception as e:
        print("error:%s"%e)
    finally:
        db.close()
        
    return results

def getRes():
    models = getModelList()
    print(len(models))
    prefix_image = "http://image.Python.com/imgsrv/"
    prefix_imgex = ""
    prefix_img00 = ""
    for r in models:
        url = prefix_image + "stag/model/upload/%s/%s.DAE"%(r[1],r[1])
        try:
            models = urllib.request.urlopen(url)
            print("正常的：",url,models.getcode())
        except Exception: 
            print("异常的：",url)
    print("访问完毕！")
        
if __name__ == '__main__':
    getRes()