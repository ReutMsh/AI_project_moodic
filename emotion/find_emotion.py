from fer import FER


def scanning_emotion():
    # Our code #
    return


def emotion(img):
    detector = FER()
    dominant_emotion, emotion_score = detector.top_emotion(img)
    return dominant_emotion
