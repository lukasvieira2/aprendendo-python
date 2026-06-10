# Definindo uma matriz 3x3 com números inteiros
matriz = [
    [10, 25, 47],
    [88, 13, 5],
    [92, 4, 61]
]

# Pedindo o número para o usuário
numero_buscado = int(input("Digite um número para buscar na matriz: "))

achou = False

# Percorrendo a matriz para buscar o elemento
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if matriz[linha][coluna] == numero_buscado:
            print(f"Número encontrado na Linha {linha}, Coluna {coluna}.")
            achou = True
            break # Remove o break se quiser encontrar todas as posições caso o número se repita

if not achou:
    print("Número não encontrado")