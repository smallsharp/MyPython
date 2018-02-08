'''
Created on 2017年9月27日
读取配置文件，配置文件中需要定义块，和字段
@author: cm
'''
from configparser import ConfigParser


config = ConfigParser()
config.read('ids.prop', encoding='utf-8')
print(config.get('login', 'user'))
print(config.get('logout', 'logoutId'))