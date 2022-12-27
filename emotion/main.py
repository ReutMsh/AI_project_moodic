import cv2
from find_emotion import emotion
##############################
frameWidth = 640
frameHeight = 480
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
minArea = 500
color = (255,0,255)
##############################
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 2, 4)
    for (x, y, w, h) in faces:
        area = w*h
        if area > minArea:
            #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, emotion(img[y:y+h, x:x+w]), (x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1, color, 2)
            #imgRoi = img[y:y+h, x:x+w]
            #cv2.imshow("ROI", imgRoi)

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break