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
import Levenshtein
from difflib import SequenceMatcher
import re
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

current_directory = os.path.dirname(os.path.abspath(__file__))
cap_images = [os.path.join(current_directory, str(i) + ".png") for i in range(1, 84)]
item_list = "bos","DOLUNAYKILICI", "CENNETINGOZUKOLYE", "RUZGARAYAKKABISI", "KUCULENKAFA", "HIZIKSIR", "FUTBOLTOPU",\
            "EJDERHABICAGI", "ZEHIRKILICI", "HAVALICELIKYAY", "EJDERHATANRISIZIRHI", "ORKDISI", "OLTAI", "MOROT", \
            "KUTSAMAKAGIDI", "EJDERHAPENCESI", "KESISPLAKAZIRH", "ZENFASULYE", "SOZYUZUG", "PONG", "TAHTAKUPE", "ISTIRIDYE", "PARTIZAN", "SEYTANKANADICAKRAM", "KIVRIKANAHTAR", \
            "KUTSAMAKURESI", "MAVIIKSIR", "KRISTALKUPE", "KIRMIZIOT", "YARIINSANKILIC", "HIZTASI", "SALDIRIIKSIRI", \
            "MOROT", "SMOKIN", "BECERIKITABI", "MAVIPNGI", "SARIEJDERHAYAYI", "CESARETPELERINI", "KANTASI", "ARTTIRMAKAGIDI", \
            "SIYAHCELIKZIRH", "ISINLANMAYUZUGU", "ISINLAIMAYOZUGO", "GELINLIK", "OKCANTASI", "ABANOZKUPE", "ALTIN", "BUYULUMETAL", \
            "MORYAKUTKOLYE", "KIRMIZIDEMIRPALA", "AURATASZIRHI", "ASLANAGZIKALKAN", "MAVICELIKZIRH", "GELENEKSELMIGFER", "YESILOT", \
            "ALEVYELESI", "ORKDISI", "ASLANKILICI", "MUHAREBEKILICI", "GOKMAVISITAKIM", "KAPLANKALKAN", "ABANOZ", "TATLILAR", \
            "RUHTASI", "PUNC", "HORTLAKDISIKILICI", "KINKILICI", "KILCIK", "KLGIK", "KLgilk", "ZEHIRKILICI", "BEYAZINCI", "Kilcik", \
            "kilgik", "SIAMBICAGI", "ZENFASULYE", "KAZMA", "INCI", "INCLL", "inci", "DUYGUMASKESI", "AYISIGIDEFINESANDIGI", \
            "DERICIZMESI", "DOLUNAYKILICI", "SAHINKALKANI"


def click(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(np.random.uniform(0.1, 0.4))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def middle_click(metin):
    x, y, width, height = metin
    center_x = int(x + np.random.uniform(10, 30))
    center_y = int(y + np.random.uniform(10, 60))
    pyautogui.moveTo(center_x, center_y)
    time.sleep(np.random.uniform(0.5))
    click(center_x, center_y)
    time.sleep(1)


def random_click(metin):
    x, y, width, height = metin
    center_x = int(x + np.random.uniform(10, 30))
    center_y = int(y - np.random.uniform(40, 90))
    pyautogui.moveTo(center_x, center_y)
    time.sleep(np.random.uniform(0.5))
    click(center_x, center_y)
    time.sleep(1)


def is_captcha():
    captcha = pyautogui.locateOnScreen("sabit.png", grayscale=True, confidence=0.55)
    if captcha is None:
        print("captcha is none")
        return False
    else:
        print("captcha is true")
        return True


def is_game():
    game = pyautogui.locateOnScreen("oyun.jpg", grayscale=True, confidence=0.65)
    if game is None:
        return True
    else:
        return False


def attack_prom():
    time.sleep(np.random.uniform(0.4, 0.6))
    metin = pyautogui.locateOnScreen('metini.png', grayscale=True, confidence=0.60)
    is_attacking = pyautogui.locateOnScreen('metin_can_2.png', grayscale=True, confidence=0.40)
    if metin is not None:
        # print("i see")
        if is_attacking is None:
            print("i can attack")
            x, y, width, height = metin
            center_x = x + width // 2
            center_y = y + height // 2 + 33
            pyautogui.moveTo(center_x, center_y)
            time.sleep(np.random.uniform(0.2, 0.5))
            click(center_x, center_y)
            time.sleep(2)
        else:
            print("i am attacking i guess?")
    else:
        if metin is None and is_attacking is None:
            time.sleep(np.random.uniform(0.5, 2))
            keyboard.press("q")
            time.sleep(np.random.uniform(0.1, 0.7))
            keyboard.release("q")


def read_text_from_image():
    captcha = pyautogui.locateOnScreen("sabit.png", grayscale=True, confidence=0.55)
    x, y, width, height = captcha
    image = pyautogui.screenshot(region=(x, y - 169, width-8, height-14))
    text = pytesseract.image_to_string(image)
    text = re.sub('[^A-Za-z]+', '', text) # sadece harfleri bırakır
    #image.show()
    print(text)
    return text.strip()


def solve_captcha(string_list):
    read_text = read_text_from_image()
    for text in string_list:
        distance = Levenshtein.distance(read_text, text)
        text_length = max(len(read_text), len(text))
        similarity_ratio = (text_length - distance) / text_length
        if similarity_ratio > 0.65:
            print(text)
            index = string_list.index(text)
            print(index)
            cap_click = pyautogui.locateOnScreen(f"CAP2/{index}.png", grayscale=True, confidence=0.70)
            time.sleep(np.random.uniform(1, 2))
            middle_click(cap_click)
    time.sleep(2)
    if is_captcha() is True:
        captcha = pyautogui.locateOnScreen("sabit.png", grayscale=True, confidence=0.50)
        random_click(captcha)


while keyboard.is_pressed("-") is False:
    time.sleep(2)
    while is_game() is True:
        if is_captcha() is True:
            solve_captcha(item_list)
            time.sleep(np.random.uniform(1, 1.5))
            attack_prom()
        else:
            attack_prom()
            '''keyboard.press("space")
            time.sleep(np.random.uniform(1, 2))
            keyboard.press("1")
            time.sleep(0.1)
            keyboard.release("1")'''



