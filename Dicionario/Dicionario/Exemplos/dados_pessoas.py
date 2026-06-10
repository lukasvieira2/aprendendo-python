dados_pessoais = {
    "nome" : "joão",
    "idade" : 21,
    "nascimento" : "20-05-2005",
    "sexo" : "m",
    "altura" : 1.70,
    "temCNH" : True
}+
print(dados_pessoais.keys())
dados_pessoais["altura"] = 1.85
dados_pessoais["peso"] = 70
dados_pessoais[""]

nova_chaves, novo_valor = input("digite uma nova chave e um novo valor ou realize uma atalização de dado: ").split(",")

dados_pessoais[nova_chaves] = novo_valor

continuar = "s"
while continuar == "s":




        dados = input("digite o que quer encontrar: ")

        print(dados_pessoais.get(dados, "Valor não encontrado!"))

        continuar = input("deseja continuar? [s/n]:")[0].lower()