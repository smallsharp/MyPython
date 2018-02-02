# encoding=utf-8
import cv2

"""
在OpenCV中，图像不是用常规的RGB颜色通道来存储的，它们用的是BGR顺序。当读取一幅图像后，默认的是BGR，不过有很多转换方式是可以利用的。
颜色空间转换可以用函数cvtColor()函数。比如，下面是一个转换为灰度图像
参考 http://blog.csdn.net/jningwei/article/details/77725559
"""
img = cv2.imread("test.jpg")

# 图片的高度和宽度
h, w = img.shape[:2]  # 300 533
scale = w / 200

# 缩放
resize_img = cv2.resize(img, (200, int(h / scale)), interpolation=cv2.INTER_NEAREST)

# 转成灰色图片
gray_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)

cv2.imshow("origin", img)
cv2.imshow("resize_img", resize_img)
cv2.imshow("gray_img", gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()