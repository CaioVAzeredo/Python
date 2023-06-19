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

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    i = 0
    while len(pergunta['Opções']) > i:
        print(f'{i})',pergunta['Opções'][i])
        i+=1
    resposta = input('Qual a resposta?')
     