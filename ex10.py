
#Pedir pro usuário digitar o número

#Transformar o n em string para conseguir percorrer
n = input("Digite um número: ")
 
#Retirar a contagem do -
if n[0] == "-":
    n = n[1:]

if n.isdigit() == True:
    print(len(n))

else:
    print("Não é um número")




