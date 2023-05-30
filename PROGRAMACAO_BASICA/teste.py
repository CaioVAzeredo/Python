import random
tamanho = 0
cpf = ''
while tamanho <= 8:
    numero = "{:.0f}".format(random.random()*9)
    numeroFinal = str(numero)
    cpf += numeroFinal
    tamanho += 1

print(cpf)