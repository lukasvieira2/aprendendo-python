
# Exercício 13: Carrinho de Compras
# Enunciado: Desenvolva um simulador simplificado de carrinho de compras.
# O programa deve ter uma lista vazia chamada carrinho.
# Usando um laço while, permita que o usuário adicione nomes de produtos ao carrinho até que ele digite a palavra "sair".
# Ao encerrar, exiba a lista de produtos ordenada alfabeticamente.

carrinho = []

print("--- Simulador de Carrinho de Compras ---")
print("Digite o nome dos produtos que deseja adicionar.")
print("Quando terminar, digite 'sair' para encerrar.\n")

while True:
    produto = input("Digite o nome do produto: ").strip()


    if produto.lower() == 'sair':
        break


    if produto:
        carrinho.append(produto)
        print(f"'{produto}' adicionado ao carrinho!")
    else:
        print("Por favor, digite um nome de produto válido.")

print("\n----------------------------------------")

# Exibe a lista final ordenada alfabeticamente
if carrinho:
    print("Seu carrinho de compras final (em ordem alfabética):")
    # sorted() cria uma nova lista ordenada sem modificar a original permanentemente
    for item in sorted(carrinho):
        print(f"- {item}")
else:
    print("Seu carrinho terminou vazio.")