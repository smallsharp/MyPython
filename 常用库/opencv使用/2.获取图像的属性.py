# encoding=utf-8
import cv2

img = cv2.imread("test.jpg") # 返回的图像矩阵

# 图像像素总数目
imgSize = img.size
print(imgSize)

# 图像数据类型
type = img.dtype
print(type)

# 返回图像高（图像矩阵的行数）、宽（图像矩阵的列数）和通道数3个属性组成的元组，若图像是非彩色图，则只返回高和宽组成的元组。
w,h,r = img.shape # (300, 533, 3) ,分别对应图片的宽度，高度 和 通道数
print(w,h,r)