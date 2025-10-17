import cv2

import numpy as np


img = cv2.imread("red.jpg")

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

Lower_red = np.array([20,120,0])
Upper_red = np.array([30,255,255])

mask1 = cv2.inRange(hsv,Lower_red,Upper_red)
cv2.imshow("mask1",mask1)

red_detect = cv2.bitwise_and(img,img,mask=mask1)

cv2.imshow("image",img)
cv2.imshow("red",red_detect)
cv2.waitKey(0)
cv2.destroyAllWindows()