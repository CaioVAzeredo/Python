import pywhatkit
import pyautogui
import time
from datetime import datetime


contato = []
while True:
    numero = input("Insira um numero com o +55 ou (s/S) para sair: ")
    contato.append(numero)
    if numero == "s" or numero == "S":
        break

mensagem = input("Insira a mensagem que deseja mandar para esses números: ")
while len(contato) >= 1:
    pywhatkit.sendwhatmsg(contato[0], mensagem, datetime.now().hour, datetime.now().minute + 1)
    if contato[0] == 's' or contato[0] == 'S':
        break
    del contato[0]
    
    time.sleep(60) 
    pyautogui.hotkey("ctrl", "w")
print('Fim do programa!')
time.sleep(5)