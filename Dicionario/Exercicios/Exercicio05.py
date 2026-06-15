frase = input("Digite uma frase: ")

# Separando a frase em uma lista de palavras (ignorando maiúsculas/minúsculas)
palavras = frase.lower().split()
contador = {}

for palavra in palavras:
    if palavra in contador:
        contador[palavra] += 1
    else:
        contador[palavra] = 1

print("\nContagem de palavras:")
for palavra, quantidade in contador.items():
    print(f"'{palavra}': aparece {quantidade} vez(es)")