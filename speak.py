import webbrowser
import pyttsx3

engine = pyttsx3.init("sapi5")  # Fixed: was "ngine"
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set to the first voice
engine.setProperty("rate", 170)  # Set speech rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def open_url(url):
    """
    Open the specified URL in the default web browser.
    """
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    webbrowser.open(url)