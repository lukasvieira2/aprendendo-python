while True:
    mes = int(input("Digite o número do mês (1 a 12) ou 0 para sair: "))

    match mes:
        case 12 | 1 | 2:
            print("Verão")

        case 3 | 4 | 5:
            print("Outono")

        case 6 | 7 | 8:
            print("Inverno")

        case 9 | 10 | 11:
            print("Primavera")

        case 0:
            break

        case _:
            print("Mês inválido")