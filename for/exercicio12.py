
#Exercício 12: Análise de Dados Estatísticos de um Grupo (Simulando do while)
#Enunciado: Construa um script que leia a idade e o sexo (M/F) de várias pessoas.
# A cada pessoa cadastrada, o programa deve perguntar se o usuário quer continuar. No final do programa, mostre:

#Quantas pessoas têm mais de 18 anos.
#Quantos homens foram cadastrados.
#Quantas mulheres têm menos de 20 anos.

quantidadeHomens = 0
quantidadeMulheres = 0
continuar = "s"
maiorIdade = 0

while continuar == "s":
    sexo = str(input("Informe o sexo [M/F]: "))
    idade = int(input("Informe a idade: "))

    if idade >= 18:
        maiorIdade += 1
    if sexo == "M":
        quantidadeHomens += 1
    if sexo == "F" and idade < 20:
        quantidadeMulheres += 1

    continuar = input("Quer continuar? (S/N): ").lower()

print("\nRESULTADO FINAL")
print(f"Pessoas com mais de 18 anos: {maiorIdade}")
print(f"Homens cadastrados: {quantidadeHomens}")
print(f"Mulheres com menos de 20 anos: {quantidadeMulheres}")




