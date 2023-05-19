"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [10,20,30,40]
lista.append('Caio')
nome = lista.pop()
lista.append(1233)
del lista[-1]
#lista.clear()
lista.insert(4, 50) #o primeiro valor é referente ao indice onde quero adicionar e o segundo é referente ao valor
print(lista[4])