
#Exercício 11: O Caixa Eletrônico / Saque de Cédulas (while)
#Enunciado: Crie um programa que simule o funcionamento de um caixa eletrônico. O usuário informa o valor que deseja sacar (número inteiro). O programa deve calcular quantas cédulas de cada valor serão entregues, priorizando as maiores. Considere que o banco possui cédulas de R$ 50, R$ 20, R$ 10 , 5 R$ e R$ 2.

#Exemplo: Saque de R$ 82 ➔ 1 cédula de R$ 50, 1 de R$ 20, 1 de R$ 10 e 1 de R$ 2.

valor = int(input("Digite o valor do saque: R$ "))

cedulas = [50, 20, 10, 5, 2]

i = 0

while i < len(cedulas):
    nota = cedulas[i]
    quantidade = valor // nota

    if quantidade > 0:
        print(f"{quantidade} cédula(s) de R$ {nota}")

    valor = valor % nota
    i += 1

if valor != 0:
    print(f"Não foi possível sacar o valor restante de R$ {valor}")
