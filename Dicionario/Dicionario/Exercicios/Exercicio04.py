
# Dicionário com produtos e preços
produtos = {
    "arroz": 25.50,
    "feijao": 8.90,
    "macarrao": 5.75
}

# Solicita o nome do produto
produto = input("Digite o nome do produto: ").lower()

# Verifica se o produto existe no dicionário
if produto in produtos:
    print(f"O preço do produto '{produto}' é R$ {produtos[produto]:.2f}")
else:
    print("Produto não encontrado.")         