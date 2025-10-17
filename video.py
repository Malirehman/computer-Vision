import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Camera open nahi ho raha.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([86, 120, 70])
    upper_blue = np.array([125, 255, 255])
    #yoiu can change the color according to your need
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    red_detected = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Red Color Detection", red_detected)
    cv2.imshow("Live Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Camera closing...")
        break

cap.release()
cv2.destroyAllWindows()
print("Camera released successfully ")
