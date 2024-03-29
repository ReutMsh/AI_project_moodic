from fer import FER
import cv2
from Enum import emotionEnum
from UserException import OpenCameraException

# region const variables
##############################
# constant parameters
MAX_FACES = 3

FRAME_WIDTH = 640
FRAME_HEIGHT = 480
MIN_AREA = 500


##############################
# endregion

# region get_expressed_emotion
def get_expressed_emotion():
    """
    Scanning and retrieving the users emotions and returning the dominant emotion the user expressed

    ~ Returns:
               A string containing the name of the chosen emotion.
    """
    expressed_emotions = get_dominant_emotions_from_camera()  # get a list that counts the expressed emotions

    index_biggest_emotion = -1
    counter_biggest_emotion = -1

    # finding the index of the emotion that was expressed the most
    for i in range(len(expressed_emotions)):
        if expressed_emotions[i] > counter_biggest_emotion:
            index_biggest_emotion = i
            counter_biggest_emotion = expressed_emotions[i]

    return emotionEnum(index_biggest_emotion).name  # the name of the most expressed emotion
# endregion

# region get_dominant_emotions_from_camera
def get_dominant_emotions_from_camera():
    """
    Accessing the camera feed of the device and extracting the emotions expressed in the feed.

    ~ Returns:
               A list of int. Each index represents an emotion.
               The value of an index represents the amount of times the user was caught expressing this emotion.
               The connection [index - emotion] uses the emotionEnum Enum class.
    """
    # accessing the camera feed and loading the emotion detection model
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier("emotion\haarcascade_frontalface_default.xml")

    count_dominant_emotion = [0, 0, 0, 0, 0, 0]
    count_faces = 0

    # capturing images from the camera feed, cropping the faces and classifying their emotion
    while count_faces < MAX_FACES:
        success, img = cap.read()  # take one frame from the video feed
        if success is False:
            raise OpenCameraException()

        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces_from_frame = face_cascade.detectMultiScale(imgGray, 2, 4)

        # classifying each face and adding the emotion to the counter
        for (x, y, w, h) in faces_from_frame:
            area = w * h
            if area > MIN_AREA:  # the face is big enough for emotion detection
                emt = extract_emotion_from_image(img[y:y + h, x:x + w])

                if emt is None or emt == "disgust":  # no relevant emotion was recognized
                    continue

                # increase the emotion counter and the face counter
                count_dominant_emotion[emotionEnum[emt].value] += 1
                count_faces += 1

    return count_dominant_emotion


# endregion

# region extract_emotion_from_image
def extract_emotion_from_image(img):
    """
    Finding an emotion that appears  in an image. Using a classification model provided by FER library
    ~ img: Object that will be scanned by the model to extract an emotion.

    ~ Return:
              String containing the dominant emotion that appears in the image

              ~ special values:
                * None - no emotion or face was detected. problem in detection
    """
    detector = FER()
    dominant_emotion, emotion_score = detector.top_emotion(img)
    return dominant_emotion
# endregion
