import time

import pyautogui
import pyperclip

pyautogui.PAUSE = 2

#Passo 1: Entrar no google
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Passo 2: Abrir link do Youtube
time.sleep(3)
youtube = "https://www.youtube.com/watch?v=esX7SFtEjHg"
pyperclip.copy(youtube)
pyautogui.hotkey('ctrl','v')
pyautogui.press("enter")

#Passo 3: Abrir o gmail
time.sleep(3)
pyautogui.hotkey('ctrl','t')
gmail = "https://mail.google.com/"
pyperclip.copy(gmail)
pyautogui.hotkey('ctrl','v')
pyautogui.press("enter")

#Passo 4: Abrir o telegram
pyautogui.press("win")
pyautogui.write("telegram")
pyautogui.press("enter")

#Passo 5: Abrir o vscode
pyautogui.press("win")
pyautogui.write("vscode")
pyautogui.press("enter")

#Passo 6: Abrir o pycharm
pyautogui.press("win")
pyautogui.write("pycharm")
pyautogui.press("enter")