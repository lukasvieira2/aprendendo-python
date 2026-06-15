dicionario_de_quadrados = {"chave" : "valor"}
for i in range(1,6):
     dicionario_de_quadrados.setdefault(i, i**2)
print("Chave | Valor")
for k,v in dicionario_de_quadrados.items():
    print(f"{k} -> {v}")