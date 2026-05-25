listaIdade = []
continuar = "s",

while continuar == "s" :
    idade = int(input("Digite sua idade: "))
    listaIdade.append(idade)
    continuar = input("Deseja continuar? [S/N]").upper()[0]

print(listaIdade)