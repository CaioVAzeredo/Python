nomes =['Caio','Viana','Azeredo']
nome1, nome2, nome3 = nomes

#nome1, nome2, nome3 = ['Caio','Viana','Azeredo']

nome1, *_ = ['Caio','Viana','Azeredo']
print(nome1, _) #o underline é para identificar o resto das informações da array

#para pegar o indice que quiser basta colocar o underline
_,nome2,_, *_ = ['Caio','Viana','Azeredo'] 
print(nome2)
_,_,nome3, *_ = ['Caio','Viana','Azeredo'] 
print(nome3)