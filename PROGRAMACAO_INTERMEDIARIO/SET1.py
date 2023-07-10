# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
""" s1 = set() #vazio
s1 = {'Caio', 1, 2} # com dados
s2 = set('Caio')
print(s2) """



# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
""" li = [1,2,3,3,3,3,3]
s1 = set(li)
l2 = list(s1)
s1 = {1, 2, 3}
print(3 not in s1)
for numero in s1:
    print(numero) """





# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Caio')
s1.add(1)
s1.update(('olá, mundo', 1, 2, 3, 4))
s1.discard('olá, mundo')
s1.discard('Caio')
print(s1)
