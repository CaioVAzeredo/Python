valor1 = input("Insira o primeiro valor: ")
valor2 = input("Insira o segundo valor: ")

if valor1 > valor2:
    print(f"{valor1=} è maior que o segundo")
elif valor2>valor1:
    print(f" {valor2=} è maior que o primeiro")
elif valor2 == valor1:
    print('Os dois valores sao iguais')
else:
    print('Nada foi digitado')
