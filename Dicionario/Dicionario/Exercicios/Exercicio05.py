
frase = input("Digite uma frase: ")


palavras = frase.split()


frequencia_palavras = {}

for palavra in palavras:

    palavra_limpa = palavra.lower().strip(",.?!;:")

    if palavra_limpa:

        if palavra_limpa in frequencia_palavras:
            frequencia_palavras[palavra_limpa] += 1

        else:
            frequencia_palavras[palavra_limpa] = 1

print("\nResultado da contagem:")
print(frequencia_palavras)