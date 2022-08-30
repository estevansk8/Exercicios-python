lista = []

#Fazer o usuário falar qual é a palavra
palavra = input("Digite uma palavra: ")

#fazer o usuário falar qual letra deve ser removida
letra = input("Digite uma letra para ser removida: ")



#Fazer a remoção dessa letra na palavra
i = 0
while i < len(palavra):
    
    if palavra[i] == letra:
        palavra = palavra[:i] + palavra[i +1:]
        lista.append(palavra)
    i = i + 1

print(f"A letra removida foi {letra.upper()}")
print(f"A palavra ficou : {lista[len(lista) - 1]} ")




print(f"A letra removida foi {letra} e a palavra ficou assim: {lista}")