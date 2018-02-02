'''
Created on 2017年9月26日

@author: cm
'''
import difflib
text1 = """
pid logs/nginx.pid;
 
events {
use epoll;
worker_connections 2048;
}
 
http {
include mime.types;
default_type application/octet-stream;
 
server {
listen 80;
server_name itoatest.example.com;
root /apps/oaapp;}
 
charset utf-8;
access_log logs/host.access.log main;}
"""
 
text2 = """
pid logs/nginx.pid;
 
events {
use epoll;
worker_connections 2000;
}
 
http {
include mime.types;
default_type application/octet-stream;}
 
server {
listen 80;
server_name itoatest.example.com;
root /apps/oaapp;}
"""
lines1 = text1.splitlines() #以行进行分割

lines2 = text2.splitlines()
 
d = difflib.Differ() #创建Differ对象
diff = d.compare(lines1,lines2)
# print('\n'.join(list(diff)))

d = difflib.HtmlDiff()
# print(d.make_file(lines1,lines2))