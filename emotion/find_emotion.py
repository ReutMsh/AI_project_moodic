from fer import FER

def emotion(img):
    detector = FER()
    dominant_emotion, emotion_score = detector.top_emotion(img)
    return dominant_emotion
