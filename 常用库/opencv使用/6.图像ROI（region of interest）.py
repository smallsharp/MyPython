# coding=utf-8

import cv2
import numpy as np

img = cv2.imread("./ball.jpg")

ball = img[330:390, 220:290]  # 球坐在的矩阵，高度(y坐标范围)，宽度（x坐标范围）
print(ball)
img[330:390, 40:110] = ball # 替换到图其他矩阵

cv2.imshow("new", img)

cv2.waitKey()
cv2.destroyAllWindows()
