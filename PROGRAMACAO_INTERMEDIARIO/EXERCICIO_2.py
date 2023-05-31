def parOuImpar(numero):
    resultado = ' '
    if numero % 2 == 0:
        resultado = 'É PAR'
    else:
        resultado = 'É IMPAR'
    return resultado



valorPrimeiro = input('Insira um número: ')
valor = int(valorPrimeiro)
a = parOuImpar(valor)
print(a)

