import pyttsx3

from pynput.keyboard import Key,Controller

from time import sleep

keyboard = Controller()

engine = pyttsx3.init("sapi5")  # Fixed: was "ngine"
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set to the first voice
engine.setProperty("rate", 170)  # Set speech rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#windows shortcuts
def windows_shortcuts():
    # Open Start Menu
    keyboard.press(Key.cmd)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    keyboard.release(Key.cmd)
    
    sleep(1)

    # Take a screenshot
    keyboard.press(Key.print_screen)
    keyboard.release(Key.print_screen)
    
    sleep(1)

    # Open Task Manager
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press(Key.escape)
    keyboard.release(Key.escape)
    keyboard.release(Key.shift)
    keyboard.release(Key.ctrl)
    sleep(1)

    # Open Settings
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press(Key.s)
    keyboard.release(Key.s)
    keyboard.release(Key.shift)
    keyboard.release(Key.ctrl)
    sleep(1)

    # Open File Explorer
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press(Key.e)
    keyboard.release(Key.e)
    keyboard.release(Key.shift)
    keyboard.release(Key.ctrl)
    sleep(1)

    # Open Run Dialog cmd
    keyboard.press(Key.cmd)
    keyboard.press(Key.r)
    keyboard.release(Key.r)
    keyboard.release(Key.cmd)
    sleep(1)

    # Open Run Dialog
    keyboard.press(Key.cmd)
    keyboard.press(Key.r)
    keyboard.release(Key.r)
    keyboard.release(Key.cmd)
    sleep(1)

    # select all files and folders
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    sleep(1)

    # Copy selected files and folders
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)
    sleep(1)

    # Paste copied files and folders
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)  
    sleep(1)

    # Cut selected files and folders
    keyboard.press(Key.ctrl)
    keyboard.press('x')
    keyboard.release('x')
    keyboard.release(Key.ctrl)      
    sleep(1)
