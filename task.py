import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import subprocess

# --- Initialize Text-to-Speech Engine ---
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # Select male voice

def speak(audio):
    """Speaks the provided audio text."""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Wishes the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am an AI assistant. How may I help you?")

def takecommand():
    """Listens to the microphone and returns the recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1) # Adjust for background noise
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
    except sr.UnknownValueError:
        print("Sorry, I could not understand that. Could you please repeat?")
        return "None"
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return "None"
    return command

# --- Functions to perform tasks ---
def search_wikipedia(query):
    """Searches Wikipedia for the given query."""
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except wikipedia.exceptions.PageError:
        speak("Sorry, I could not find that page on Wikipedia.")
    except Exception:
        speak("Sorry, something went wrong while searching Wikipedia.")

def open_website(url):
    """Opens a website in the default web browser."""
    speak(f"Opening {url}")
    webbrowser.open(url)

def play_music():
    """Plays music from a directory."""
    # Ensure this path is correct for your system
    music_dir = 'C:\\Users\\Kavya Prajapati\\Music' 
    if os.path.exists(music_dir):
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
        else:
            speak("No music files found in the directory.")
    else:
        speak("Music directory not found.")

def open_camera():
    """Opens the system camera."""
    speak("Opening camera")
    subprocess.run('start microsoft.windows.camera:', shell=True)

def open_cmd():
    """Opens the command prompt."""
    speak("Opening Command Prompt")
    os.system("start cmd")

def sendEmail(to, content):
    """Sends an email using a mock server (requires setup for real use)."""
    # NOTE: This function requires proper SMTP server credentials for actual use.
    # The current implementation will likely fail without a configured SMTP setup.
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password') # Replace with your credentials
        server.sendmail('youremail@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to send this email.")

# --- Main Program Loop ---
if __name__ == "__main__":
    wishMe()
    while True:
        command = takecommand().lower()

        # Logic for executing commands
        if 'wikipedia' in command:
            search_wikipedia(command)
        
        elif 'open youtube' in command:
            open_website("youtube.com")
            
        elif 'open google' in command:
            open_website("google.com")

        elif 'open stack overflow' in command:
            open_website("stackoverflow.com")

        elif 'play music' in command:
            play_music()

        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open command prompt' in command or 'open cmd' in command:
            open_cmd()

        elif 'open camera' in command:
            open_camera()

        elif 'send email' in command:
            try:
                speak("What should I say?")
                content = takecommand()
                speak("To whom should I send it?")
                to = takecommand()
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("Sorry, I could not send the email.")
        
        elif 'stop' in command or 'exit' in command:
            speak("Goodbye!")
            break

        # Additional functionality can be added here
        else:
            if command != "none": # Avoid repeating "Sorry, I could not understand"
                speak("Sorry, I did not understand that command.")