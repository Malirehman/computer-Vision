import cv2
import  numpy as np


#ye hamne blank image create kiya hai
img = np.zeros((600,600,3),dtype=np.uint8)

cv2.line(img,(10,20), (300,400),(0,255,0),3)

cv2.rectangle(img,(100,100),(400,400),(255,0,0),3)


# Circle draw karo (center, radius, color, thickness)
cv2.circle(img, (300, 300), 50, (0, 0, 255), -1)  # -1 = filled circle

cv2.putText(img, "BMW", (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

cv2.imshow("shapes",img)
cv2.waitKey(0)
cv2.destroyAllWindows()