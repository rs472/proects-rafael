import pyautogui
import time

time.sleep(2)

pyautogui.PAUSE = 1.5


def rename():
    pyautogui.press('f2')
    pyautogui.press('right')
    pyautogui.typewrite('.png')
    pyautogui.press('enter')
    pyautogui.press('right')


try:
    while True:
        rename()

except KeyboardInterrupt:
    print('parou')
