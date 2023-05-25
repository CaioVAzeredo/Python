salas = [
    #0
    #   0         1
    ['Maria', 'Helena'],
    
    #1
    #   0
    ['Elaine'],

    #2                                3
    #   0       1        2       0   1   2   3
    ['Luiz', 'Joao', 'Eduarda', (0, 10, 30, 40)]
]
print(salas[0][1]) #Acessando dentro da primeira lista no segundo índice
print(salas[2][2])
print(salas[2][3][3])


for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)

