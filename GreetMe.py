import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")  # Fixed: was "ngine"
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set to the first voice
engine.setProperty("rate", 170)  # Set speech rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user based on the time of day
def greetme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning! How can I assist you today?")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon! How can I assist you today?")
    else:
        speak("Good evening! How can I assist you today?")
    speak("please tell me, how can i help you.")