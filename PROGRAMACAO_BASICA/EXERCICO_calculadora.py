while True:
    print("c - calcular\ns - sair")
    comando = input()
    if comando == 's' or comando == 'S':
        break
    elif comando == 'c' or comando == 'c':
        num1 = input('Primeiro numero: ')
        num2 = input('Segundo numero: ')

        int_num1 = int(num1)
        int_num2 = int(num2)

        operador = input('insira um operador (*, /, +, -): ')

        if operador == '*':
            resultado = int_num1 * int_num2
            print(resultado)
        if operador == '/':
            resultado = int_num1 / int_num2
            print(resultado)
        if operador == '+':
            resultado = int_num1 + int_num2
            print(resultado)
        if operador == '-':
            resultado = int_num1 - int_num2
            print(resultado)
    else:
        print('comando invalido. Insira um comando válido (s/c)')
print('operação acabou')