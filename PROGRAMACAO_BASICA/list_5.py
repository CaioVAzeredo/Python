"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
listaA = ['Caio','Jose',1, True, 1.2]
listaB = listaA.copy() #Copia a lista anterior 

listaA[0] = 'Qualquer coisa'
print(listaA)
print(listaB)