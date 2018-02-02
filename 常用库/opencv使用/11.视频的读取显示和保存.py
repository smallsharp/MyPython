#encoding=utf-8
import numpy as np
import cv2

cap = cv2.VideoCapture(0) # 0表示设备内置摄像头

# 检查摄像头是否初始化成功
if cap.isOpened(): # 如果未成功，使用cap.open()
    while(True):
        # Capture frame by frame
        ret,frame = cap.read()
        # print(ret,frame)

        # print(cap.get(3),cap.get(4)) # 显示每一帧的宽和高
        ret = cap.set(3,320) # 显示的宽改为 320
        ret = cap.set(4,240) # 显示的高改为 240

        # operation on frame
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        # display the resulting frameq
        cv2.imshow("frame",gray)
        if cv2.waitKey(1)==ord('q'):
            break

# release the capture
cap.release()
cv2.destroyAllWindows()