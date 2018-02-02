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
    file.close()

    print(content)
    print(content['testinfo'])
    print(content['testinfo'][0])


    print(content['testinfo'][0]['id'])

    # 使用get获取key
    print(content['testinfo'][0].get('id'))

    # print("python yaml基本示例")
    # fp = codecs.open("testYaml.yaml", "r", "utf-8")
    # document = fp.read()
    # fp.close()
    #
    # # 将yaml格式内容 转换成 dict类型
    # load = yaml.load_all(document)
    #
    # # 遍历迭代器
    # for data in load:
    #     print(type(data))
    #     print(data)
    #
    #     print("---" * 25)
    #     # 将python对象转换成为yaml格式文档
    #     output = yaml.dump(data)
    #     print(type(output))
    #     print(output)