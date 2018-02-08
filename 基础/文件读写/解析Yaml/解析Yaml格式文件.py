#-*- coding:utf-8 -*-

import yaml
import codecs


def getYam(path):
    print("getYam:",path)
    try:
        with open(path, encoding='utf-8') as f:
            file_content = yaml.load(f)
            print("file_content:",file_content)
            return file_content
    except FileNotFoundError:
        print(u"找不到文件")

if __name__ == "__main__":

    # 打开文件
    file = open('testYaml.yaml',encoding='utf-8')

    # 解析yaml内容
    content= yaml.load(file)
    print(content)
    file.close()

    # 解析具体的值
    print(content['testinfo'])
    print(content['testinfo'][0])
    print(content['testinfo'][0]['id'])

    # 使用get获取key
    print(content['testinfo'][0].get('id'))