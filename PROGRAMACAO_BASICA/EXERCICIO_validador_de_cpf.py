
#    0    4    8   2   6   9   2   4     1
# *
#   10    9    8   7   6   5   4   3     2
#   0    36   64   14  36  45  8   12    2


#   0  +  36 +  64  +  14 + 36 + 45 + 8  + 12 +   2  = 217


# 217 * 10 = 2170

#2170 % 11 = 3

#se maior que 9:
    #o numero deve ser 0(zero)


numeros_para_Inserir = input("Insira um numero de cpf: ")
numeros = numeros_para_Inserir[:9] #Limitando do 0(zero) até o 9


        #0 1 2 3 4 5 6 7 8
cont = 10
soma = 0

for numero in numeros:
    soma += int(numero) * cont
    cont -= 1
    
resto = (soma * 10) % 11
if resto <=9:
    resto = resto
    print(resto)
else:
    resto = 0
    print(resto)
""" print((10*217)% 11) """