listaIdade = []

for i in range(10):
    idade = int(input("Digite sua idade: "))
    listaIdade.append(idade)

print(listaIdade)
print("-------------------------------------------------------------------------------------")
print("Imprimindo  a idade em baixo do outro")
listaIdade.sort()

for i in listaIdade:
    print(i)