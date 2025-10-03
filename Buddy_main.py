from datetime import datetime
from logging import shutdown
from speak import speak
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import pyautogui
import os
import random
import GreetMe
import speak
import task
import webbrowser    

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set to the first voice
engine.setProperty("rate", 170)  # Set speech rate

# Function to speak text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to take voice commands
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

# Function to set an alarm
def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("Alarm.py")


if __name__ == "__main__":
    while True:
        q = take_command()
        if not q or q == "None":
            continue
        query = q.lower().strip()
        if "hi buddy" in query or "hello buddy" in query or "wake up" in query:
            from GreetMe import greetme
            greetme()

            # Main loop for listening to commands
            while True:
                try:
                    q = take_command()
                    if not q or q == "None":
                        continue
                    query = q.lower().strip()

                    # Exit condition to break the loop
                    if "go to sleep" in query:
                        speak("Going to sleep. Say 'Hi Buddy' to wake me up.")
                        break

                    # ... (rest of your existing command handlers unchanged) ...

                except Exception as e:
                    import traceback
                    print("Error in command loop:", e)
                    traceback.print_exc()
                    speak("I encountered an error. Check console for details.")

                # Exit condition to break the loop
                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime.")
                    break
                # Greeting commands
                elif "hello" in query:
                    speak("Hello sir, How are you")
                elif "i am fine" in query:
                    speak("that's great, sir")  # Fixed: was "speek"
                elif "how are you" in query:
                    speak("perfect, sir")
                elif "thank you" in query:
                    speak("You are welcome, sir")
                elif "what is your name" in query:
                    speak("I am Jarvis, your personal assistant.")
                elif "what is your age" in query:
                    speak("I am just a program, I don't have an age like humans do.")

                elif "tired gujarati" in query:
                    speak("playing your favourit song")
                    a=(1,2,3)
                    b= random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=xC1cj9zhh6k")
                    elif b==2:
                        webbrowser.open("")
                    elif b==3:
                        webbrowser.open("")
                    
                elif "tired hindi" in query:
                    speak("playing your favourit song")
                    a=(1,2,3)
                    b= random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=xC1cj9zhh6k")
                    elif b==2:
                        webbrowser.open("")
                    elif b==3:
                        webbrowser.open("")
                    

                # Media control commands keyboard
                elif "pause" in query:
                    pyautogui.press("k")  # Fixed: was "pyautogui.press('space')"
                elif "play" in query:
                    pyautogui.press("k")  # Fixed: was "pyautogui.press('playpause')"
                elif "mute" in query:
                    pyautogui.press("m")
                elif "unmute" in query:
                    pyautogui.press("m")
                elif "volume up" in query:
                    from keyboard import volume_up  # Fixed: was "from keyboard import volumeup"
                    speak("Increasing volume")
                    volume_up()
                elif "volume down" in query:
                    from keyboard import volume_down
                    speak("Decreasing volume")
                    volume_down()
                elif "next" in query:
                    from keyboard import next_track  # Fixed: was "from keyboard import nexttrack"
                    speak("Playing next track")
                    next_track()
                elif "previous" in query:
                    from keyboard import previous_track  # Fixed: was "from keyboard import previoustrack"
                    speak("Playing previous track")
                    previous_track()
                elif "skip forward" in query:
                    from keyboard import skip_forward
                    speak("Skipping forward")
                    skip_forward()
                elif "skip backward" in query:
                    from keyboard import skip_backward
                    speak("Skipping backward")
                    skip_backward()
                elif "second forward" in query:
                    from keyboard import sec_forward
                    speak("Skipping forward by 5 seconds")
                    sec_forward()
                elif "second backward" in query:
                    from keyboard import sec_backward
                    speak("Skipping backward by 5 seconds")
                    sec_backward()
                elif "scroll up" in query:
                    from keyboard import scroll_up
                    speak("Scrolling up")
                    scroll_up()
                elif "scroll down" in query:
                    from keyboard import scroll_down
                    speak("Scrolling down")
                    scroll_down()
                elif "project" in query:
                    from keyboard import project
                    speak("Opening project menu")
                    project()
                elif "delete" in query:
                    from keyboard import delete_key
                    speak("Deleting")
                    delete_key()
                
                #browser functions
                elif "web" in query:
                    from browser_functions import web_functions
                    web_functions(query)
                elif "browser control" in query:
                    from browser_functions import browser_control
                    browser_control(query)
                elif "switch window" in query:
                    pyautogui.hotkey("alt", "tab")
                elif "task view" in query:
                    pyautogui.hotkey("win", "tab")
                elif "minimize window" in query:
                    pyautogui.hotkey("win", "down")
                elif "maximize window" in query:
                    pyautogui.hotkey("win", "up")
                elif "close window" in query:
                    pyautogui.hotkey("alt", "f4")
                elif "open new window" in query:
                    pyautogui.hotkey("ctrl", "n")
                elif "open new incognito window" in query:
                    pyautogui.hotkey("ctrl", "shift", "n")
                elif "refresh" in query:
                    pyautogui.hotkey("ctrl", "r")
                elif "home" in query:
                    pyautogui.hotkey("alt", "home")
                elif "back" in query:
                    pyautogui.hotkey("alt", "left")
                elif "forward" in query:
                    pyautogui.hotkey("alt", "right")

                # Windows speak commands
                elif "screenshot" in query:
                    from win_shotcut import screenshot
                    speak("Taking screenshot")
                    screenshot()
                elif "open task manager" in query:
                    from win_shotcut import taskmanager
                    speak("Opening Task Manager")
                    taskmanager()
                elif "open settings" in query:
                    from win_shotcut import settings
                    speak("Opening Settings")
                    settings()
                elif "open file explorer" in query:
                    from win_shotcut import fileexplorer
                    speak("Opening File Explorer")
                    fileexplorer()
                elif "open run dialog" in query:
                    from win_shotcut import rundialog
                    speak("Opening Run Dialog")
                    rundialog()
                elif "select all" in query:
                    from win_shotcut import select_all
                    speak("Selecting all")
                    select_all()
                elif "copy" in query:
                    from win_shotcut import copy
                    speak("Copying")
                    copy()
                elif "paste" in query:
                    from win_shotcut import paste
                    speak("Pasting")
                    paste()
                elif "cut" in query:    
                    from win_shotcut import cut
                    speak("Cutting")
                    cut()

                # Mouse control commands
                elif "move left" in query:
                    from mouse import move_left
                    speak("Moving left")
                    move_left()
                elif "move right" in query:
                    from mouse import move_right
                    speak("Moving right")
                    move_right()
                elif "move up" in query:
                    from mouse import move_up
                    speak("Moving up")
                    move_up()
                elif "move down" in query:
                    from mouse import move_down
                    speak("Moving down")
                    move_down()
                elif "left click" in query:
                    from mouse import click_left
                    speak("Left clicking")
                    click_left()
                elif "right click" in query:
                    from mouse import click_right
                    speak("Right clicking")
                    click_right()
                elif "double left click" in query:
                    from mouse import double_click_left
                    speak("Double left clicking")
                    double_click_left()
                elif "double right click" in query:
                    from mouse import double_click_right
                    speak("Double right clicking")
                    double_click_right()
                elif "drag left" in query:
                    from mouse import drag_left
                    speak("Dragging left")
                    drag_left()
                elif "drag right" in query:
                    from mouse import drag_right
                    speak("Dragging right")
                    drag_right()

                # Application control commands
                elif "open" in query:
                    from Dictapp import open_appweb
                    open_appweb(query)  # Fixed: was "openappweb"
                elif "close" in query:
                    from Dictapp import closeappweb  # Fixed: was "close_appweb"
                    closeappweb(query)

                # Search commands
                elif "google" in query:
                    from SearchNow import search_google
                    search_google(query)
                elif "youtube" in query:
                    from SearchNow import searchyoutube
                    searchyoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import search_wikipedia
                    search_wikipedia(query)

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "calculate" in query:
                    from Calculator import WolfRamAlpha
                    from Calculator import Cal
                    query = query.replace("calculate","")
                    query = query.replace("Buddy","")
                    Cal(query)
                
                # WhatsApp message command
                elif "whatsapp" in query:
                    from Whatsapp import SendMessage
                    SendMessage()

                #file_saved commands
                elif "save file" in query:
                    from File_saved import save_file
                    save_file()
                elif "close notepad" in query:
                    from File_saved import close_notepad
                    close_notepad()
                elif "close word" in query:
                    from File_saved import file_saved
                    

                # search any city temperature
                elif "temperature" in query:
                    search = "temperature today"  # Fixed: more specific search
                    url = f"https://www.google.com/search?q={search}"
                    try:
                        r = requests.get(url)
                        data = BeautifulSoup(r.text, 'html.parser')
                        temp = data.find('div', class_='BNeawe iBp4i AP7Wnd').text
                        speak(f"The current temperature is: {temp}")
                    except:
                        speak("Sorry, I couldn't get the temperature information.")

                # search any city weather        p
                elif "weather" in query:
                    search = "weather today"  # Fixed: more specific search
                    url = f"https://www.google.com/search?q={search}"
                    try:
                        r = requests.get(url)
                        data = BeautifulSoup(r.text, 'html.parser')
                        weather = data.find('div', class_='BNeawe iBp4i AP7Wnd').text
                        speak(f"The current weather is: {weather}")
                    except:
                        speak("Sorry, I couldn't get the weather information.")

                # Set an alarm
                elif "set an alarm" in query:
                    speak("input time example :- 10 and 10 and 10")
                    speak("set the alarm time")
                    a= input("tell the time: ")
                    alarm(a)
                    speak("alarm set successfully")
                
                # current time
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"sir the time is: {strTime}")

                #code_writing commands
                elif "code" in query:
                    from task import code
                    code()
                elif "compile" in query:
                    from task import compile
                    compile()
                elif "run" in query:
                    from task import run
                    run()
                elif "execute" in query:
                    from task import execute
                    execute()
                elif "debug" in query:
                    from task import debug
                    debug()
                elif "find" in query:
                    from task import find
                    find()
                elif "replace" in query:
                    from task import replace
                    replace()
                elif "comment" in query:
                    from task import comment
                    comment()
                elif "uncomment" in query:
                    from task import uncomment
                    uncomment()
                elif "save" in query:
                    from task import save
                    save()
                elif "open folder" in query:
                    from task import open_folder
                    open_folder()
                elif "new file" in query:
                    from task import new_file
                    new_file()
                elif "new window" in query:
                    from task import new_window
                    new_window()
                elif "close file" in query:
                    from task import close_file
                    close_file()
                elif "close window" in query:
                    from task import close_window
                    close_window()
                elif "cut line" in query:
                    from task import cut_line
                    cut_line()
                elif "copy line" in query:
                    from task import copy_line
                    copy_line()
                elif "paste line" in query:
                    from task import paste_line
                    paste_line()
                elif "select all" in query:
                    from task import select_all
                    select_all()
                elif "undo" in query:
                    from task import undo
                    undo()
                elif "redo" in query:
                    from task import redo
                    redo()
                elif "find" in query:
                    from task import find
                    find()
                elif "replace" in query:
                    from task import replace
                    replace()
                elif "go to line" in query:
                    from task import go_to_line
                    go_to_line()
                elif "comment line" in query:
                    from task import comment_line
                    comment_line()
                elif "uncomment line" in query:
                    from task import uncomment_line
                    uncomment_line()
                elif "indent line" in query:
                    from task import indent_line
                    indent_line()
                elif "outdent line" in query:
                    from task import outdent_line
                    outdent_line()
                elif "run code" in query:
                    from task import run_code
                    run_code()
                elif "debug code" in query:
                    from task import debug_code
                    debug_code()
                elif "open terminal" in query:
                    from task import open_terminal
                    open_terminal()
                elif "close terminal" in query:
                    from task import close_terminal
                    close_terminal()
                elif "open command prompt" in query:
                    from task import open_cmd
                    open_cmd()
                elif "close command prompt" in query:
                    from task import close_cmd
                    close_cmd()
                elif "open camera" in query:
                    from task import open_camera
                    open_camera()
                elif "play music" in query:
                    from task import play_music
                    play_music()
                elif "send email" in query:
                    from task import sendEmail
                    try:
                        speak("What should I say?")
                        content = take_command()
                        speak("To whom should I send it?")
                        to = take_command()
                        sendEmail(to, content)
                    except Exception as e:
                        print(e)
                        speak("Sorry, I could not send the email.")
                elif "search wikipedia" in query:
                    from task import search_wikipedia
                    search_wikipedia(query)
                elif "open youtube" in query:
                    from task import open_website
                    open_website("youtube.com")
                elif "open google" in query:
                    from task import open_website
                    open_website("google.com")
                elif "open stack overflow" in query:
                    from task import open_website
                    open_website("stackoverflow.com")
                elif "play music" in query:
                    from task import play_music
                    play_music()
                elif "the time" in query:
                    from task import strTime
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")
                elif "open command prompt" in query or "open cmd" in query:
                    from task import open_cmd
                    open_cmd()
                elif "open camera" in query:
                    from task import open_camera
                    open_camera()
                elif "send email" in query:
                    from task import sendEmail
                    try:
                        speak("What should I say?")
                        content = take_command()
                        speak("To whom should I send it?")
                        to = take_command()
                        sendEmail(to, content)
                    except Exception as e:
                        print(e)
                        speak("Sorry, I could not send the email.")
                elif "stop" in query or "exit" in query:
                    speak("Goodbye!")
                    break
                

                # Exit commands    
                elif "good bye" in query:  # Fixed: was "good by"
                    speak("Thank you for using me, sir. Have a great day!")
                    exit()
                
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "").replace("buddy", "").strip()
                    speak("I will remember: " + rememberMessage)
                    with open("Remember.txt", "w", encoding="utf-8") as remember:
                        remember.write(rememberMessage)
                elif "what do you remember" in query or "what do u remember" in query:
                    try:
                        with open("Remember.txt", "r", encoding="utf-8") as remember:
                            data = remember.read().strip()
                        if data:
                            speak("You told me: " + data)
                        else:
                            speak("You haven't told me anything to remember.")
                    except FileNotFoundError:
                        speak("I don't have any memory saved yet.")

                elif "shutdown system" in query:
                    speak("Are you sure you want to shutdown your system? (yes/no)")
                    answer = input("Do you wish to shutdown your computer? (yes/no): ").strip().lower()
                if answer == "yes":
                    speak("Shutting down now.")
                    os.system("shutdown /s /t 1")
                else:
                    speak("Shutdown cancelled.")
