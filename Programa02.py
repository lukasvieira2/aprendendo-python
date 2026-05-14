n1 = float(input("Escreva o primeiro número: ").replace(",", "."))
n2 = float(input("Escreva o segundo número: ").replace(",", "."))
n3 = float(input("Escreva o terceiro número: ").replace(",", "."))

media = (n1 + n2 + n3) / 3

# Exibe a média formatada com 2 casas decimais
print(f"\nMédia final: {media:.2f}")

if media >= 7:
    print("O aluno foi aprovado!")
elif media >= 5:
    print("O aluno está de recuperação.")
else:
    print("O aluno está reprovado.")