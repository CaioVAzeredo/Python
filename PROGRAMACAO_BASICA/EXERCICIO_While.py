"""
Iterando strings com while
"""
#       012345678910
nome = "Caio Viana"  # Iteráveis
#      1110987654321
""" print(nome)
print(tamanho_nome)
print(nome[3])

nova_string = ''
nova_string += '*L*u*i*z* *O*t*á*v*i*o' """


add = ""
i = 0
while i < len(nome):
    
    add += nome[i] + "*"
    i += 1

print(add)
