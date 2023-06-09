# Exercício - sistema de perguntas e respostas

perguntas= [
    {
      'Pergunta': 'Quanto é 2+2?',  
      'Opções': ['1', '2', '3', '4','5'], 
      'Resposta': '4', 
    },
        {
      'Pergunta': 'Quanto é 5*5?',  
      'Opções': ['25', '55', '10', '10', '51'], 
      'Resposta': '25', 
    },
        {
      'Pergunta': 'Quanto é 10/2?',  
      'Opções': ['4', '5', '2', '2','1'], 
      'Resposta': '5', 
    }
]

i = 0
for pergunta in perguntas :
      
    print(pergunta['Pergunta'])
    j = int(0)
    for opcao in pergunta['Opções']:
        print(f'{j})',opcao)  
        j += 1

    respostaUsuario = input('Escolha uma opçao: ')
    resposta = str(respostaUsuario)

    if resposta == pergunta['Resposta']:
        print('Voce acertou')
    else: print('Voce errou')
    i += 1
    