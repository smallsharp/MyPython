'''
Created on 2017年9月27日
读取配置文件，配置文件中需要定义块，和字段
@author: cm
'''
from configparser import ConfigParser

# config = ConfigParser()
# config.read('ids.prop', encoding='utf-8')
# print(config.get('login', 'user'))
# print(config.get('logout', 'logoutId'))


class ReadConfig():

    def __init__(self, file):
        self.config = ConfigParser()
        self.config.read(file, encoding='utf-8')

    def getValue(self, key1, key2):
        '''
        :param key1: 块
        :param key2: Key
        :return: 块下，对应key的值
        '''
        return self.config.get(key1, key2)


# config = ReadConfig('ids.prop')
# print(config.getValue('login', 'user'))
# print(config.getValue('login', '名字'))
