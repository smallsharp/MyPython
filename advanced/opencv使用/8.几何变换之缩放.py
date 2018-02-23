#coding=utf-8

import cv2
import numpy as np


img = cv2.imread('ball.jpg')


# dsize指输出图像的尺寸，由于设置了缩放因子fx,fy,所以这里为None
res = cv2.resize(src=img,dsize=None,fx=0.8,fy=0.8,interpolation=cv2.INTER_CUBIC)

# 或者 直接设置dsize,就不需要设置缩放因子
# h,w = img.shape[:2]
# res = cv2.resize(src=img,dsize=(2*w,2*h),interpolation=cv2.INTER_CUBIC)

while 1:
    cv2.imshow("res",res)
    cv2.imshow("img",img)
    if cv2.waitKey(1)&0xFF==27:
        break
cv2.destroyAllWindows()
