import pyautogui
import time
import keyboard

# Wait for 5 seconds to give you time to open the window you want to click in
time.sleep(5)

# Clicks in the current mouse position, 10 times with an interval of 1 second
#for i in range(100):
while True:
    pyautogui.click()
    time.sleep(1)
    keyboard.press_and_release('delete') 