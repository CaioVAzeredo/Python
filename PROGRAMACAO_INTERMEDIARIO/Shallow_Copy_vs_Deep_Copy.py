# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro


import copy
print(10 * '-','SHALOW COPY',10 * '-')
d1 = {
    'c1': 1,
    'c2': 2,
    'li': [0, 1, 2]
}

d2 = d1.copy() # faz uma cópia rasa apontando para o mesmo lugar na memória 
d2['c1'] = 1000
d2['li'][1] = 90000

print(d1, id(d1))
print(d2, id(d2))

print(10 * '-','DEEP COPY',10 * '-')
d3 = {
    'c1': 1,
    'c2': 2,
    'li': [0, 1, 2]
}
d4 = copy.deepcopy(d3)

d4['c1'] = 1000
d4['li'][1] = 90000

print(d3, id(d3))
print(d4, id(d4))

