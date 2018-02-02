#coding=utf-8


import numpy as np
import cv2

img = cv2.imread("test.jpg")

h,w,c = img.shape

M = np.float32([[1,0,100],[0,1,50]])

dst = cv2.warpAffine(src=img,M=M,dsize=(w,h))

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()