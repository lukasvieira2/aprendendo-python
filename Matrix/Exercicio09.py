matriz_valores = [
    [15, 42, 7],
    [23, 91, 12],
    [34, 8, 55]
]

maior_valor = matriz_valores[0][0]
posicao_maior = (0, 0)

menor_valor = matriz_valores[0][0]
posicao_menor = (0, 0)


for l in range(len(matriz_valores)):
    for c in range(len(matriz_valores[l])):
        valor_atual = matriz_valores[l][c]


        if valor_atual > maior_valor:
            maior_valor = valor_atual
            posicao_maior = (l, c)


        if valor_atual < menor_valor:
            menor_valor = valor_atual
            posicao_menor = (l, c)


print(
    f"Maior: {maior_valor} na posição [{posicao_maior[0]}][{posicao_maior[1]}] | Menor: {menor_valor} na posição [{posicao_menor[0]}][{posicao_menor[1]}]")