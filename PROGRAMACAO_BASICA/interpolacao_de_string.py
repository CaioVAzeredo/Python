"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Caio'
preco = 1000.9999
variavel = '%s, o preco é RS%.2f' %(nome, preco)
print(variavel)
print('O hexadeciaml de %d é %08X' %(1500, 1500) )