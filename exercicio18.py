
# Exercício 18: Contador de Intervalos Customizado (Básico)
# Enunciado: Escreva um script que solicite três valores ao usuário: um valor inicial,
# um valor final e um valor de passo (de quanto em quanto a contagem deve andar).
# Use o laço for para exibir a contagem na tela.
# Exemplo: Inicial: 2, Final: 12, Passo: 3. Saída: 2, 5, 8, 11.


inicial = int(input("Digite o valor inicial: "))
final = int(input("Digite o valor final: "))
passo = int(input("Digite o valor do passo: "))

print("\nResultado da contagem:")
# Somamos 1 ao 'final' para garantir que ele seja considerado caso o passo bata em cima dele
for contagem in range(inicial, final + 1, passo):
    print(contagem, end=" ")
print() # Apenas para pular linha no final


print("\n" + "="*50 + "\n")

