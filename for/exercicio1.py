# Exercício 01 - O Analista de Números
# Enunciado: Desenvolva um script que peça para o usuário digitar 6 números inteiros e os armazene em uma lista.
# A o final, o programa deve exibir:
# A lista completa na ordem em que foi digitada.
# A soma de todos os valores da lista.
# O maior e o menor valor presente na lista.

listaNumero = []

for i in range(6):
    numero = int(input("Digite seus numeros: "))
    listaNumero.append(numero)

total = sum(listaNumero)

print("-------------------------------------------------------------------------------------")

print(listaNumero)

print("-------------------------------------------------------------------------------------")

print(total)

print("-------------------------------------------------------------------------------------")

listaNumero.sort()
print(max(listaNumero))
print("-------------------------------------------------------------------------------------")
print(min(listaNumero))





