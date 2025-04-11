import pyautogui

import time
time.sleep(3)
for i in range(1, 4):
    pyautogui.write('Hello world!', interval=0.25)
    pyautogui.press("Enter")
    time.sleep(5)


