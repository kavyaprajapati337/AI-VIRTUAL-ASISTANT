import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set to the first voice
engine.setProperty("rate", 170)  # Set speech rate

# Function to speak text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    # Try to recognize the speech
    try:
        print("understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int ((datetime.now()+timedelta(minutes=2)).strftime("%M"))

def SendMessage():
    speak("who do you wnat to message")
    a = int(input('''person 1 - 1
              person 2 - 2'''))
    if a==1:
        speak ("what's the message")
        message = str(input("Enter the message :"))
        pywhatkit.Sendwhatmsg("+910000000000", message, time_hour=strTime, time_min=update)
    elif a==2:
        pass