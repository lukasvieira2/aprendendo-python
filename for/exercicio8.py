
# Exercício 8: O Contador Regressivo de Lançamento (while)
# Enunciado: Crie um script que simule a contagem regressiva para o lançamento de um foguete. O programa deve começar em 10 e ir até 0,
# #aguardando 1 segundo entre cada número (Dica: use a função time.sleep(1) da biblioteca time). Ao final, exiba a mensagem: "Decolar!".

import time
contador = 10

while contador >= 0:
    print(contador)
    time.sleep(1)
    contador -= 1

print("Decolar!")