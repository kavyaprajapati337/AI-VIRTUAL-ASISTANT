# after creating new file saving word, ppt, excel or etc file with voice command at any destination with any name with voice
import os
from speak import speak
from keyboard import delete_key
from time import sleep
from pynput.keyboard import Key, Controller
keyboard = Controller()
from Dictapp import dictapp
from datetime import datetime
from win_shotcut import windows_shortcuts
import pyautogui
from browser_functions import web_functions
from tkinter import Tk, simpledialog
import pyperclip
from tkinter import messagebox
from pynput.mouse import Button, Controller as MouseController
mouse = MouseController()
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set to the first voice
engine.setProperty("rate", 170)  # Set speech rate
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def file_saved():
    try:
        speak("Where do you want to save the file sir?")
        sleep(2)
        windows_shortcuts()
        sleep(2)
        speak("Please type the destination path in the dialog box")
        root = Tk()
        root.withdraw()  # Hide the main window
        # we can change destination as per we want to save file
        destination_path = simpledialog.askstring("Input", "Enter the destination path where you want to save the file:")
        root.destroy()  # Close the Tkinter window
        if destination_path:
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            speak("What should be the name of the file sir?")
            sleep(2)
            speak("Please type the file name in the dialog box")
            root = Tk()
            root.withdraw()  # Hide the main window
            file_name = simpledialog.askstring("Input", "Enter the file name (without extension):")
            root.destroy()  # Close the Tkinter window
            if file_name:
                speak("Please tell me the file format like word, excel, powerpoint or text file")
                sleep(5)
                speak("Please type the file format in the dialog box")
                root = Tk()
                root.withdraw()  # Hide the main window
                file_format = simpledialog.askstring("Input", "Enter the file format (word, excel, powerpoint, text):")
                root.destroy()  # Close the Tkinter window
                if file_format:
                    extensions = {
                        "word": ".docx",
                        "excel": ".xlsx",
                        "powerpoint": ".pptx",
                        "text": ".txt"
                    }
                    ext = extensions.get(file_format.lower())
                    if ext:
                        full_path = os.path.join(destination_path, file_name + ext)
                        if os.path.exists(full_path):
                            speak(f"A file named {file_name} already exists at the destination. Please choose a different name.")
                            return
                        if file_format.lower() == "word":
                            keyboard.press(Key.ctrl)
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.release(Key.ctrl)
                            sleep(2)
                            pyperclip.copy(full_path)
                            keyboard.press(Key.ctrl)
                            keyboard.press('v')
                            keyboard.release('v')
                            keyboard.release(Key.ctrl)
                            sleep(1)
                            keyboard.press(Key.enter)
                            keyboard.release(Key.enter)
                            speak(f"Word document saved as {file_name} at the specified location.")
                        elif file_format.lower() == "excel":
                            keyboard.press(Key.ctrl)
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.release(Key.ctrl)
                            sleep(2)
                            pyperclip.copy(full_path)
                            keyboard.press(Key.ctrl)
                            keyboard.press('v')
                            keyboard.release('v')
                            keyboard.release(Key.ctrl)
                            sleep(1)
                            keyboard.press(Key.enter)
                            keyboard.release(Key.enter)
                            speak(f"Excel file saved as {file_name} at the specified location.")
                        elif file_format.lower() == "powerpoint":
                            keyboard.press(Key.ctrl)
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.release(Key.ctrl)
                            sleep(2)
                            pyperclip.copy(full_path)
                            keyboard.press(Key.ctrl)
                            keyboard.press('v')
                            keyboard.release('v')
                            keyboard.release(Key.ctrl)
                            sleep(1)
                            keyboard.press(Key.enter)
                            keyboard.release(Key.enter)
                            speak(f"PowerPoint file saved as {file_name} at the specified location.")
                        elif file_format.lower() == "text":
                            keyboard.press(Key.ctrl)
                            keyboard.press('s')
                            keyboard.release('s')
                            keyboard.release(Key.ctrl)
                            sleep(2)
                            pyperclip.copy(full_path)
                            keyboard.press(Key.ctrl)
                            keyboard.press('v')
                            keyboard.release('v')
                            keyboard.release(Key.ctrl)
                            sleep(1)
                            keyboard.press(Key.enter)
                            keyboard.release(Key.enter)
                            speak(f"Text file saved as {file_name} at the specified location.")
                        else:
                            speak("Unsupported file format. Please try again.")
    except Exception as e:
        speak("An error occurred while saving the file. Please try again. " + str(e))