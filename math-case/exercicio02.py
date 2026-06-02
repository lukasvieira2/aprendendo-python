
TRABALHO = ""
while True:
    trabalho = (input("Digite uma letra A|B|C|D|F "))
    match trabalho.upper():
        case "A":
            print("Excelente trabalho")

        case "B":
            print("Bom desempenho")
        case  "C":
            print("Satisfatório")
        case  "D":
            print("Abaixo da média (Atenção).")

        case  "F":
            print("Reprovado")

        case 0:
            break
        case _:
            print("Conceito desconhecido")


