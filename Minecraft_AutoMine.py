import pyautogui
import time
def checkPos():
    print(pyautogui.position())
def mine():
    pyautogui.moveTo(927, 310)
    pyautogui.leftClick()
    for i in range(0, 500):
        if i%5==0:
            time.sleep(1)
        else:
            pyautogui.dragTo(0, 0, 3, button="left")
mine()


