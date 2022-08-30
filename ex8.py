#Fazer o usuário digitar uma frase
frase = input("Digite uma frase: ")

#Criar contadores
contador_vazio = 0
contador_vogais = 0
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

#Percorrer a frase para verificar os elementos
i = 0
while i< len(frase):

#Adicionar os elementos pertencentes aos seus devidos contadores   
    if frase[i] == " ":
        contador_vazio = contador_vazio + 1

    if frase[i] == "a":
        contador_a = contador_a + 1
        contador_vogais = contador_vogais + 1

    if frase[i] == "e":
        contador_e = contador_e + 1
        contador_vogais = contador_vogais + 1

    if frase[i] == "i":
        contador_i = contador_i + 1
        contador_vogais = contador_vogais + 1

    if frase[i] == "o":
        contador_o = contador_o + 1
        contador_vogais = contador_vogais + 1

    if frase[i] == "u":
        contador_u = contador_u + 1
        contador_vogais = contador_vogais + 1

    i = i + 1

#Printar os elementos
print(f"O numero de elemnetos vazio nessa frase é de: {contador_vazio} ")
print(f"O numero de vogais nessa frase é de: {contador_vogais} ")
print(f"'A' aparece {contador_a} vezes ")
print(f"'E' aparece {contador_e} vezes")
print(f"'I' aparece {contador_i}  vezes")
print(f"'O' aparece {contador_o} vezes")
print(f"'U' aparece {contador_u} vezes")

