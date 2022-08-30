#Escrever uma palavra para ser analisada
palavra = input("Digite uma palavra: ")

#Fazer ela ficar toda maiuscula para não dar diferença entre maiuscula e minuscula
palavra_upper = palavra.upper()

#Analisar essa palavra percorrendo-a
i = 0
i2 = -1
diferente = False

while i < len(palavra_upper) and diferente == False:
    
    if palavra_upper[i] != palavra_upper[i2]:
        diferente = True
    
    
    i = i + 1
    i2 = i2 + (-1)

#Mostrar se elas são palindromas ou não:
if diferente == False:
    print(f"A palavra {palavra_upper} é palíndroma")

else:
    print(f"A palavra {palavra_upper} não é palíndroma ")
