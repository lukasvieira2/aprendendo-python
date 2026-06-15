produtos = {
    "Celular": 1500.00,
    "Notebook": 3500.00,
    "Fone de Ouvido": 120.00
}

busca = input("Digite o nome do produto que deseja buscar: ").title()

if busca in produtos:
    print(f"O preço de {busca} é R$ {produtos[busca]:.2f}")
else:
    print("Produto não encontrado.")