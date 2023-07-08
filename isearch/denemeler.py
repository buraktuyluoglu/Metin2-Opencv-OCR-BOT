import PIL
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
import cv2 as cv
import pydirectinput
import numpy as np
import os
import Levenshtein
import re
import pytesseract
import pywinauto
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
            "DERICIZMESI", "DOLUNAYKILICI", "SAHINKALKANI", "MAVIEJDERHASUIT", "HAVUC"


def randomizer():
    randomu = np.random.uniform(1, 3)
    key = "w"
    if randomu == 2:
        key = "a"
    if randomu == 3:
        key = "s"
    if randomu == 4:
        key = "d"
    return key


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
    time.sleep(0.5)


def random_click(metin):
    x, y, width, height = metin
    center_x = int(x + np.random.uniform(13, 30))
    center_y = int(y - np.random.uniform(40, 90))
    pyautogui.moveTo(center_x, center_y)
    time.sleep(np.random.uniform(0.5))
    click(center_x, center_y)
    time.sleep(0.5)


def is_captcha():
    captcha = pyautogui.locateOnScreen("sabit.png", grayscale=True, confidence=0.55)
    if captcha is None:
        print("captcha is none")
        return False
    else:
        print("captcha is true")
        return True


def is_alive():
    spawn = pyautogui.locateOnScreen("alive.png", grayscale=True, confidence=0.50)
    if spawn is not None:
        print("i am dead")
        return False
    else:
        return True


def spawn():
    time.sleep(8)
    spawn_bar = pyautogui.locateOnScreen("spawn_bar.png", grayscale=True, confidence=0.80)
    spawn_x, spawn_y, spawn_height, spawn_width = spawn_bar
    pyautogui.moveTo(spawn_x + 5, spawn_y)
    time.sleep(np.random.uniform(0.2, 0.5))
    click(spawn_x + 5, spawn_y)
    time.sleep(np.random.uniform(0.8, 1.5))
    keyboard.press("h")
    time.sleep(np.random.uniform(0.1, 0.2))
    keyboard.release("h")
    time.sleep(np.random.uniform(0.6, 1.3))
    keyboard.press("space")
    attack_prom()


def is_game():
    game = pyautogui.locateOnScreen("oyun.png", grayscale=True, confidence=0.80)
    if game is None:
        print("none game")
        return False
    else:
        return True


def attack_prom():
    if is_captcha() is True:
        solve_captcha(item_list)
        attack_prom()
    if is_alive() is not True:
        spawn()
    else:
        metin = pyautogui.locateOnScreen('metin_buzul.png', grayscale=True, confidence=0.60)
        is_attacking = pyautogui.locateOnScreen('metin_can_2.png', grayscale=True, confidence=0.40)
        if metin is not None:
            # print("i see")w
            if is_attacking is None:
                print("i can attack")
                keyboard.release("space")
                x, y, width, height = metin
                center_x = x + width // 2 - 4
                center_y = y + height // 2 + 40
                pyautogui.moveTo(center_x, center_y)
                time.sleep(np.random.uniform(0.2, 0.5))
                click(center_x, center_y)
                time.sleep(3)
                keyboard.press("space")
            else:
                print("i am attacking i guess?")
                time.sleep(0.5)
                if is_attacking is not None:
                    '''keyboard.press("esc")
                    time.sleep(np.random.uniform(0.1, 0.2))
                    keyboard.release("esc")
                    time.sleep(2)'''
                #do_fishing()

        else:
            if metin is None and is_attacking is None:
                keyboard.press("q")
                time.sleep(np.random.uniform(0.9, 1.1))
                keyboard.release("q")
                keyboard.release("space")
                new_key = randomizer()
                keyboard.press(new_key)
                time.sleep(np.random.uniform(1.8, 2.2))
                keyboard.release(new_key)


def do_fishing():
    time.sleep(1)
    app = pywinauto.Application(backend='uia').connect(title='ÜnalTuran2 | Wexler')
    window = app.window(title='ÜnalTuran2 | Wexler')
    window.set_focus()
    time.sleep(1)
    if is_captcha() is True:
        print("fish if")
        solve_captcha(item_list)
        stop = pyautogui.locateOnScreen("durdur.png", grayscale=True, confidence=0.80)
        x, y, width, height = stop
        center_x = int(x + np.random.uniform(5, 210))
        center_y = int(y + np.random.uniform(1, 15))
        pyautogui.moveTo(center_x, center_y)
        time.sleep(np.random.uniform(0.2, 0.5))
        click(center_x, center_y)
        time.sleep(np.random.uniform(2, 2.5))
        keyboard.press("space")
        time.sleep(np.random.uniform(0.1, 0.2))
        keyboard.release("space")
        time.sleep(np.random.uniform(2, 2.5))
        click(center_x, center_y)
        time.sleep(0.5)
        app = pywinauto.Application(backend='uia').connect(title='ÜnalTuran2 | Ignacio')
        window = app.window(title='ÜnalTuran2 | Ignacio')
        window.set_focus()
    else:
        print("fish else")
        time.sleep(0.5)
        app = pywinauto.Application(backend='uia').connect(title='ÜnalTuran2 | Ignacio')
        window = app.window(title='ÜnalTuran2 | Ignacio')
        window.set_focus()


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
    max_similarity = 0
    max_similarity_index = -1

    for index, text in enumerate(string_list):
        distance = Levenshtein.distance(read_text, text)
        text_length = max(len(read_text), len(text))
        similarity_ratio = (text_length - distance) / text_length
        if similarity_ratio > 0.65 and similarity_ratio > max_similarity:
            max_similarity = similarity_ratio
            max_similarity_index = index

    if max_similarity_index != -1:
        print(string_list[max_similarity_index])
        cap_click = pyautogui.locateOnScreen(f"CAP2/{max_similarity_index}.png", grayscale=True, confidence=0.70)
        time.sleep(1)
        middle_click(cap_click)

    time.sleep(1)
    if is_captcha() is True:
        captcha = pyautogui.locateOnScreen("sabit.png", grayscale=True, confidence=0.50)
        random_click(captcha)


while keyboard.is_pressed("-") is False:
    time.sleep(2)
    while is_game() is True:
        attack_prom()





