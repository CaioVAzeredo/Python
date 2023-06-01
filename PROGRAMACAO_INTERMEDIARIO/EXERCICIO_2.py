def parOuImpar(numero):
    
    if numero % 2 == 0:
        return 'É PAR'
    return 'É IMPAR'
     



valorPrimeiro = input('Insira um número: ')
valor = int(valorPrimeiro)

print(parOuImpar(valor))

