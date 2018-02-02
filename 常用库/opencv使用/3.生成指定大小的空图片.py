#encoding=utf-8
import cv2
import numpy as np

img = cv2.imread("test.jpg")
# print(img) # 图像矩阵

# 返回图像高（图像矩阵的行数）、宽（图像矩阵的列数）和通道数3个属性组成的元组，若图像是非彩色图，则只返回高和宽组成的元组。
print(img.shape)
w,h = img.shape[:2]

# 原图等大的空图 shape : int or sequence of ints Shape of the new array, e.g., ``(2, 3)`` or ``2``.
imgZero = np.zeros(img.shape, np.uint8)

# 原图2倍大的空图
imgFix = np.zeros((w*2, h*2, 3), np.uint8)

# cv2.imshow("img", img)
# cv2.imshow("imgZero", imgZero)
# cv2.imshow("imgFix", imgFix)
cv2.waitKey()


