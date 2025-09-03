import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import wikipedia  # Fixed: was "wekipedia"
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set to the first voice
engine.setProperty("rate", 170)  # Set speech rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to take voice commands
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
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

# Function to search Google, YouTube, and Wikipedia
def search_google(query):
    if "google" in query:
        query = query.replace("Buddy", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        query = query.strip()
        speak("This is what I found on google")

        # Try to search on Google
        try:
            kit.search(query)
            result = wikipedia.summary(query, sentences=1)  # Fixed: was googleScrap
            speak(result)
        except:
            speak("Sorry, I couldn't find any information on that topic.")

# Function to search YouTube
def searchyoutube(query):
    if "youtube" in query:
        speak("This is what I found on YouTube")
        query = query.replace("Buddy", "")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.strip()
        try:
            kit.playonyt(query)
            speak("Playing on YouTube")
        except:
            speak("Sorry, I couldn't play that on YouTube.")

# Function to search Wikipedia
def search_wikipedia(query):  # Fixed: was "searchwikipedia"
    if "wikipedia" in query:
        speak("This is what I found on Wikipedia")
        query = query.replace("Buddy", "")
        query = query.replace("wikipedia search", "")
        query = query.replace("wikipedia", "")
        query = query.strip()
        try:
            result = wikipedia.summary(query, sentences=2)  # Fixed: now stores result
            speak(result)  # Fixed: now actually speaks the result
        except:
            speak("Sorry, I couldn't find that on Wikipedia.")