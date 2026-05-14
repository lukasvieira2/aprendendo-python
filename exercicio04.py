nascimento = int(input("Digite seu ano de nascimento: "))

idade = 2026 - nascimento



if idade >= 60:
    print(f"Você tem ", idade, " Você é idoso!")
elif idade < 18:
    print(f" Você tem ", idade, " Você é de menor de idade!")
elif idade >= 18:
    print(f"Você tem ", idade, " Você é de maior de idade!")
else:
    print(f"Você digitou errado")


