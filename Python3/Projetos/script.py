import pyautogui
from time import sleep
f = open("../msc/script.txt", 'r')
pyautogui.press("win")
sleep(1)
pyautogui.typewrite('powershell')
pyautogui.press("enter")
sleep(2)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")