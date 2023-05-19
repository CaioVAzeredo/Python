lista = ['Maria','Helena','Luiz']

""" for letra in 'ABC':
    print(letra) """

# Minha solução
""" i = 0
for nome in lista:
    i += 1
    print(i - 1) """

#Solução do professor
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))