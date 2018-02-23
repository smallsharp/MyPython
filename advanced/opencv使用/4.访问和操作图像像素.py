# encoding=utf-8

import cv2


# OpenCV中图像矩阵的顺序是B、G、R。可以直接通过坐标位置访问和操作图像像素。

img = cv2.imread("test.jpg")

# 图片的坐标
numb = img[50, 100]
print(numb) # [28 70 93]

# 修改坐标的色值
# img[50, 100] = (0, 0, 0) # B=0,G=0,R=0
# cv2.imshow("img", img)
# cv2.waitKey()


# 更改图像某一矩形区域的像素值
img[0:10, 0:100, 0] = 255
img[100:200, 100:200, 1] = 255
img[200:300, 200:300, 2] = 255

cv2.imshow("img", img)

cv2.waitKey()