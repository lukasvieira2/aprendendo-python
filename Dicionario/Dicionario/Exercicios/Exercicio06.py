
estoque = {
    "Teclado": 15,
    "Mouse": 22,
    "Monitor": 8
}

print("--- Estoque Atual ---")
for produto, qtd in estoque.items():
    print(f"- {produto}: {qtd} unidades")
print("---------------------\n")

produto_desejado = input("Digite o nome do produto que deseja comprar: ").title()

if produto_desejado in estoque:
    quantidade_desejada = int(input(f"Quantas unidades de '{produto_desejado}' você quer? "))

    if estoque[produto_desejado] >= quantidade_desejada:

        estoque[produto_desejado] -= quantidade_desejada
        print(f"\nCompra realizada com sucesso! Você comprou {quantidade_desejada}x {produto_desejado}.")
    else:

        print(
            f"\nDesculpe, estoque insuficiente. Temos apenas {estoque[produto_desejado]} unidades de '{produto_desejado}' disponíveis.")

else:
    print(f"\nO produto '{produto_desejado}' não está disponível em nossa loja.")

print("\n--- Estoque Atualizado ---")
print(estoque)