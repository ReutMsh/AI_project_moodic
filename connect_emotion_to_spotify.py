from emotion.find_emotion import scanning_emotion


'''return string to search and the emotion'''
def emotion_to_song(emotion):
    match emotion:
        case 'angry':
            return "שירים מרגיעים"
        case 'disgust':
            return "שירים כשאתה נגעל"
        case 'fear':
            return "שירים כשאתה מפחד"
        case 'happy':
            return "שירים שמחים"
        case 'neutral':
            return "שירים טבעיים"
        case 'sad':
            return "שירים משמחים"
        case 'surprise':
            return "שירים מפתיעים"
