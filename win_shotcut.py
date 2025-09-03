from pynput.keyboard import Key,Controller

from time import sleep

keyboard = Controller()

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

    # Open Settings
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press(Key.s)
    keyboard.release(Key.s)
    keyboard.release(Key.shift)
    keyboard.release(Key.ctrl)

    # Open File Explorer
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press(Key.e)
    keyboard.release(Key.e)
    keyboard.release(Key.shift)
    keyboard.release(Key.ctrl)

    # Open Run Dialog cmd
    keyboard.press(Key.cmd)
    keyboard.press(Key.r)
    keyboard.release(Key.r)
    keyboard.release(Key.cmd)

    # Open Run Dialog
    keyboard.press(Key.cmd)
    keyboard.press(Key.r)
    keyboard.release(Key.r)
    keyboard.release(Key.cmd)

    # open 