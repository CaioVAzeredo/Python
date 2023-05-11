"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar seu numero: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
except:
    print('Isso não é um número')