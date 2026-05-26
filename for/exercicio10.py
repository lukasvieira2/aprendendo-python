import random

#Exercício 10: Jogo da Adivinhação (while)
#Enunciado: O computador deve "pensar" em um número secreto entre 1 e 20 (Dica: use random.randint(1, 20)).
# O usuário deve tentar adivinhar.
# Enquanto o usuário errar, o programa deve dizer se o número secreto é maior ou menor que o palpite digitado.
# O laço encerra quando o usuário acertar.

import random

palpite = 0
numeroSecreto = random.randint(1, 20)

while palpite != numeroSecreto:
    palpite = int(input("digite um numero entre 1 e 20 tente adivinhar qual está certa: "))
    if palpite < numeroSecreto:
        print("o número secreto é maior")
    elif palpite > numeroSecreto:
        print("o número secreto é menor")

print("Parabéns! Você acertou o número secreto!")

