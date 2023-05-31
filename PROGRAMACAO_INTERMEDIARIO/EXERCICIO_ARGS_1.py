def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero

    return total

resultado = multiplica(1,2,3,10)
print(resultado)