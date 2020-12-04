import speech_recognition as sr
from gtts import gTTS
def speak(audio):
    engine=pyttsx3.init()
    engine.say(audio)
    engine.runAndWait
def take command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        audio = r.listen(source)
        text=""