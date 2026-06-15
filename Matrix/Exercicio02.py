matriz_quadrada = [
    [5, 2, 9, 12],
    [1, 8, 3, 8],
    [4, 7, 6, 8],
    [4, 7, 6, 12]
]

Numeros = []


for i in range(len(matriz_quadrada)):
        Numeros.append(matriz_quadrada[i][i])
t = str(set(Numeros))


print(f'Soma da diagonal da matriz quadrada de {" + ".join(map(str,Numeros))} = {sum(Numeros)}:')
