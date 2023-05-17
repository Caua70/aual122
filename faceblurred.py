import os
import cv2

path = os.getcwd()

if os.path.isdir("haarcascade") == False:
    print("a pasta nao existe")
else:
    print("a pasta existe")

cascade = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")

def face_blur(gray, frame):
    faces = cascade.detectMultiScale(gray, 1.1,4)

    for x,y,w,h in faces:
        roi_frame = frame[y:y+h, x:x+w]
        blur = cv2.GaussianBlur(roi_frame, (101,101), 0)
        frame[y:y+h, x:x+w] = blur

    return frame 

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = face_blur(gray, frame)
    cv2.imshow("blurred video", blur)

    if cv2.waitKey(2) == 32:
        break

cv2.destroyAllWindows()
video.realese()