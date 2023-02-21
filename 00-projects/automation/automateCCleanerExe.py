'''
Run CCleaner v3
Designed to run at boot on Windows 7.
With screen res of 1920x1080, 125% medium.
 
Task:
run ccleaner app,
pause 10, wait for windows to load, click on auto clean,
Run CCleaner
press R
pause 15 wait for clean to finish,
move mouse to exit, click on exit.
 
By Steve Shambles July 2019.
stevepython.wordpress.com
'''
import subprocess
import time
import pyautogui
 
# Wait for everything to load in, windows, apps etc.
# You may need to adjust this timing for your system.
time.sleep(10)
 
# Run CCleaner.
# You may need to change this to reflect your install.
subprocess.Popen(r"C:\Program Files\CCleaner\CCleaner64.exe")
time.sleep(0.3)
 
# Tell Pyautogui what the windows name is.
WINDOW = pyautogui.getWindow("CCleaner")
 
# Focus on and bring ccleaner to front.
WINDOW.set_foreground()
 
# Give CCleaner plenty of time to come to front.
time.sleep(1.5)
 
#keyboard shortcut R to hit 'Run Cleaner' button,
pyautogui.press('R')
 
# Wait 15 seconds to give time for the cleaning operation.
# You may need to adjust.
time.sleep(15)
 
# Move mouse to exit button and click.
pyautogui.moveTo(1905, 10, 1)
pyautogui.click()