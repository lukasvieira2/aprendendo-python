
matriz = [
    [10, 25, 47],
    [88, 13, 5],
    [92, 4, 61]
]

numero_buscado = int(input("Digite um número para buscar na matriz: "))

achou = False
for linha in range(len(matriz)):
  for coluna in range(len(matriz[linha])):
    if matriz[linha][coluna] == numero_buscado:
       print(f"Número encontrado na Linha {linha}, Coluna {coluna}.")
       achou = True
       break

    if not achou:
       print("Número não encontrado")