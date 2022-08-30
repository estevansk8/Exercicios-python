#Pedir para o usuário fornecer duas strings
str1 = input("Digite uma palavra: ")
str2 = input("Digite outra palavra: ")


#Verificar o tamanho das strings são iguais
if len(str1) != len(str2):
    print("As palavras são diferentes")


else:

#Percorrer as palavras e verificar se todas as letras são iguais
    i = 0
    diferente = False
    
    while i < len(str1) and diferente == False :

        if str1[i] != str2[i]:
            diferente = True

        else:
            i = i + 1

#Printar se elas são diferentes ou não
    if diferente == False:
        print("As palavras são iguais")

    else:
        print("As palavras são diferentes")


#Printar as palavras e seu tamanho
print(f"A palavra ' {str1} ' tem tamanho {len(str1)}")
print(f"A palavra ' {str2} ' tem tamanho {len(str2)}")


    
