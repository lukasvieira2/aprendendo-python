
TRABALHO = ""
while True:
    trabalho = (input("Digite codigo 100|101|102|103 ?  "))
    match trabalho.upper():
        case "100":
            print("Cachorro-Quente - R$ 10,00")

        case "101":
            print("Bauru Simples - R$ 12,00")
        case "102":
            print("X-Salada - R$ 15,00")
        case  "103":
            print("Hambúrguer - R$ 13,00")

        case _:
            print("Código de produto inválido.")
            break

