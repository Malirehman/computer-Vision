# sabse pehlay ham opencv ko import krte hai
import cv2

# iske baad haarcascade code ko load  karte hai
# ik variable ma jese k face_cascade may be
face_casecade = cv2.CascadeClassifier(
    r"C:\\Users\\auonp\\OneDrive\\Desktop\\real time face detection\\haarcascade_frontalface_default.xml"
)
# face_casecade variable ab object ban gaya hai 
# CascadeClassifier ab ik function hai jo xml ko load karta hai

# ab ham video recording start karte hai
web = cv2.VideoCapture(0)
# (0) ka matlab hai laptop ka primary camera use karna

# ab ham loop lagaenge thakay har waqt on rahe jab tak quit na kare
while True:
    succes, frames = web.read()
    # succes ka matlab hai boolean store karta hai (True/False)
    # frames har frame ka data hota hai (image)
    # q k web.read() do cheezein return karta hai

    # ---------------------------------------
    # ab ham har frame ko gray ma convert karte hai
    # thaky detection fast ho
    gray_img = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    # ab faces detect karenge face_casecade se
    # ye object apne functions ke zarye detection karega
    faces = face_casecade.detectMultiScale(gray_img)
    # detectMultiScale ik function hai jo face_casecade ke pass hota hai
    # ye har detected face ke liye x, y, w, h values return karta hai
    # jo ham faces variable ma store karte hain

    # ---------------------------------------
    # ab ham rectangle draw karenge har detected face ke around
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 255, 0), 10)

    # ab ham screen per show karenge
    cv2.imshow("real time detection", frames)

    key = cv2.waitKey(1) & 0xFF
    # waitKey ke baghair loop kabhi end nahi hoga
    # ye 1 millisecond tak wait karega jab tak ham koi key press na kare
    # & 0xFF likhne se key value sahi detect hoti hai

    if key == ord('q'):  
        # agar user 'q' press kare to loop break
        break

# jab loop se bahar aao to camera band kar do
web.release()

# aur OpenCV ki sari windows close kar do
cv2.destroyAllWindows()
