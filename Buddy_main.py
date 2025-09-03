import datetime
import pyttsx3
import speech_recognition as sr
import requests
import bs4 as BeautifulSoup
import pyautogui
import os
import keyboard
import mouse
import random
import webbrowser

#for i in range(3):
 #   a= input("enter password to open jarvis:")
  #  pw_file = open ("Password.txt", "r")
   # pw = pw_file.read()
    #pw_file.close()
    

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

# Main function to run the assistant
if __name__ == "__main__":
    while True:
        query = take_command().lower()
        if "Hi buddy" in query:  # Fixed: was "weak up"
            from GreetMe import greetme  # Fixed: was "greetme"
            greetme()

            # Main loop for listening to commands
            while True:
                query = take_command().lower()
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

                elif "tired" in query:
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

                elif "whatsapp" in query:
                    from Whatsapp import SendMessage
                    SendMessage()

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

                # search any city weather        
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

                # Exit commands    
                elif "good bye" in query:  # Fixed: was "good by"
                    speak("Thank you for using me, sir. Have a great day!")
                    exit()
                
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("Buddy","")
                    speak("you told me"+rememberMessage)
                    open("Remember.txt", "w")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do ypu remember" in query:
                    with open("Remember.txt", "r") as remember:
                        speak("you told me" + remember.read()) 
                elif "shutdown system" in query:
                    speak("are you sure you want to shutdown your system")
                    shutdown= input("do you whish to shutdown your computer? (yes/no)") 
                if shutdown.lower() == "yes":
                    os.system("shutdown /s /t 1")
                
                elif shutdown.lower() == "no":
                    break
                