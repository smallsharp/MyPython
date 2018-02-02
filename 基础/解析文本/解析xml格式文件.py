'''
Created on 2017年11月28日
解析xml格式数据
@author: cm
'''
import  xml.dom.minidom

def parseXml():
    dom = xml.dom.minidom.parse('./content.svg')
        
    # 得到文档元素对象
    root = dom.documentElement
#     print (root.nodeName)
#     print(root.nodeValue)
#     print(root.nodeType)
#     print(root.ELEMENT_NODE)    
    imagelist = root.getElementsByTagName("image")
    for image in imagelist:
        print('id:',image.getAttribute("id"))
        print('width:',image.getAttribute("width"))
        print('height:',image.getAttribute("height"))
        print('href:',image.getAttribute("xlink:href"))
        print("-"*50)
       
if __name__ == '__main__':
    parseXml()
