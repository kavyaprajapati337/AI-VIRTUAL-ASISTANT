from pynput.mouse import Button,Controller

from time import sleep

mouse = Controller()

# Function to simulate mouse movements and clicks
def move_left():
    for _ in range(5):
        mouse.move(-10, 0)
        sleep(0.1)  
def move_right():
    for _ in range(5):
        mouse.move(10, 0)
        sleep(0.1)

# Function to simulate mouse movements up and down
def move_up():
    for _ in range(5):
        mouse.move(0, -10)
        sleep(0.1)
def move_down():
    for _ in range(5):
        mouse.move(0, 10)
        sleep(0.1)

# Function to simulate left and right mouse clicks
def click_left():
    mouse.click(Button.left, 1)
def click_right():
    mouse.click(Button.right, 1)
def double_click_left():
    mouse.click(Button.left, 2)
def double_click_right():
    mouse.click(Button.right, 2)
def drag_left():
    mouse.press(Button.left)
    sleep(0.1)
    mouse.release(Button.left)
def drag_right():
    mouse.press(Button.right)
    sleep(0.1)
    mouse.release(Button.right)
