import time
import pyautogui


def screenshot():
    name = int(round(time.time() * 1000))
    name = f'{name}.png'
    time.sleep(5)  # Time Wait Before Taking Screenshot
    img = pyautogui.screenshot(name)
    img.show()  # To Show the Screenshot After Being Taken


screenshot()
