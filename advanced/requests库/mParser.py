'''
Created on 2017年9月27日
读取配置文件，配置文件中需要定义块，和字段
@author: cm
'''
from configparser import ConfigParser


config = ConfigParser()


def parser(file,encoding='utf-8'):
    dictF = dict()
    config.read(file,encoding)

    print(config.get("Server","host_ios"))

    # 返回所有区块名称
    print(config.sections())

    # 返回Server下的所有数据
    print(config.items('Server'))

    # 返回Server区块下的 所有key
    print(config.options('Server'))


if __name__ == '__main__':
    parser("interface.prop")