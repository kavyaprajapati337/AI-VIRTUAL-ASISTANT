from pynput.keyboard import Key,Controller

from time import sleep

keyboard = Controller()

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

