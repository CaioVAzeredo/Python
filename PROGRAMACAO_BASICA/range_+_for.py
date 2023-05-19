"""
For + Range
range -> range(start, stop, step)
"""

numeros = range(10)

print(f'\nrange: {numeros}\n')


numeros = range(5, 10)
numeros = range(5, 10, 2) #range(menor valor, maior valor, steps)
for numero in numeros:
    print(numero)
print(10* '-')

num = range(10)
for numero in num:
    print(numero)
print(10* '-')
