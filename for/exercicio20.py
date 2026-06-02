

# Exercício 20: O Somador de Números Ímpares
# Enunciado: Crie um programa que calcule e exiba a soma de todos os números ímpares
# que são múltiplos de 3 e que se encontram no intervalo de 1 até 100.


soma_multiplos = 0

for numero_atual in range(1, 101):
    # Verifica se o número é ímpar E se é divisível por 3 ao mesmo tempo
    if numero_atual % 2 != 0 and numero_atual % 3 == 0:
        soma_multiplos += numero_atual

print(f"A soma dos ímpares múltiplos de 3 entre 1 e 100 é: {soma_multiplos}")