matriz_base = [[1, 2], [3, 4]]

fator = int(input("Digite um numero inteiro: "))

nova_matriz = []

for linha in matriz_base:
    nova_linha = []

    for elemento in linha:
        nova_linha.append(elemento * fator)

    nova_matriz.append(nova_linha)

print("Nova matriz:")
for linha in nova_matriz:
    print(linha)