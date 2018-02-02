# coding=utf-8

"""
这是物体跟踪中 最简单的方法
常用的两个
cv2.COLOR_BGR2GRAY
cv2.COLOR_BGR2HSV
"""
import cv2
import numpy as np

# 列出所有可用的颜色标志
flags = [i for i in dir(cv2) if i.startswith("COLOR_")]

cap = cv2.VideoCapture(0)  # 获取摄像头
while (0):

    # 获取每一帧
    ret, frame = cap.read()

    # 转换到HSV
    hsv = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2HSV)

    # 设定蓝色的阈值
    lower_blue = np.array([110, 50, 50], dtype=np.uint8)
    upper_blue = np.array([130, 255, 255], dtype=np.uint8)

    # 根据阈值构建掩模
    mask = cv2.inRange(src=hsv, lowerb=lower_blue, upperb=upper_blue)

    # 对原图和掩模 进行位运算
    res = cv2.bitwise_and(src1=frame, src2=frame, mask=mask)

    # 显示图像
    # cv2.imshow('origin', frame)
    # cv2.imshow('mask', mask)
    # cv2.imshow('final', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()


"""
怎样获取要跟踪对象的HSV值
"""
# green = np.uint8([0.255,0])
green = np.uint8([[[0,255,0]]]) # 三层括号对应：cvArray,cvMat,IplImage
hsv_green = cv2.cvtColor(src=green,code=cv2.COLOR_BGR2HSV)
print(hsv_green)