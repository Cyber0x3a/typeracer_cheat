import pyautogui
import mouse
from time import sleep
from os import system

while True:
    speed = input("\nChoose the typing speed(Default 2): 1> ~300WPM, 2> ~200WPM, 3> ~100WPM")
    if speed in ['1', '2', '3']:
        if speed == '1':
            speed = 0.3
        elif speed == '2':
            speed == 0.35
        elif speed == '3':
            speed == 0.5
        break
    if speed == '':
        print('Selected the default speed')
        speed = '2'

writing_text = input("Enter the copied text> ")
print("\n\nWaiting for left mouse click to start typing...")
mouse.wait(button='left', target_types=('down',))
system('cls')
sleep(1)
pyautogui.write(writing_text, interval=0.035)
