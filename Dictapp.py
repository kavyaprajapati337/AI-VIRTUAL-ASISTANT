import os
import pyautogui
import webbrowser
import pyttsx3  # Fixed: was "importpyttsx3"
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set to the first voice
engine.setProperty("rate", 170)  # Set speech rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to open applications or websites based on voice commands
dictapp = {"commandPrompt":"cmd",                    #cmd
           "paint":"mspaint",                        #mspaint
           "calculator":"calc",                      #calc
           "notepad":"notepad",                      #notepad
           "wordpad":"wordpad",                      #wordpad    
           "chrome":"chrome",                        #chrome
           "edge":"msedge",                          #msedge
           "vlc":"vlc media player",                 #vlc
           "spotify":"spotify",                      #spotify
           "brave":"brave",                          #brave
           "explorer":"explorer",                    #explorer
           "task manager":"taskmgr",                 #taskmgr
           "settings":"ms-settings:",                #ms-settings
           "visual studio code":"code",              #code
           "blend":"blender",                        #blender
           "powerpoint":"powerpnt",                  #powerpnt
           "excel":"excel",                          #excel
           "word":"winword",                         #winword
           "whatsapp":"whatsapp",                    #whatsapp
           "zoom":"zoom",                            #zoom
           "discord":"discord",                      #discord
           "telegram":"telegram",                    #telegram
           "steam":"steam",                          #steam
           "microsoft store":"ms-windows-store:",    #ms-windows-store
           "file explorer":"explorer",               #explorer
           "task view":"taskview",                   #taskview
           "snipping tool":"snippingtool",           #snippingtool
           "canva":"canva",                          #canva
           "photoshop":"photoshop",                  #photoshop
           "illustrator":"illustrator",              #illustrator
           "after effects":"afterfx",                #afterfx
           "premiere pro":"pr",                      #pr
           "unity":"unity",                          #unity
           "git":"git bash",                         #git bash
           "terminal":"wt",                          #wt
           "quickshare":"quickshare",                #quickshare
           "obs":"obs",                              #obs
           "davenci resolve":"davinci resolve",      #davinci resolve
           "gitdesktop":"git desktop",               #git desktop
           "xampp":"xampp control panel",            #xampp control panel
           "xbox":"xbox game bar",                   #xbox game bar
           }

# Function to open applications or websites based on voice commands
def open_appweb(query):
    speak("Launching sir....")
    if ".com" in query or ".in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("Launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"http://www.{query}")  # Fixed: removed extra WWW
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")
                break

# Function to close applications or tabs based on voice commands
def closeappweb(query):
    speak("Closing sir....")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("tab closed")
    elif "2 tabs" in query:
        for i in range(2):
            pyautogui.hotkey("ctrl", "w")
            if i < 1: sleep(0.5)
        speak("2 tabs closed")
    elif "3 tabs" in query:
        for i in range(3):
            pyautogui.hotkey("ctrl", "w")
            if i < 2: sleep(0.5)
        speak("3 tabs closed")
    elif "4 tabs" in query:
        for i in range(4):
            pyautogui.hotkey("ctrl", "w")
            if i < 3: sleep(0.5)
        speak("4 tabs closed")
    elif "5 tabs" in query:
        for i in range(5):
            pyautogui.hotkey("ctrl", "w")
            if i < 4: sleep(0.5)
        speak("5 tabs closed")
    elif "6 tabs" in query:
        for i in range(6):
            pyautogui.hotkey("ctrl", "w")
            if i < 5: sleep(0.5)
        speak("6 tabs closed")
    elif "7 tabs" in query:
        for i in range(7):
            pyautogui.hotkey("ctrl", "w")
            if i < 6: sleep(0.5)
        speak("7 tabs closed")
    elif "8 tabs" in query:
        for i in range(8):
            pyautogui.hotkey("ctrl", "w")
            if i < 7: sleep(0.5)
        speak("8 tabs closed")
    elif "9 tabs" in query:
        for i in range(9):
            pyautogui.hotkey("ctrl", "w")
            if i < 8: sleep(0.5)
        speak("9 tabs closed")
    elif "10 tabs" in query:
        for i in range(10):
            pyautogui.hotkey("ctrl", "w")
            if i < 9: sleep(0.5)
        speak("10 tabs closed")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
                break