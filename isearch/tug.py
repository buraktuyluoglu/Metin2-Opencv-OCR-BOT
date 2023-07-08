import pyautogui
import pydirectinput
import time
import PIL
from pyautogui import *
import keyboard
import cv2 as cv
time.sleep(2)
troll = pyautogui.locateOnScreen("trol.png",grayscale=True, confidence=0.90)
x, y, width, height = troll
pydirectinput.leftClick(int(x+width/2), int(y+height/2))
time.sleep(0.5)
keyboard.press("f2")
keyboard.press("ctrl")
keyboard.press_and_release("c")
keyboard.release("ctrl")
keyboard.press_and_release("a")
keyboard.press_and_release("m")
keyboard.press_and_release("a")
keyboard.press_and_release("space")
keyboard.press_and_release("c")
keyboard.press_and_release("o")
keyboard.press_and_release("k")
keyboard.press_and_release("space")
keyboard.press_and_release("s")
keyboard.press_and_release("e")
keyboard.press_and_release("v")
keyboard.press_and_release("i")
keyboard.press_and_release("y")
keyboard.press_and_release("o")
keyboard.press_and_release("r")
keyboard.press_and_release("u")
