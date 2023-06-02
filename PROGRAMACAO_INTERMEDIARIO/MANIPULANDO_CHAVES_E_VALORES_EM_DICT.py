# Manipulando chaves e valores em dicionários

pessoa = {}
chave1 = 'nome' #criando uma chave(instancia) para pessoa

chave2 = 'sobrenome' #poderia ser: pessoa['sobrenome'] = Azeredo

pessoa[chave1] = 'Caio Viana' #adicionando uma informaçao na chave

pessoa[chave2] = 'Azeredo'

print(pessoa[chave1])

pessoa[chave1] = 'joao'
print(pessoa[chave1])

del pessoa[chave2]
print(pessoa)
print(pessoa['nome'])


#print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NAO existe')
else:
    print(pessoa['sobrenome'])