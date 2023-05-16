frase = "O Python é uma linguagem de programação multiparadigma. Python foi cirado por Guido van Rossum.".lower()

num_frase = len(frase)
i = 0
maior = 0
letra_apareceu = " "

while i < num_frase:
    letra_atual = frase[i]
    quant_de_letra = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if quant_de_letra > maior:
        maior = quant_de_letra
        letra_apareceu = letra_atual

    i += 1

print(f"A letra que apareceu mais vezes foi: {letra_apareceu.upper()} com {str(maior)}x  ")


