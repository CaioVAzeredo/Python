import pywhatkit
import pyautogui
import time
from datetime import datetime


contato = []
while True:
    numero = input("Insira um numero com o +55 ou (s/S) para sair: ")
    contato.append(numero)
    if numero == "s":
        break

mensagem = input("Insira a mensagem que deseja mandar para esses números: ")
while len(contato) >= 1:
    if contato == "s" or contato == "S":
        break
    pywhatkit.sendwhatmsg(contato[0], mensagem, datetime.now().hour, datetime.now().minute + 2)
    del contato[0]
    time.sleep(5)
    pyautogui.hotkey("enter")
    time.sleep(15) 
    pyautogui.hotkey("ctrl", "w")

print('Fim do programa!')
time.sleep(5)