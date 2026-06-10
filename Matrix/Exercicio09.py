matriz_valores = [
    [15, 42, 7],
    [23, 91, 12],
    [34, 8, 55]
]

# Inicializando as variáveis com o primeiro elemento da matriz
maior_valor = matriz_valores[0][0]
posicao_maior = (0, 0)

menor_valor = matriz_valores[0][0]
posicao_menor = (0, 0)

# Percorrendo a matriz para comparar os valores
for l in range(len(matriz_valores)):
    for c in range(len(matriz_valores[l])):
        valor_atual = matriz_valores[l][c]

        # Verificando o maior
        if valor_atual > maior_valor:
            maior_valor = valor_atual
            posicao_maior = (l, c)

        # Verificando o menor
        if valor_atual < menor_valor:
            menor_valor = valor_atual
            posicao_menor = (l, c)

# Exibindo o resultado no formato solicitado
print(
    f"Maior: {maior_valor} na posição [{posicao_maior[0]}][{posicao_maior[1]}] | Menor: {menor_valor} na posição [{posicao_menor[0]}][{posicao_menor[1]}]")