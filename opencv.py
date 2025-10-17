import cv2

img = cv2.imread("jet.jpg")


resized_img = cv2.resize(img, (400,300))


gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)




cv2.imshow("jets", img)
cv2.imshow("resized", resized_img)
cv2.imshow("gray", gray_img)

cv2.waitKey(0)

cv2.destroyAllWindows()