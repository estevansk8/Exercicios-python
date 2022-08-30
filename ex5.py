#Inserir uma frase
frase = input("Digite uma frase: ")

#Percorrer a frase para colocar suas palavras em uma lista e conta-las depois
i = 0
contador = 1
while i<len(frase):
    
    if frase[i] == " ":
        contador = contador + 1
        i = i + 1


    else:
        
        i = i + 1

#Printar a quantidade de itens da lista(que no caso é a quantidade de palavras)
print(f"Essa frase possui {contador} palavras")
