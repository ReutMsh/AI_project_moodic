from connect_emotion_to_spotify import emotion_to_song

#print(find_emotion.scanning_emotion())
print(emotion_to_song())
'''import cv2
import find_emotion
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



class emotionEnum(Enum):
    angry = 0
    disgust = 1
    fear = 2
    happy = 3
    neutral = 4 # TODO activate favorite songs
    sad = 5
    surprise = 6




def scanning_emotion():
    count_dominant = [0, 0, 0, 0, 0, 0, 0]
    while True:
        success, img = cap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray, 2, 4)
        for (x, y, w, h) in faces:  #TODO limit to the biggest face
            area = w * h
            if area > minArea:
                emt = emotion(img[y:y + h, x:x + w])
                if emt is None:
                    continue
                mt = emotionEnum[emt].value
                count_dominant[mt] += 1

        # cv2.imshow("Result", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return


scanning_emotion()

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
'''