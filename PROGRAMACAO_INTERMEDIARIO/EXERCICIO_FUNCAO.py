 
""" def duplicar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3

def quaduplicar(numero):
    return numero * 4 """
    

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        resultado = numero * multiplicador
        return resultado
    return multiplicar
duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quaduplicar = criar_multiplicador(4)

duplicador1 = duplicar(2)
duplicador2 = triplicar(2)
duplicador3 = quaduplicar(2)

print(duplicador1)
print(duplicador2)
print(duplicador3)