"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input("Insira um numero inteiro: ")
try:
    Num = int(num)
    if Num % 2 == 0:
        print("O numero é par")
    else:
        print("O número é impar")
except:
    print("não é um número inteiro")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
Tempo = input("Insira as horas: ")
tempo = int(Tempo)

if tempo >= 0 and tempo <= 11:
    print("Bom dia")
elif tempo >= 12 and tempo <= 17:
    print("Boa tarde")
elif tempo >= 18 and tempo <= 23:
    print("Boa Noite")
elif tempo > 23:
    print("Valor inválido")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Insira seu nome: ")
tamanho = len(nome)

if tamanho <= 4:
    print("Seu nome é curto")
elif tamanho == 5 or tamanho == 6:
    print("Seu nome é normal")
elif tamanho > 6:
    print("Seu nome é grande")
