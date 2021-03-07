import pyttsx3

def speak_text(text, shouldPrint=True):
    engine = pyttsx3.init()

    if (shouldPrint):
        print(text)

    engine.say(text)
    engine.runAndWait()
