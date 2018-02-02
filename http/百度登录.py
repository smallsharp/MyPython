'''
Created on 2017年9月11日

@author: cm
'''
from urllib import request,parse

# post请求
def login_post():
    print("Login to baidu.com…")
    username = input("username:")
    password = input("password:")
    login_data = parse.urlencode([
        ('username',username),
        ('password',password),
        ('entry','mweibo'),
        ('client_id',''),
        ('savestate','1'),
        ('ec',''),
        ('Referer','http://i.baidu.com/welcome/')])
    
    req = request.Request('https://passport.baidu.com/v2/api/?login')
    req.add_header('Origin', 'http://i.baidu.com')
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
    with request.urlopen(req, data=login_data.encode('utf_8')) as f:
        print(f.status,f.reason)
        
        for k,v in f.getheaders():
            print(k,v)
#         print(f.read().decode('utf-8'))
        print(f.getcode())


# get请求
def getResponse():
    with request.urlopen("http://baidu.com") as f:
        data = f.read()
        print('status:%s %s'%(f.status,f.reason))
        for k,v in f.getheaders():
            print(k,v)
        print(data.decode('utf-8'))
    
def main():
#         login_post()
    getResponse()
        
        
if __name__=="__main__":
        main()