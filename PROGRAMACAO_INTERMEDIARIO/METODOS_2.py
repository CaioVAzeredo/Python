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

p1 = {
    'nome': 'Caio',
    'sobrenome': 'Viana',
}
""" print(p1['nome'])
print(p1.get('nome', 'Nao existe nome')) """

""" nome = p1.pop('nome')
print(nome)
print(p1) """

""" ultima_chame = p1.popitem()
print(ultima_chame)
print(p1) """


""" Primeria forma de fazer update """
p1.update({
    'nome': 'novo valor',
    'idade': 30,
})
""" Segunda forma de fazer update """
""" p1.update(nome = 'novo valor', idade = 30)
print(p1) """
""" Terceira forma de fazer update """
""" tupla = ('nome', 'novo valor'), ('idade', 30)
p1.update(tupla)
print(p1) """

""" Quarta forma de fazer update """
""" lista = ['nome', 'novo valor'], ['idade', 30]
p1.update(lista)
print(p1) """
