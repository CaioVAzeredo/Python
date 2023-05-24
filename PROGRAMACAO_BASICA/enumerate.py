""" 
enumerate - enumera iteráveis (índices)
 """
lista = ['Maria','Helena','Luiz']
lista.append('Joao')

#lista_enumerada = list(enumerate(lista, start = 19))

for indice, nome in enumerate(lista):
    print(indice, nome, )


""" for item in enumerate(lista):
    indice, nome = item 
    print(indice, nome)
 """    
#for tupla_enumerada in enumerate(lista)
#   print('For da tupla: ')
#   for valor in tupla_enumerada:
#       print(f'\t{valor}')