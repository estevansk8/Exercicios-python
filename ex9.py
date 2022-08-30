#Pedir para o usuário digitar uma palavra
p1 = input("Digite uma palavra: ")

#Pedir para o usuário digitar outra palavra
p2 = input("Digite outra palavra: ")

#Deixar tudo maiusculo para nao dar diferença
p1_upper = p1.upper()
p2_upper = p2.upper()

#Ignorar espaços em branco da palavra1
i = 0
while i<len(p1_upper):
    
    if p1_upper[i] == " ":
        p1_upper = p1_upper[:i] + p1_upper[i+1 : ]

    i = i + 1

#Ignorar espaços em branco da palavra2
i = 0
while i<len(p2_upper):
    
    if p2_upper[i] == " ":
        p2_upper = p2_upper[:i] + p2_upper[i+1 : ]

    i = i + 1

#Analisar as duas palavras e verificar se elas são anagramas
if len(p1_upper) != len(p2_upper):
    print("Não é um anagrama")

#Criar estrutura de repetição para contar o numero de vezes que a letra aparece
else:
    
    anagrama = True
    i = 0
    while i< len(p1_upper) and anagrama:

#Contar a quantidade de elementos em cada palavra
        letra = p1_upper[i]
        p1_upper.count(letra)
        p2_upper.count(letra)
        
#Comparar se a quantidade de letras são iguais
        if p1_upper.count(letra) != p2_upper.count(letra):
            anagrama == False

        i = i + 1

#Falar se é ou não é anagrama
if anagrama == True:
    print("Esta palavra é um anagrama")

else:
    print("Esta palavra não é um anagrama")




