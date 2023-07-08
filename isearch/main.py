import PIL
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
import cv2 as cv
import sounddevice as sd
import soundfile as sf
import pydirectinput
import numpy as np
import os

'''current_directory = os.path.dirname(os.path.abspath(__file__))
metin_images = [os.path.join(current_directory, "metin", str(i) + ".png") for i in range(1, 23)]'''

# ... diğer kodlarınız ...


def click(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def is_captcha():
    captcha = pyautogui.locateOnScreen("cap/sabit.png", grayscale=True, confidence=0.50)
    if captcha is None:
        return False
    else:
        return True

while keyboard.is_pressed("-") is False:
    while pyautogui.locateOnScreen("oyun.jpg", grayscale=True, confidence=0.80) is not None:
        captcha = pyautogui.locateOnScreen("cap/sabit.png", grayscale=True, confidence=0.50)
        if is_captcha() is None:
            time.sleep(np.random.uniform(0.4, 0.6))
            image_location = pyautogui.locateOnScreen('metin.jpg', grayscale=True, confidence=0.60)
            is_attacking = pyautogui.locateOnScreen('metin_can.jpg', grayscale=True, confidence=0.50)
            if image_location is not None:
                # print("i see")
                if is_attacking is None:
                    print("i can attack")
                    x, y, width, height = image_location
                    center_x = x + width // 2 - 5
                    center_y = y + height // 2 + 40
                    pyautogui.moveTo(center_x, center_y)
                    time.sleep(np.random.uniform(0.2, 0.5))
                    click(center_x, center_y)
                    time.sleep(1)
                else:
                    print("i am attacking i guess?")
                    time.sleep(np.random.uniform(0.7, 1.4))
                    keyboard.press("esc")
                    time.sleep(0.1)
                    keyboard.release("esc")
            else:
                print("i can't see")



