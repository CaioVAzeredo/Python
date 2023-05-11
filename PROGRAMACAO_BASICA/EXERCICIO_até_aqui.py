"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input("Insira seu nome: ")
idade = input("Insira seu nome: ")


if nome and idade:
    nomeInvertido = nome[::-1]
    nomeEspaco = " " in nome
    resultado = ""
    if nomeEspaco == True:
        resultado = "Verdade"
    else:
        resultado = "Falso"
    numLetras = len(nome)
    primeiraLetra = nome[0]
    ultimaLetra = nome[-1]
    print(
        f"Nome invertido: {nomeInvertido} \nSeu nome tem espaço em {nome}: {resultado} \nSeu nome tem {numLetras} letras \nPrimeira do seu nome: {primeiraLetra}\n Ultima letra: {ultimaLetra}"
    )
else:
    print("Desculpe, você deixou campos vazios.")
