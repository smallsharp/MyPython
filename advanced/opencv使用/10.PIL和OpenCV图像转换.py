#encoding=utf-8
import cv2
from PIL import Image
import numpy

def pil2open():
    print("PIL.Image转换成OpenCV格式")
    image = Image.open("test.jpg")
    # image.show()
    img = cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2BGR)
    cv2.imshow("OpenCV", img)
    cv2.waitKey()

def open2pil():
    print("OpenCV转换成PIL.Image格式")
    img = cv2.imread("test.jpg")
    cv2.imshow("OpenCV", img)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    image.show()
    cv2.waitKey()


if __name__ == '__main__':
    open2pil()