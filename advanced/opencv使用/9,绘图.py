#coding=utf-8


import numpy as np
import cv2


# create a black image
img = np.zeros((512,512,3),np.uint8)

"""
画线
"""
# draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(512,512),(255,0,0),5) # 图片，起点，重点，颜色，粗细

"""
画矩形
"""
cv2.rectangle(img=img,pt1=(384,0),pt2=(510,128),color=(0,255,0),thickness=2) # 左上角顶点和右下角顶点

"""
画圆形
"""
cv2.circle(img=img,center=(447,63),radius=63,color=(0,0,255),thickness=-1) # 指定圆形的中心点坐标 和 半径

"""
画椭圆
"""
# 中心点坐标，长轴和短轴的长度，椭圆沿逆时针旋转的角度
cv2.ellipse(img=img,center=(256,256),axes=(100,50),angle=0,startAngle=0,endAngle=180,color=100,thickness=-1)


"""
在图片上添加文字
绘制的文字，位置，字体，大小，粗细
"""
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img=img,text='OpenCV',org=(10,500),fontFace=font,fontScale=4,color=(255,255,2),thickness=2)


cv2.imshow("line",img)
cv2.waitKey()
cv2.destroyAllWindows()