import pyautogui
import time
pyautogui.PAUSE = 0.5
#Abrir o navegador
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")

#Entrar no site
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")

time.sleep(4)
pyautogui.click(x=54, y=232)
pyautogui.write("cauaf5556@gmail.com")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.write("bosta")