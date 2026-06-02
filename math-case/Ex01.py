print("Digite uma letra para saber se é Vogal ou Consoante (ou digite 0 para sair):")

while True:

    entrada = input("\nDigite uma letra: ").strip()

    if entrada == '0':
        print("Programa encerrado. Até logo!")
        break

    if len(entrada) != 1:
        print("Por favor, digite apenas UMA letra por vez.")
        continue
    match entrada.lower():
        case 'a' | 'e' | 'i' | 'o' | 'u':
            print(f"A letra {entrada} é uma VOGAL.")

        case c if c.isalpha():
            print(f"A letra {entrada} é uma CONSOANTE.")

        case _:
            print(f" {entrada} não é um caractere válido do alfabeto.")