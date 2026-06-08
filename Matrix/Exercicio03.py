matriz_base = [[1, 2], [3, 4]]

nu1 = int(input("Digite um numero inteiro: "))

if matriz_base[0][0]:
    matriz_base[0][0] *= nu1
    matriz_base[0][1] *= nu1
    matriz_base[1][0] *= nu1
    matriz_base[1][1] *= nu1

print(matriz_base)

