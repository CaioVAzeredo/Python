def soma(*args): # *args empacota o que for envido para a funcao dentro de uma tupla
    total = 0
    for numero in args:
        total += numero 
    return total

soma_1_2_3 = soma(1, 2, 3,) 
print('-'*10,'\n', soma_1_2_3)
soma_4_5_6 = soma( 4, 5, 6) 
print('-'*10,'\n', soma_4_5_6)






numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros) # o asterisco serve para desempacotar os numeros da variável numeros 
print('-'*10,'\n', outra_soma)

print('\n', sum(numeros))