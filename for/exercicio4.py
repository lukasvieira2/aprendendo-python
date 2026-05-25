
# Exercício 4: Verificador de Maioridade da Turma (Intermediário)
# Enunciado: Desenvolva um programa que leia o ano de nascimento de 7 pessoas. Utilizando o for, o programa deve calcular a idade de cada uma com base no ano atual (2026) e, no final, exibir quantas pessoas já atingiram a maioridade (18 anos ou mais) e quantas ainda são menores.

anos = []
maior = []
menor = []

for c in range(7):
    ano = int(input("Digite o ano de nascimento: "))
    idade = 2026 - ano
    anos.append(idade)

    if idade >= 18:
        maior.append(idade)

    else:
        menor.append(idade)


print(f"As pessoa atigiram á maior idade são : {len(maior)}  e o que faltam pra virar maior idade é: {len(menor)} ")




