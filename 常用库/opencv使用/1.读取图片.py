# encoding=utf-8
import cv2
import numpy

"""
读取图片：cv2.imread()
第一个参数：图片路径
第二个参数：可选，cv2.IMREAD_UNCHANGED(包含alpha通道)，cv2.IMREAD_GRAYSCALE(灰度模式) 等

显示图片：cv2.imshow()
第一个参数：窗口的名字
第二个参数：要显示的图片对象

"""
img = cv2.imread("./test.jpg",cv2.IMREAD_GRAYSCALE) # 灰度图

# print(img.shape) # (1920, 1080, 3)
# print(img.shape[0]) # 图片的高度
# print(img.shape[1]) # 图片的宽度
# print(img.shape[2]) # 图片的通道数，如RGB为3通道，RGBA为4通道

# 打印图像尺寸
h, w = img.shape[:2] # 图片的高度和宽度

cv2.namedWindow("image",cv2.WINDOW_NORMAL) # 可调整窗口大小
cv2.imshow("image", img)

# 保存原jpg格式的图像为png格式图像
cv2.imwrite("./test_new.png", img)

# 键盘绑定函数
cv2.waitKey()
# 释放窗口
cv2.destroyAllWindows()