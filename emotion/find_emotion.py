from fer import FER
import cv2
import Enum

MAX_FACES = 10

##############################
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
minArea = 500  # TODO change to uppercase
color = (255,0,255)

def general():
    emotions = scanning_emotion()
    biggest_index = -1
    biggest = -1
    for i in range(len(emotions)):
        if emotions[i] > biggest:
            biggest_index = i
            biggest = emotions[i]
    return biggest_index # TODO convert to emotion enum


'''gets the image and returns a counter for the emotions the camera scanned'''
def scanning_emotion():
    cap = cv2.VideoCapture(0)
    cap.set(3, FRAME_WIDTH)
    cap.set(4, FRAME_HEIGHT)
    cap.set(10, 150)

    count_dominant = [0, 0, 0, 0, 0, 0, 0]
    count_faces = 0
    while count_faces < MAX_FACES:
        success, img = cap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray, 2, 4)
        for (x, y, w, h) in faces:  #TODO limit to the biggest face
            count_faces += 1
            area = w * h
            if area > minArea:
                emt = emotion(img[y:y + h, x:x + w])
                if emt is None:
                    continue
                mt = Enum.emotionEnum[emt].value
                count_dominant[mt] += 1
    return count_dominant


def emotion(img):
    detector = FER()
    dominant_emotion, emotion_score = detector.top_emotion(img)
    return dominant_emotion

'''
func 1 - in charge of all the action and returning the chosen emotion.

func 1.1 - creating an array of emotions 
func 1.2 - calculate the dominant emotion
'''
