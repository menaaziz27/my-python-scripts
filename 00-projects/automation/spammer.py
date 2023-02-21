import webbrowser
import pyautogui
import time
import cv2

webbrowser.open('https://web.whatsapp.com/')
time.sleep(5)
pyautogui.click(pyautogui.locateOnScreen(
    'C:\\Users\\3azzouz\\mypythonscripts\\whatsapp\\Unknown.PNG', grayscale=True, confidence=.7), duration=1)
pyautogui.click(pyautogui.locateOnScreen(
    'C:\\Users\\3azzouz\\mypythonscripts\\whatsapp\\type.png'), duration=1)
for i in range(10):
    pyautogui.write('Hi', interval=0.0)
    pyautogui.press('enter')
