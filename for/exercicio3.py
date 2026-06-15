
#Exercício 3: O Separador de Pares e Ímpares
#Enunciado: Crie um programa que leia 10 números inteiros do teclado e os armazene em uma lista principal. Depois, o programa deve criar duas novas listas vazias: pares e impares. Varra a lista principal e mova cada número para a sua respectiva lista de acordo com a sua paridade. No final, exiba as três listas
numeros = []
impar = []
par = []

for i in range(10):
    numero = int(input("Digite o seu numero: "))
    numeros.append(numero)

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print("Minhas lista: ", numeros)
print("numeros pares: ", par)
print("numeros impares: ", impar)

