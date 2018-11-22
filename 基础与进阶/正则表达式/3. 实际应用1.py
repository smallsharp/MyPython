#coding=utf-8
import re

# field = 'do it now, do right now'
# print(field.replace('do', 'Just do'))
# print(field.replace('o', 'Just',1))
# print(field.replace('o', 'Just',2))
# print(field)

xml = '''
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="1000px" height="1250px" viewbox="0 0 1000 1250" style="enable-background:new 0 0 1000 1250;" xml:space="preserve">
    <g id="bg_xA0__1_">
        <image style="overflow:visible;" width="1000" height="1250" id="bg_xA0_" xlink:href="http://image.Python.com/imgsrv/pre/model/2D/goodsSvgTemplate/20171201081212/3361/1/AFECB667.jpg" />
    </g>
    <g xmlns="http://www.w3.org/2000/svg" fill="#000" id="frame_0000" stroke-width="0" mask="url(#frame_0000_mask3361)" transform="">
        <g xmlns="http://www.w3.org/2000/svg" fill="#000" id="frame_0000_face" stroke-width="0" transform="">
            <mask xmlns="http://www.w3.org/2000/svg" fill="#000" id="frame_0000_mask3361" stroke-width="0" transform="">
                <image style="overflow:visible;" width="161" height="161" id="p-1_xA0_" xlink:href="http://image.Python.com/imgsrv/pre/model/2D/goodsSvgTemplate/20171201081212/3361/1/AFECB665.png" transform="matrix(1 0 0 1 420 494)" />
            </mask>
            <image style="overflow:visible;" width="161" height="161" id="z-1_xA0_" xlink:href="http://image.Python.com/imgsrv/pre/model/2D/goodsSvgTemplate/20171201081212/3361/1/AFECB66B.png" transform="matrix(1 0 0 1 420 494)" />
        </g>
    </g>
    <g id="d-1_xA0__1_">
        <image style="overflow:visible;" width="101" height="26" id="d-1_xA0_" xlink:href="http://image.Python.com/imgsrv/pre/model/2D/goodsSvgTemplate/20171201081212/3361/1/AFECB66D.png" transform="matrix(1 0 0 1 454 617)" />
    </g>
</svg>
'''
list1 = re.findall(r'http:.*[jpn]g', xml)  # 匹配出所有的图片
print(list1)

list2 = re.findall(r"id=\"(.{6,7}_)\"", xml)  # 匹配出所有的id
print(list2)

list3 = re.findall(r"width=\"(\d{2,5})\"\sh", xml)  # 匹配出所有的width
print(list3)

list4 = re.findall("height=\"(\d*)\"", xml)  # 匹配出所有的height
print(list4)

dictlist = []
for i in range(4):
    dict1 = {}
    dict1['id'] = list2[i]
    dict1['width'] = list3[i]
    dict1['height'] = list4[i]
    dict1['url'] = list1[i]
    dictlist.append(dict1)
print(dictlist)













