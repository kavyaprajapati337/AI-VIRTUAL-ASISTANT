import webbrowser
import pyautogui
from speak import speak
from pynput.keyboard import Controller
keyboard = Controller()
import pyttsx3

engine = pyttsx3.init("sapi5")  # Fixed: was "ngine"
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set to the first voice
engine.setProperty("rate", 170)  # Set speech rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to open applications or websites based on voice commands
def web_functions(query):
    # open any website with www or without www
    if "open" in query:
        query = query.replace("open", "").strip()
        if "www" in query:
            webbrowser.open(f"http://{query}")
        elif "." in query:
            webbrowser.open(f"http://{query}")
        elif "youtube" in query:
            query = query.replace("youtube", "").strip()
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        elif "google" in query:
            query = query.replace("google", "").strip()
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif "facebook" in query:
            query = query.replace("facebook", "").strip()
            webbrowser.open(f"https://www.facebook.com/{query}")
        elif "twitter" in query:
            query = query.replace("twitter", "").strip()
            webbrowser.open(f"https://www.twitter.com/{query}")
        elif "instagram" in query:
            query = query.replace("instagram", "").strip()
            webbrowser.open(f"https://www.instagram.com/{query}")
        elif "linkedin" in query:
            query = query.replace("linkedin", "").strip()
            webbrowser.open(f"https://www.linkedin.com/in/{query}")
        elif "github" in query:
            query = query.replace("github", "").strip()
            webbrowser.open(f"https://www.github.com/{query}")
        elif "stackoverflow" in query:
            query = query.replace("stackoverflow", "").strip()
            webbrowser.open(f"https://stackoverflow.com/search?q={query}")
        elif "reddit" in query:
            query = query.replace("reddit", "").strip()
            webbrowser.open(f"https://www.reddit.com/r/{query}")
        elif "quora" in query:
            query = query.replace("quora", "").strip()
            webbrowser.open(f"https://www.quora.com/search?q={query}")
        elif "wikipedia" in query:
            query = query.replace("wikipedia", "").strip()
            webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")
        elif "amazon" in query: 
            query = query.replace("amazon", "").strip()
            webbrowser.open(f"https://www.amazon.com/s?k={query}")
        elif "ebay" in query:
            query = query.replace("ebay", "").strip()
            webbrowser.open(f"https://www.ebay.com/sch/i.html?_nkw={query}")
        elif "netflix" in query:
            webbrowser.open("https://www.netflix.com")

# function for open new tab and close tab scroll up and down, click on titles
def browser_control(query):
    if "new tab" in query:
        pyautogui.hotkey("ctrl", "t")
    elif "close tab" in query or "close this tab" in query:
        pyautogui.hotkey("ctrl", "w")
    elif "scroll down" in query:
        pyautogui.scroll(-500)  # Scroll down
    elif "scroll up" in query:
        pyautogui.scroll(500)   # Scroll up
    elif "click on" in query:
        query = query.replace("click on", "").strip()
        try:
            location = pyautogui.locateCenterOnScreen(f'{query}.png', confidence=0.8)
            if location:
                pyautogui.click(location)
            else:
                speak(f"Could not find {query} on the screen.")
        except Exception as e:
            speak(f"An error occurred: {str(e)}")

# play any video on youtube or song on spotify using it title name and play word or else any other website
def play_video_song(query):
    if "play" in query:
        query = query.replace("play", "").strip()
        if "on youtube" in query:
            query = query.replace("on youtube", "").strip()
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        elif "on spotify" in query:
            query = query.replace("on spotify", "").strip()
            webbrowser.open(f"https://open.spotify.com/search/{query}")
        else:
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    elif "watch" in query:
        query = query.replace("watch", "").strip()
        if "on youtube" in query:
            query = query.replace("on youtube", "").strip()
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        else:
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")