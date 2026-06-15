#Exercício 9: Menu Interativo de Sistema (Simulando do while)
#Enunciado: Crie um menu interativo de calculadora utilizando while True. O programa deve exibir na tela:
#Somar
#Subtrair
#Multiplicar
#Dividir
#Sair


while True:
    calculadora = input("qual conta você quer calcular? [ + | - | * | / | sair ] ")
    if calculadora == "+":
        nu1 = float(input("digite um numero: "))
        nu2 = float(input("digite outro numero: "))
        soma = nu1 + nu2
        print(f"A soma foi de {soma}")
    elif calculadora == "-":
        nu3 = float(input("digite um numero: "))
        nu4 = float(input("digite outro numero: "))
        Subtrair = nu3 - nu4
        print(f"A Subtracão foi de {Subtrair}")
    elif calculadora == "*":
        nu5 = float(input("digite um numero: "))
        nu6 = float(input("digite outro numero: "))
        Multiplicar = nu5 * nu6
        print(f"A multiplicacão foi de {Multiplicar}")
    elif calculadora == "/":
        nu7 = float(input("digite um numero: "))
        nu8 = float(input("digite outro numero: "))
        Dividir = nu7 / nu8
        print(f"A divicão foi de {Dividir}")
    elif calculadora == "sair":
        print("Saindo do sistema")
        break
    else:
        print("opcão inválida")