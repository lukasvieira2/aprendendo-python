salario = float(input("Escreva o seu salário: "))
parcela = float(input("Escreva o parcela que deseja: "))

limite_da_parcela_maxima = salario * 0.3

if parcela <= limite_da_parcela_maxima:
    print(f"o seu crédito foi  aprovado com a parcela de {parcela:.2f} reais com o salário de {salario:.2f} reais")
else:
    print(f"o seu crédito foi  recusado , pois ultrapassou o limite da parcela que é {limite_da_parcela_maxima:.2f} reais")