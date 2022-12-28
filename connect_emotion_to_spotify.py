from emotion.find_emotion import scanning_emotion


'''return string to search and the emotion'''
def emotion_to_song():
    emotion = scanning_emotion()
    match emotion:
        case 'angry':
            return "שירים מרגיעים", 'angry'
        case 'disgust':
            return "שירים כשאתה נגעל", 'disgust'
        case 'fear':
            return "שירים כשאתה מפחד", 'fear'
        case 'happy':
            return "שירים שמחים", 'happy'
        case 'neutral':
            return "שירים טבעיים", 'neutral'
        case 'sad':
            return "שירים משמחים", 'sad'
        case 'surprise':
            return "שירים מפתיעים", 'surprise'
