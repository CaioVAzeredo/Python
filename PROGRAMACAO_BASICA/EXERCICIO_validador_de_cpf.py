#    0    4    8   2   6   9   2   4     1
# *
#   10    9    8   7   6   5   4   3     2
#   0    36   64   14  36  45  8   12    2


#   0  +  36 +  64  +  14 + 36 + 45 + 8  + 12 +   2  = 217


# 217 * 10 = 2170

#2170 % 11 = 3

#se maior que 9:
    #o numero deve ser 0(zero)
import time
import re

while True:
    condicao = input('Deseja coloca um cpf? (s-sim. n-não):\n')
    if condicao == 's' or condicao == 'S':
        cpf = re.sub(r'[^0-9]', # isso faz com o que crie um range de 0 até 9 e que seja:
            '', # subistituído pelo que tem nas aspas
            input("Insira um numero de cpf: ").replace('.', '').replace('-', ''))

        cpfRepeticao = cpf[0] * len(cpf)
        if cpfRepeticao == cpf:
            print('\nCPF inválido. Insira um CPF válido!!!\n')
            continue

        digito_1 = cpf[:9] #Limitando do 0(zero) até o 9
        cont_10 = 10

        soma_1 = 0
        # digito 1
        for numero in digito_1:
            soma_1 += int(numero) * cont_10
            cont_10 -= 1
            
        resto_1 = (soma_1 * 10) % 11
        if resto_1 <=9:
            resto_1 = resto_1

        else:
            resto_1 = 0

        #digito 2

        digito_2 = cpf[:10]
        soma_2 = 0
        cont_11 = 11
        for numero in digito_2:
            soma_2 += int(numero) * cont_11
            cont_11 -= 1

        resto_2 = (soma_2*10)%11
        if resto_2  <= 9:
            resto_2 = resto_2

        else:
            resto_2 = 0

        if cpf[9:12] == (str(resto_1) + str(resto_2)):
            print('CPF válido')
        else:
            print('CPF NÃO é válido')
            """ print((10*217)% 11) """
    elif condicao == 'n' or condicao == 'N':
        break
    else:
        print('Insira um valor válido')
print('Fim do programa')
time.sleep(5)