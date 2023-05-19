"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]

lista[2] = 300 #atribuindo novo valor para o indice 2
del lista[2] #del  deleta o indice em questão

print(lista)
print(lista[2])

lista.append(50) # .append() adiciona valor no final da lista
lista.pop() #.pop() ---> remove o ultimo valor
lista.append(60)
lista.append(70)

ultimoValor = lista.pop(3) #removendo o indice 3 

print(lista, ' Removido', ultimoValor)