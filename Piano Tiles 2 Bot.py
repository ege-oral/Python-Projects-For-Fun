"""
1- Enter this link "https://poki.com/en/g/piano-tiles-2?campaign=14340126420&adgroup=121283441970&target=dsa-645606693027&location=1012786&creative=540368175359&placement=&gclid=Cj0KCQjwpreJBhDvARIsAF1_BU0szzuiGlkSG5pw_UQIETMF6etdwMJKMhKq_BIj_wNX3V2zX_22d0MaAoeQEALw_wcB".
2- Start this code.
3- Press play button then press start button.
4- Enjoy.
"""

import pyautogui
import win32api
import keyboard

def mouseClick(x, y):
    win32api.SetCursorPos((x, y))
    pyautogui.click()

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(698, 490)[0] == 1 or pyautogui.pixel(698, 490)[0] == 0:
        mouseClick(698, 509)
    if pyautogui.pixel(778, 490)[0] == 1 or pyautogui.pixel(778, 490)[0] == 0:
        mouseClick(778, 509)
    if pyautogui.pixel(861, 490)[0] == 1 or pyautogui.pixel(861, 490)[0] == 0:
        mouseClick(861, 509)
    if pyautogui.pixel(946, 490)[0] == 1 or pyautogui.pixel(946, 490)[0] == 0:
        mouseClick(946, 509)

