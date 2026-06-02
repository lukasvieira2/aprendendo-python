

# Exercício 19: Somador de Números até o Zero (while)
# Enunciado: Desenvolva um programa que peça para o usuário digitar vários números inteiros.
# O programa deve somar todos esses números. A repetição só deve parar quando o usuário
# digitar exatamente o número 0. No final, exiba a soma total.


soma_total = 0

while True:
    num = int(input("Digite um número inteiro (ou 0 para encerrar): "))
    if num == 0:
        break  # Interrompe o laço imediatamente se o número for zero
    soma_total += num

print(f"\nA soma total de todos os números digitados é: {soma_total}")


print("\n" + "="*50 + "\n")

