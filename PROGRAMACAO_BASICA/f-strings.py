nome = 'Caio Viana'
altura = 1.75
peso = 75
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'# O .2f se refere à quantidade de casas decimais terá depois do ponto

print(linha_1)
print(linha_2)
print(linha_3)