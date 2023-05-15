

contato = []
quantidade_num = 0

while True:

    condicao = input('Deseja adicionar algum número?(s/n): ')
    if condicao == 's' or condicao == 'S':
        numero = input('Insira um numero')
        contato.append(numero)
    elif condicao == 'n' or condicao == 'N':
        break
    else: 
        print('Insira um valor válido')
        quantidade_num -= 1
    quantidade_num += 1

    if quantidade_num < 1:
        quantidade_num = 0 
    else:    
        quantidade_num = len(contato)

print(f"quantidade de números: {quantidade_num} números na lista: {contato}")