"""
 Fça uma lista de compra com listas 
O usuário dece ter a possibilidade de
inserir, apagar e listar valores da sua lista
Nao permita que o programa quebre com 
erros de índices inexistentes na lista. 
"""
import os
compras  = []

while True:
    opcao = input('Selecione uma opção \n[i]nserir, [a]pagar ou [l]istar: ')

    if opcao == 'a':
        os.system('cls')
        apagarIndice = input('Escolha o índice para apagar: ')
    elif opcao == 'i':
        os.system('cls')
        inserir = input("Produto: ")
        compras.append(inserir)
        continue
    else:
        os.system('cls')
        print('Insira um valor válido!')

        
    if opcao == 'l' and len(compras) == 0:
        os.system('cls')
        print('Nada para listar')
        continue
    elif opcao == 'l':
        print(compras)
    else:
        continue

#ver atividade enumerate
