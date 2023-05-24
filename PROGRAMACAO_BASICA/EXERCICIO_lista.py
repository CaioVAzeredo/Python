"""
 Fça uma lista de compra com listas 
O usuário dece ter a possibilidade de
inserir, apagar e listar valores da sua lista
Nao permita que o programa quebre com 
erros de índices inexistentes na lista. 
"""
import os
compras  = [' ']

while True:
    for i, nome in enumerate(compras):
        opcao = input('[A]pagar, [I]nserir ou [L]istar: ')
        if opcao == 'i':
            if opcao == 'i' and compras[0] == ' ':
                del compras[0]
            os.system('cls')
            nome = input('Valor: ')
            compras.append(nome)
            os.system('cls')

        elif opcao == 'a':
            os.system('cls')
            indice = input('Insira o valor do índice para apagar: ')
            intIndice = int(indice)
            del compras[intIndice]
            print(f'Produto excluído com sucesso!!')
            os.system('cls')
            continue
        elif opcao == 'l':
            if opcao == 'l' and len(compras) == 1 and compras[0] == ' ':
                print('Não há nada para listar!!')
            else:
                for i, nome in enumerate(compras):
                    print(i, nome)
                continue
        else:
            print('Insira um valor válido')