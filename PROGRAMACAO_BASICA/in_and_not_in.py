# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

nome = 'Caio';

print(nome[2]);
print(nome[-4]);

print(10 * '-');

print('io' in nome); # in e not in retorna True or False
print('Ca' in nome);

print(10 * '-');

print('io' not in nome);
print('ca' not in nome);

print(30 * '-');

nome = input('Digite seu nome: ');
encontrar = input('Digite o que deseja encontrar: ');

achar = encontrar in nome;
Nao_achar = encontrar not in nome
if achar == True:
    print(f'{encontrar} tem em {nome}');
elif Nao_achar not in nome:
    print(f'{encontrar} não tem em {nome}');
else:
    print('error');
