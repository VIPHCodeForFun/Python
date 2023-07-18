
# pip install PyAutoGUI
# pip install opencv-python
# https://theuselessbutton.com/

from pyautogui import locateCenterOnScreen, click
import time


def click_button(image):
    while True:
        position = locateCenterOnScreen(image, confidence=0.9)

        if position:
            break

    x, y = position
    click(x, y)


image = 'fireBoltQ.png'
# time.sleep(2)  # wait 2 seconds
click_button(image)
