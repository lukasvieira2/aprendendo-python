from sys import prefix

# Exercício 7: Validação de Nota Básica (while)
# Enunciado: Escreva um programa que peça para o usuário digitar uma nota entre 0 e 10. Se ele digitar um valor inválido
# (como 12 ou -2), o programa deve exibir uma mensagem de erro e continuar pedindo a nota até que o usuário digite um valor válido.


notaBasica=int(input("digite sua nota de 0 a 10: "))
while notaBasica < 0 or notaBasica > 10:
    print(f"Nota invalida")
    notaBasica=int(input("digite sua nota de 0 a 10: "))

print(f"Sua nota foi validada com sucesso ")

