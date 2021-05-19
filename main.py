from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from datetime import date, datetime
from PIL import ImageChops # $ pip install pillow
from pyscreenshot import grab # $ pip install pyscreenshot


def sumCheck(x1,y1,x2,y2):
    im = grab(bbox=(x1,y1,x2,y2))
    while True: 
        diff = ImageChops.difference(grab(bbox=(x1,y1,x2,y2)), im)
        bbox = diff.getbbox()
        if bbox is not None:
            break

def click (x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def scroll(clicks=0, delta_x=0, delta_y=0, delay_between_ticks=0):

    if clicks > 0:
        increment = win32con.WHEEL_DELTA
    else:
        increment = win32con.WHEEL_DELTA * -1

    for _ in range(abs(clicks)):
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, delta_x, delta_y, increment, 0)
        time.sleep(delay_between_ticks)

def main():

    while True:
        if datetime.now().hour >=17:
            click(799,335)
            time.sleep(1)
            scroll(-1,0,0,0.1)
            click(1113,710)
            print("Pass")
            break

        elif keyboard.is_pressed('q'):
            break
        
        else:
            print(datetime.now().minute)

main()

