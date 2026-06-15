peso = float(input("Qual o seu peso?"))
altura = float(input("Qual a sua altura?"))

total = peso / (altura * altura)

if total < (18.5):
    print(f"Você està com ", total, " pesos",", Você ta abaixo de peso! ")
elif total <= 24.9:
    print(f"Você està com ", total, " pesos",", peso normal! ")
elif total >= 25:
    print(f"Você està com ", total, " pesos",", Sobrepeso! ")
elif total >= 30:
    print(f"Você està com ", total, " pesos",", Obesidade Grau I! ")
elif total >= 35:
    print(f"Você està com ", total, " pesos",", Obesidade Grau II! ")
elif total >40:
    print(f"Você està com ", total, " pesos"," Obesidade Grau III! ")
else:
    print(f"Você digitou errado! ")
    print(f"Você està com", total, "pesos")