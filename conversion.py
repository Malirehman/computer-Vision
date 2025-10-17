import cv2

img = cv2.imread("jet.jpg")

# RGB → Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# RGB → HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("HSV", hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()
