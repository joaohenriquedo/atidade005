#Escreva um programa que permaneça em laço lendo números inteiros. 
#O laço termina quando for digitado 0 (zero).
#Cada valor diferente de zero digitado deve ser colocado em uma lista, desde que ele ainda não esteja lá, ou seja, valores repetidos não são aceitos. 
#Se um valor repetido for digitado, o programa deve exibir uma mensagem na tela. 
#Ao final exiba a lista e a quantidade de elementos que ela contém.

numeros = []
num = int(input("Digite um número (0 para terminar): "))
while num != 0:
    if num in numeros:
        print("Número repetido! Tente novamente.")
    else:
        numeros.append(num)
    num = int(input("Digite um número (0 para terminar): "))
print("\nLista de números:", numeros)
print("Quantidade de elementos:", len(numeros))

print("joa henrique")