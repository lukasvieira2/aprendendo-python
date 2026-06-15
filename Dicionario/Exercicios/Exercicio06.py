estoque = {
    "Teclado": 15,
    "Mouse": 22,
    "Monitor": 8
}

produto_desejado = input("Digite o produto que deseja comprar: ").title()

if produto_desejado in estoque:
    quantidade = int(input(f"Quantas unidades de {produto_desejado} você quer? "))


    if estoque[produto_desejado] >= quantidade:
        estoque[produto_desejado] -= quantidade
        print(f"Compra realizada com sucesso! Estoque atualizado de {produto_desejado}: {estoque[produto_desejado]}")
    else:
        print(f"Estoque insuficiente. Temos apenas {estoque[produto_desejado]} unidades disponíveis.")
else:
    print("Desculpe, não vendemos esse produto.")