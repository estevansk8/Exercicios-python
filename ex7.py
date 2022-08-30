#Fazer o usuário digitar o nome
nome = input("Digite seu nome: ")

#Transformar esse nome em MAIUSCULO
nome_upper = nome.upper()

#Percorrer o nome e guardar os itens em uma lista
lista = []
i = len(nome_upper) - 1
while i >= 0:
    lista.append(nome_upper[i])
    i = i -1

#Mostrar esse nome de trás para frente
print(lista)


'''
MODO 2

#Fazer o usuário digitar o nome
nome = input("Digite seu nome: ")

#Transformar esse nome em MAIUSCULO
nome_upper = nome.upper()

#Percorrer o nome e guardar os itens em uma lista
lista = []
i = 0
while i < len(nome_upper):
    lista.insert(0, nome_upper[i])
    i = i + 1

#Mostrar esse nome de trás para frente
print(lista)
'''



'''
MODO 3

frase = "Mundo mundo vasto mundo"
print(frase[::-1])

'''