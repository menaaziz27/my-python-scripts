>>> import pyautogui
>>> pyautogui.size()
Size(width=1920, height=1080)
>>> width, height = pyautogui.size()
>>> width
1920
>>> height
1080
>>> pyautogui.position()
Point(x=1157, y=450)
>>> pyautogui.position()
Point(x=1619, y=841)
>>> pyautogui.moveTo(10,10)
>>> pyautogui.moveTo(10,100 , duration = 1)
>>> pyautogui.moveRel(200,0)
>>> pyautogui.moveRel(200,0 , duration=5)
>>> pyautogui.click()
>>> pyautogui.position()
Point(x=1110, y=190)
>>> pyautogui.click(1110,190)
>>> pyautogui.position()
Point(x=1021, y=673)
>>> pyautogui.dragRel(300,0 , duration = 3)
>>> 


#keyboard GUI

>>> pyautogui.click(100,200) ; pyautogui.typewrite('Hello World!')
>>> pyautogui.click(100,200) ; pyautogui.typewrite('Hello World!' , interval = 0.1)
>>> pyautogui.click(100,200) ; pyautogui.typewrite('Hello World!' , interval = 0.1)
>>> pyautogui.click(100,100) ; pyautogui.typewrite(['a' , 'b' , 'left' , 'left','X' , 'Y'] , interval = 0.1)
>>> pyautogui.position()
Point(x=65, y=141)
>>> pyautogui.click(65,141) ; pyautogui.typewrite(['a' , 'b' , 'left' , 'left','X' , 'Y'] , interval = 0.1)
>>> pyautogui.KEYBOARD_KEYS
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome',
  'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15',
   'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 
   'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print',
    'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright',
     'yen', 'command', 'option', 'optionleft', 'optionright']


>>> pyautogui.press('f1')
>>> pyautogui.hotkey('ctrl' , 'o')
>>> 
