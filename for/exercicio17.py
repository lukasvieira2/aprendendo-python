
# Exercício 17: A Tabuada Automatizada
# Enunciado: Desenvolva um programa que peça para o usuário digitar um número inteiro.
# Utilizando o laço for e a função range(), exiba a tabuada desse número de 1 a 10 no terminal.
# Exemplo de saída esperada: 5 x 1 = 5, 5 x 2 = 10...


numero = int(input("Digite um número inteiro para ver a sua tabuada: "))

print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


print("\n" + "="*50 + "\n")
