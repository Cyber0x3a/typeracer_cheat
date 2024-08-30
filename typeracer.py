import pyautogui
from time import sleep
from os import system
print("")
writing_text = input("Enter the copied text>")
print("")
print("")
print("")
input("Press Enter when the race started and click on the typeracer input field as fast as you can")
sleep(2)
writing_text_list = writing_text.split(" ")
for i in writing_text_list:
    for j in i:
        pyautogui.press(j)
    pyautogui.press(" ")
system('cls')
