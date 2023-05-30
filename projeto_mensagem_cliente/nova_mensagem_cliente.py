import pywhatkit
import pyautogui
import time
from datetime import datetime


""" contato = []
while True:
    numero = input("Insira um numero com o +55 ou (s/S) para sair: ")
    contato.append(numero)
    if numero == "s" or numero == "S":
        break

mensagem = input("Insira a mensagem que deseja mandar para esses números: ")
while len(contato) >= 1:
    pywhatkit.sendwhatmsg(contato[0], mensagem, datetime.now().hour, datetime.now().minute + 1)
    del contato[0]
    time.sleep(40)s
    pyautogui.hotkey("enter")s
    time.sleep(5) 
    pyautogui.hotkey("ctrl", "w") """
contato = []
while True:
    numero = input("Insira um numero com o +55 ou (s/S) para sair: ")
    contato.append(numero)
    
    if numero == "s" or numero == "S":
        break

mensagem = input("Insira a mensagem que deseja mandar para esses números: ")
while len(contato) >= 1:
    while len(contato) >= 1:
        if numero == 's' or numero == 'S':
            pyautogui.hotkey("enter")
        pywhatkit.sendwhatmsg(contato[0], mensagem, datetime.now().hour, datetime.now().minute + 2)
        del contato[0]
        time.sleep(15) 
        pyautogui.hotkey("ctrl", "w")
        break
print('fim do programa')



