
def emotion_to_song():
    emotion = scanning_emotion()
    match emotion:
        case 'angry':
            return "שירים מרגיעים"
        case 'disgust':
            return
        case 'fear':
            return
        case 'happy':
            return "שירים שמחים"
        case 'neutral':
            return
        case 'sad':
            return "שירים שמחים"
        case 'surprise':
            return "שירים "
