numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


soma = numero1 + numero2 
soma1 = numero1 - numero2
soma2 = numero1 / numero2
soma3 = numero1 * numero2
soma4 = numero1 // numero2
soma5 = numero1 % numero2
soma6 = numero1 ** numero2


print("A soma é:",soma)
print("A subtração é:",soma1)
print("A divisão é:",soma2)
print("A multiplicação é:",soma3)
print("o resto da divisão é:",soma4)
print("A divisão é:",soma5)
print("A potencia é:",soma6)


print("-------------------------------------------------------------------------------------------------------------------------")
print("                                                     operações relacionais                                               ")


relacao1 = numero1 > numero2
relacao2 = numero1 < numero2
relacao3 = numero1 >= numero2
relacao4 = numero1 <= numero2
relacao5 = numero1 == numero2
relacao6 = numero1 != numero2

print("os resultados das relacão estarão abaixo: \n{}\n{}\n{}\n{}\n{}\n{}".format( relacao1,relacao2,relacao3,relacao4,relacao5,relacao6))