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
    pywhatkit.sendwhatmsg(contato[0], mensagem, datetime.now().hour, datetime.now().minute + 1)
    del contato[0]
<<<<<<< HEAD
    
=======
>>>>>>> 0a12af8e0cba838603bcb21869cb9cea1c2feec4
    time.sleep(60) 
    pyautogui.hotkey("ctrl", "w")
