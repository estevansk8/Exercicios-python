
#Fazer o usuário falar qual é a palavra
palavra = input("Digite uma palavra: ")

#fazer o usuário falar qual letra deve ser removida
letra = input("Digite uma letra para ser removida: ")


#Fazer a remoção dessa letra na palavra
i = 0
while i < len(palavra) and palavra[i] != letra:
    i = i +1

# o i vai ta com o indice da letra que você quer remover ou com o ultimo indice
if palavra[i] == letra:
    #fatiamento = palavra[x:y]
    palavra = palavra[:i] + palavra[i + 1:]

print(f"A letra removida foi {letra.upper()}")
print(f" A palavra ficou assim: {palavra}")
        
        
    
