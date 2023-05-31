def soma(*args):
    total = 0
    for numero in args:
        print('Total: ', total, numero)
        total += numero 
        print('Total: ', total)
    print(total)

soma(1, 2, 3, 4, 5, 6)