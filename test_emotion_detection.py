from emotion_detection import emotion_detector

def test_emotion_detector():
    text = "I am really mad about this"
    result = emotion_detector(text)

    print("Emotion Detector Test:")
    print(result)

if __name__ == "__main__":
    test_emotion_detector()