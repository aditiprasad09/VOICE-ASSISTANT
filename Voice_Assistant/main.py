import pyttsx3 as p

import speech_recognition as sr


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()

speak("hello aditi prasad..")

speak("hope you are having a nice day.")

speak("and i'm your python voice assistant..")

speak("I can read your commands easily.")

speak("And I can also read out your commands in my own voice.")
