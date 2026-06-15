dados_pessoais = {
    "nome" : "joão",
    "idade" : 21,
    "nascimento" : "20-05-2005",
    "sexo" : "m",
    "altura" : 1.70,
    "temCNH" : True
}
dados_pessoais["altura"] = 1.85
dados_pessoais["peso"] = 70


nova_chaves, novo_valor = input("digite uma nova chave e um novo valor ou realize uma atal mização de dado: ").split(",")

dados_pessoais[nova_chaves] = novo_valor

continuar = "s"
while continuar == "s":




        dados = input("digite o que quer encontrar: ")

        print(dados_pessoais.get(dados, "Valor não encontrado!"))

        continuar = input("deseja continuar? [s/n]:")[0].lower()

print("---------------------------------------------------------------------------------")

for chave, valor in dados_pessoais.items ():
    print(f"{chave}: {valor}")

print("---------------------------------------------------------------------------------")

print(dados_pessoais.pop("peso", "chave não existe!"))
print(dados_pessoais.pop("nascimento", "chave não existe!"))
print(dados_pessoais)

print("---------------------------------------------------------------------------------")

print(dados_pessoais.values())

print("---------------------------------------------------------------------------------")

print("setando valor: ")

dados_pessoais.setdefault("peso", 80)
dados_pessoais.setdefault("telefone","6199999775")
dados_pessoais.setdefault("idade", 25)