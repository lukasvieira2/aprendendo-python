
#Exercício 2: Média de Notas com Validação
#Enunciado: Escreva um programa que receba 4 notas de um aluno, armazene-as em uma lista e calcule a média aritmética.
#Se a média for maior ou igual a 7.0,
# exiba a lista de notas e a mensagem "Aprovado".
# Caso contrário, exiba "Recuperação".

notas = []

for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("\nNotas:", notas)
print(f"Média: {media:.2f}")

if media >= 7.0:
    print("Aprovado")
else:
    print("Recuperação")