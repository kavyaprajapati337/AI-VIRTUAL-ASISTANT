import pyttsx3
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set to the first voice
engine.setProperty("rate", 170)  # Set speech rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to take voice commands
extractedtime = open("Alarmtext.txt", "rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

# Function to delete the alarm time from the file
deletetime = open("Alarmtext.txt", "r+")
deletetime.truncate(0)  # Clear the file
deletetime.close()

# Function to ring the alarm at the specified time
def ring (time):
    timeset= str(time)
    timenow =timeset.replace("Jarvis", "")
    timenow = timenow.replace("alarm", "")
    timenow = timenow.replace("set an alarm", "")
    timenow = timenow.replace(" and ", ":")
    Alarmtime = str(timenow)
    print(Alarmtime)

    # Loop to check the current time and ring the alarm
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == Alarmtime:
            speak("Alarm ringing")
            os.startfile("Alarm.mp3")  # Play the alarm sound
        elif current_time + "00:00:30" == Alarmtime:
            exit()

# Main function to run the alarm
ring(Time)