from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import keyboard as k
import time

if __name__ == '__main__':
    time.sleep(3)
    keyboard = KeyboardController()
    mouse = MouseController()
    mouse.position = (726, 454)
    i = 0
    while True:
        if k.is_pressed('a'):
            break
        keyboard.press(Key.f2)
        mouse.click(Button.left, 1)
        i = i + 1

    print(i)
