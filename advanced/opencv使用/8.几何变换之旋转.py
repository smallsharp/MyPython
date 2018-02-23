#coding=utf-8

import cv2
import numpy as np


img = cv2.imread('ball.jpg',0)

h,w = img.shape

M = cv2.getRotationMatrix2D(center=(w/2,h/2),angle=45,scale=0.6) # 旋转的原点，旋转的角度，缩放的比例

dst = cv2.warpAffine(src=img,M=M,dsize=(w,h)) # 第三个参数是 输出图像的尺寸中心

cv2.imshow("img",img)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
