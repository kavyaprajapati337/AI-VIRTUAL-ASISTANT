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
# Function to simulate key presses for various keyboard commands
def volume_up():
    for _ in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)

# Function to simulate key presses for volume down
def volume_down():
    for _ in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)

# Function to simulate key presses for media control commands
def next_track():
    keyboard.press(Key.media_next)
    keyboard.release(Key.media_next)
    sleep(0.1)

# Function to simulate key presses for previous track
def previous_track():
    keyboard.press(Key.media_previous)
    keyboard.release(Key.media_previous)
    sleep(0.1)

# Function to simulate key presses for skipping forward and backward
def skip_forward():
    keyboard.press(Key.media_next)
    keyboard.release(Key.media_next)
    sleep(0.1)
def skip_backward():
    keyboard.press(Key.media_previous)
    keyboard.release(Key.media_previous)
    sleep(0.1)

# Function to simulate key presses for skipping seconds forward and backward
def sec_forward():
    for _ in range(5):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        sleep(0.1)
def sec_backward():
    for _ in range(5):
        keyboard.press(Key.left)
        keyboard.release(Key.left)
        sleep(0.1)

# Function to simulate scrolling up and down
def scroll_up():
    for _ in range(5):
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        sleep(0.1)
def scroll_down():
    for _ in range(5):
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        sleep(0.1)

#bluetooth turn on and off
def bluetooth_on():
    keyboard.press(Key.media_bluetooth)
    keyboard.release(Key.media_bluetooth)
    sleep(0.1)

def bluetooth_off():
    keyboard.press(Key.media_bluetooth)
    keyboard.release(Key.media_bluetooth)
    sleep(0.1)

#wifi turn on and off
def wifi_on():
    keyboard.press(Key.media_wifi)
    keyboard.release(Key.media_wifi)
    sleep(0.1)

def wifi_off():
    keyboard.press(Key.media_wifi)
    keyboard.release(Key.media_wifi)
    sleep(0.1)

#hotspot turn on and off
def hotspot_on():
    keyboard.press(Key.media_hotspot)
    keyboard.release(Key.media_hotspot)
    sleep(0.1)

def hotspot_off():
    keyboard.press(Key.media_hotspot)
    keyboard.release(Key.media_hotspot)
    sleep(0.1)

#brightness increase and decrease at specific number tel by user
def brightness_control(level):
    if level > 0:
        for _ in range(level):
            keyboard.press(Key.media_brightness_up)
            keyboard.release(Key.media_brightness_up)
            sleep(0.1)
    elif level < 0:
        for _ in range(-level):
            keyboard.press(Key.media_brightness_down)
            keyboard.release(Key.media_brightness_down)
            sleep(0.1)

# screen cast and project
def screen_cast():
    keyboard.press(Key.media_projection)
    keyboard.release(Key.media_projection)
    sleep(0.1)
def project():
    keyboard.press(Key.media_projection)
    keyboard.release(Key.media_projection)
    sleep(0.1)

# delete key press
def delete_key():
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)
    sleep(0.1)

# software switching (Alt + Tab)
def switch_software():
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    sleep(0.1)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)
    sleep(0.1)

